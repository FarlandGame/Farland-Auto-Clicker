"""Scheduler and hook behavior tests; no real mouse input is generated."""

import ctypes
import threading
import time
import unittest

from click_engine import (
    ClickEngine, KBDLLHOOKSTRUCT, MSLLHOOKSTRUCT, POINT,
    WM_KEYDOWN, WM_KEYUP, WM_LBUTTONDOWN, WM_MBUTTONDOWN,
)


class ClickEngineTests(unittest.TestCase):
    def setUp(self):
        self.clicks = []
        self.events = []
        self.batches = []
        self.lock = threading.Lock()

        def sender(button, count):
            with self.lock:
                self.batches.append(count)
                self.clicks.extend((button, time.perf_counter()) for _ in range(count))

        self.engine = ClickEngine(lambda kind, value: self.events.append((kind, value)), sender)
        self.engine.scheduler.start()

    def tearDown(self):
        self.engine.stop()

    def test_inactive_and_disabled_sides(self):
        self.engine.trigger("left")
        time.sleep(0.05)
        self.assertEqual(self.clicks, [])
        self.engine.configure(enabled={"right": False}, cps={"left": 5})
        self.engine.set_active(True)
        self.engine.trigger("right")
        self.engine.trigger("left")
        time.sleep(0.85)
        self.assertEqual([button for button, _ in self.clicks], ["left"] * 5)

    def test_stop_cancels_pending_clicks(self):
        self.engine.configure(cps={"left": 50})
        self.engine.set_active(True)
        self.engine.trigger("left")
        time.sleep(0.08)
        self.engine.set_active(False)
        stopped_count = len(self.clicks)
        time.sleep(0.15)
        self.assertEqual(len(self.clicks), stopped_count)
        self.assertLess(stopped_count, 50)

    def test_simultaneous_sides(self):
        self.engine.configure(cps={"left": 10, "right": 10})
        self.engine.set_active(True)
        self.engine.trigger("left")
        self.engine.trigger("right")
        time.sleep(1.05)
        self.assertEqual(sum(button == "left" for button, _ in self.clicks), 10)
        self.assertEqual(sum(button == "right" for button, _ in self.clicks), 10)

    def test_ten_thousand_cps_is_accepted_and_batched(self):
        self.engine.configure(cps={"left": 10_000})
        self.assertEqual(self.engine.cps["left"], 10_000)
        self.engine.configure(cps={"left": 10_001})
        self.assertEqual(self.engine.cps["left"], 10_000)
        self.engine.set_active(True)
        self.engine.trigger("left")
        time.sleep(1.08)
        self.assertEqual(len(self.clicks), 10_000)
        self.assertLessEqual(max(self.batches), 50)
        self.assertLessEqual(len(self.batches), 200)

    def test_physical_hook_and_injected_filter(self):
        self.engine.configure(cps={"left": 2})
        middle = MSLLHOOKSTRUCT(POINT(0, 0), 0, 0, 0, 0)
        self.engine._mouse_callback(0, WM_MBUTTONDOWN, ctypes.addressof(middle))
        self.assertTrue(self.engine.active)
        injected = MSLLHOOKSTRUCT(POINT(0, 0), 0, 1, 0, 0)
        self.engine._mouse_callback(0, WM_LBUTTONDOWN, ctypes.addressof(injected))
        time.sleep(0.04)
        self.assertEqual(self.clicks, [])
        physical = MSLLHOOKSTRUCT(POINT(0, 0), 0, 0, 0, 0)
        self.engine._mouse_callback(0, WM_LBUTTONDOWN, ctypes.addressof(physical))
        time.sleep(0.55)
        self.assertEqual(len(self.clicks), 2)
        self.engine._mouse_callback(0, WM_MBUTTONDOWN, ctypes.addressof(middle))
        self.assertFalse(self.engine.active)

    def test_keyboard_hotkey_repeat_and_emergency(self):
        self.engine.configure(hotkey="f6")
        f6 = KBDLLHOOKSTRUCT(0x75, 0, 0, 0, 0)
        self.engine._key_callback(0, WM_KEYDOWN, ctypes.addressof(f6))
        self.assertTrue(self.engine.active)
        self.engine._key_callback(0, WM_KEYDOWN, ctypes.addressof(f6))
        self.assertTrue(self.engine.active)
        self.engine._key_callback(0, WM_KEYUP, ctypes.addressof(f6))
        self.engine._key_callback(0, WM_KEYDOWN, ctypes.addressof(f6))
        self.assertFalse(self.engine.active)
        self.engine.set_active(True)
        f12 = KBDLLHOOKSTRUCT(0x7B, 0, 0, 0, 0)
        self.engine._key_callback(0, WM_KEYDOWN, ctypes.addressof(f12))
        self.assertFalse(self.engine.active)
        self.assertIn(("emergency", None), self.events)


if __name__ == "__main__":
    unittest.main()
