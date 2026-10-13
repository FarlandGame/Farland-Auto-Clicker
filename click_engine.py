"""Global Windows input hooks and the timed click scheduler.

Physical clicks are identified by the low-level hook's injected flag. SendInput
clicks are marked as injected by Windows and never start another burst.
"""

from __future__ import annotations

import ctypes
import heapq
import itertools
import math
import threading
import time
from ctypes import wintypes
from typing import Callable


user32 = ctypes.WinDLL("user32", use_last_error=True)
kernel32 = ctypes.WinDLL("kernel32", use_last_error=True)
ULONG_PTR = ctypes.c_size_t
LRESULT = ctypes.c_ssize_t

WH_KEYBOARD_LL = 13
WH_MOUSE_LL = 14
WM_QUIT = 0x0012
WM_KEYDOWN = 0x0100
WM_KEYUP = 0x0101
WM_SYSKEYDOWN = 0x0104
WM_SYSKEYUP = 0x0105
WM_LBUTTONDOWN = 0x0201
WM_RBUTTONDOWN = 0x0204
WM_MBUTTONDOWN = 0x0207
WM_XBUTTONDOWN = 0x020B
LLMHF_INJECTED = 0x01
LLKHF_INJECTED = 0x10
VK_F12 = 0x7B
XBUTTON1 = 1
XBUTTON2 = 2
MAX_CPS = 10_000
MAX_BATCH_CLICKS = 50
TARGET_BATCHES_PER_SECOND = 200

HOTKEYS = {
    "middle": ("mouse", "middle"),
    "x1": ("mouse", "x1"),
    "x2": ("mouse", "x2"),
    "f6": ("key", 0x75),
    "f7": ("key", 0x76),
    "f8": ("key", 0x77),
    "f9": ("key", 0x78),
    "home": ("key", 0x24),
    "end": ("key", 0x23),
    "insert": ("key", 0x2D),
}


class POINT(ctypes.Structure):
    _fields_ = [("x", wintypes.LONG), ("y", wintypes.LONG)]


class MSLLHOOKSTRUCT(ctypes.Structure):
    _fields_ = [
        ("pt", POINT), ("mouseData", wintypes.DWORD),
        ("flags", wintypes.DWORD), ("time", wintypes.DWORD),
        ("dwExtraInfo", ULONG_PTR),
    ]


class KBDLLHOOKSTRUCT(ctypes.Structure):
    _fields_ = [
        ("vkCode", wintypes.DWORD), ("scanCode", wintypes.DWORD),
        ("flags", wintypes.DWORD), ("time", wintypes.DWORD),
        ("dwExtraInfo", ULONG_PTR),
    ]


class MOUSEINPUT(ctypes.Structure):
    _fields_ = [
        ("dx", wintypes.LONG), ("dy", wintypes.LONG),
        ("mouseData", wintypes.DWORD), ("dwFlags", wintypes.DWORD),
        ("time", wintypes.DWORD), ("dwExtraInfo", ULONG_PTR),
    ]


class INPUT_UNION(ctypes.Union):
    _fields_ = [("mi", MOUSEINPUT)]


class INPUT(ctypes.Structure):
    _fields_ = [("type", wintypes.DWORD), ("data", INPUT_UNION)]


HOOKPROC = ctypes.WINFUNCTYPE(LRESULT, ctypes.c_int, wintypes.WPARAM, wintypes.LPARAM)
user32.SetWindowsHookExW.argtypes = (ctypes.c_int, HOOKPROC, wintypes.HINSTANCE, wintypes.DWORD)
user32.SetWindowsHookExW.restype = wintypes.HHOOK
user32.CallNextHookEx.argtypes = (wintypes.HHOOK, ctypes.c_int, wintypes.WPARAM, wintypes.LPARAM)
user32.CallNextHookEx.restype = LRESULT
user32.UnhookWindowsHookEx.argtypes = (wintypes.HHOOK,)
user32.UnhookWindowsHookEx.restype = wintypes.BOOL
user32.GetMessageW.argtypes = (ctypes.POINTER(wintypes.MSG), wintypes.HWND, wintypes.UINT, wintypes.UINT)
user32.GetMessageW.restype = wintypes.BOOL
user32.PostThreadMessageW.argtypes = (wintypes.DWORD, wintypes.UINT, wintypes.WPARAM, wintypes.LPARAM)
user32.PostThreadMessageW.restype = wintypes.BOOL
user32.PeekMessageW.argtypes = (ctypes.POINTER(wintypes.MSG), wintypes.HWND, wintypes.UINT, wintypes.UINT, wintypes.UINT)
user32.PeekMessageW.restype = wintypes.BOOL
user32.SendInput.argtypes = (wintypes.UINT, ctypes.POINTER(INPUT), ctypes.c_int)
user32.SendInput.restype = wintypes.UINT
kernel32.GetCurrentThreadId.restype = wintypes.DWORD


def send_clicks(button: str, count: int) -> None:
    """Send a small batch of press/release pairs at the pointer position."""
    down, up = (0x0002, 0x0004) if button == "left" else (0x0008, 0x0010)
    inputs = (INPUT * (2 * count))()
    for index in range(count):
        inputs[index * 2].type = 0
        inputs[index * 2].data.mi.dwFlags = down
        inputs[index * 2 + 1].type = 0
        inputs[index * 2 + 1].data.mi.dwFlags = up
    if user32.SendInput(2 * count, inputs, ctypes.sizeof(INPUT)) != 2 * count:
        raise OSError(ctypes.get_last_error(), "SendInput failed")


class ClickEngine:
    """One scheduler handles simultaneous left/right bursts without busy loops."""

    def __init__(self, on_change: Callable[[str, object], None], sender=send_clicks):
        self.on_change = on_change
        self.sender = sender
        self.condition = threading.Condition(threading.RLock())
        self.active = False
        self.closed = False
        self.generation = 0
        self.cps = {"left": 10, "right": 10}
        self.enabled = {"left": True, "right": True}
        self.hotkey = "middle"
        self.jobs: list[tuple[float, int, int, str, int, float, int]] = []
        self.sequence = itertools.count()
        self.scheduler = threading.Thread(target=self._run_scheduler, name="click-scheduler", daemon=True)
        self.hook_thread = threading.Thread(target=self._run_hooks, name="input-hooks", daemon=True)
        self.hook_ready = threading.Event()
        self.hook_error: Exception | None = None
        self.hook_thread_id = 0
        self.pressed_keys: set[int] = set()
        self.mouse_proc = None
        self.key_proc = None

    def start(self) -> None:
        self.scheduler.start()
        self.hook_thread.start()
        if not self.hook_ready.wait(5):
            self.stop()
            raise RuntimeError("Global input hooks did not start")
        if self.hook_error:
            self.stop()
            raise RuntimeError(f"Global input hooks failed: {self.hook_error}")

    def configure(self, *, cps: dict[str, int] | None = None,
                  enabled: dict[str, bool] | None = None, hotkey: str | None = None) -> None:
        with self.condition:
            if cps:
                for button, value in cps.items():
                    if button in self.cps and type(value) is int and 1 <= value <= MAX_CPS:
                        self.cps[button] = value
            if enabled:
                for button, value in enabled.items():
                    if button in self.enabled:
                        self.enabled[button] = bool(value)
                        if not value:
                            self._cancel_button(button)
            if hotkey in HOTKEYS:
                self.hotkey = hotkey
                self.pressed_keys.clear()

    def set_active(self, active: bool) -> None:
        with self.condition:
            if self.closed or self.active == active:
                return
            self.active = active
            if not active:
                self.jobs.clear()
                self.generation += 1
            self.condition.notify_all()
        self.on_change("active", active)

    def toggle(self) -> None:
        with self.condition:
            target = not self.active
        self.set_active(target)

    def trigger(self, button: str) -> None:
        """Target CPS synthetic clicks over the next second, in small batches."""
        with self.condition:
            if self.closed or not self.active or not self.enabled[button]:
                return
            count = self.cps[button]
            batch_size = min(MAX_BATCH_CLICKS, max(1, math.ceil(count / TARGET_BATCHES_PER_SECOND)))
            heapq.heappush(self.jobs, (time.perf_counter(), next(self.sequence),
                                       self.generation, button, count, 1.0 / count, batch_size))
            self.condition.notify()

    def emergency_stop(self) -> None:
        self.set_active(False)
        self.on_change("emergency", None)

    def stop(self) -> None:
        with self.condition:
            if self.closed:
                return
            self.closed = True
            self.active = False
            self.jobs.clear()
            self.generation += 1
            self.condition.notify_all()
        if self.hook_thread_id:
            user32.PostThreadMessageW(self.hook_thread_id, WM_QUIT, 0, 0)
        if self.scheduler.is_alive() and threading.current_thread() is not self.scheduler:
            self.scheduler.join(timeout=2)
        if self.hook_thread.is_alive() and threading.current_thread() is not self.hook_thread:
            self.hook_thread.join(timeout=2)

    def _cancel_button(self, button: str) -> None:
        self.jobs = [job for job in self.jobs if job[3] != button]
        heapq.heapify(self.jobs)
        self.condition.notify_all()

    def _run_scheduler(self) -> None:
        while True:
            with self.condition:
                while not self.closed and not self.jobs:
                    self.condition.wait()
                if self.closed:
                    return
                due, _, generation, button, remaining, interval, batch_size = self.jobs[0]
                delay = due - time.perf_counter()
                if delay > 0:
                    self.condition.wait(delay)
                    continue
                heapq.heappop(self.jobs)
                if generation != self.generation or not self.active or not self.enabled[button]:
                    continue
            # SendInput can invoke the mouse hook synchronously. Never hold the
            # condition while calling it, or a physical hotkey could deadlock.
            sending = min(batch_size, remaining)
            try:
                self.sender(button, sending)
            except Exception as exc:
                with self.condition:
                    self.active = False
                    self.jobs.clear()
                    self.generation += 1
                self.on_change("error", str(exc))
                continue
            with self.condition:
                if self.closed or generation != self.generation or not self.active:
                    continue
                remaining -= sending
                if remaining:
                    next_due = due + interval * sending
                    heapq.heappush(self.jobs, (next_due, next(self.sequence), generation,
                                               button, remaining, interval, batch_size))

    def _run_hooks(self) -> None:
        self.hook_thread_id = kernel32.GetCurrentThreadId()
        self.mouse_proc = HOOKPROC(self._mouse_callback)
        self.key_proc = HOOKPROC(self._key_callback)
        mouse_hook = user32.SetWindowsHookExW(WH_MOUSE_LL, self.mouse_proc, None, 0)
        key_hook = user32.SetWindowsHookExW(WH_KEYBOARD_LL, self.key_proc, None, 0)
        if not mouse_hook or not key_hook:
            self.hook_error = ctypes.WinError(ctypes.get_last_error())
            self.hook_ready.set()
            if mouse_hook:
                user32.UnhookWindowsHookEx(mouse_hook)
            if key_hook:
                user32.UnhookWindowsHookEx(key_hook)
            return
        # Create this thread's message queue before start() reports success.
        user32.PeekMessageW(ctypes.byref(wintypes.MSG()), None, 0, 0, 0)
        self.hook_ready.set()
        try:
            message = wintypes.MSG()
            while user32.GetMessageW(ctypes.byref(message), None, 0, 0) > 0:
                pass
        finally:
            user32.UnhookWindowsHookEx(mouse_hook)
            user32.UnhookWindowsHookEx(key_hook)

    def _mouse_callback(self, code: int, message: int, address: int) -> int:
        if code >= 0 and not self.closed:
            info = ctypes.cast(address, ctypes.POINTER(MSLLHOOKSTRUCT)).contents
            if not (info.flags & LLMHF_INJECTED):
                button = None
                if message == WM_LBUTTONDOWN:
                    button = "left"
                elif message == WM_RBUTTONDOWN:
                    button = "right"
                if button:
                    self.trigger(button)
                elif message in (WM_MBUTTONDOWN, WM_XBUTTONDOWN):
                    mouse_key = "middle" if message == WM_MBUTTONDOWN else (
                        "x1" if info.mouseData >> 16 == XBUTTON1 else "x2")
                    with self.condition:
                        selected = self.hotkey == mouse_key
                    if selected:
                        self.toggle()
        return user32.CallNextHookEx(None, code, message, address)

    def _key_callback(self, code: int, message: int, address: int) -> int:
        if code >= 0 and not self.closed:
            info = ctypes.cast(address, ctypes.POINTER(KBDLLHOOKSTRUCT)).contents
            if not (info.flags & LLKHF_INJECTED):
                key = info.vkCode
                if message in (WM_KEYUP, WM_SYSKEYUP):
                    self.pressed_keys.discard(key)
                elif message in (WM_KEYDOWN, WM_SYSKEYDOWN) and key not in self.pressed_keys:
                    self.pressed_keys.add(key)
                    if key == VK_F12:
                        self.emergency_stop()
                    else:
                        with self.condition:
                            selected = HOTKEYS[self.hotkey] == ("key", key)
                        if selected:
                            self.toggle()
        return user32.CallNextHookEx(None, code, message, address)
