"""Farland Auto Clicker: compact Persian Windows desktop interface."""

from __future__ import annotations

import queue
import sys
import tkinter as tk
import webbrowser
from pathlib import Path
from tkinter import messagebox

from click_engine import ClickEngine, MAX_CPS
from settings import load_settings, save_settings


TITLE = "Farland Auto Clicker"
HOTKEY_LABELS = {
    "middle": "کلیک وسط موس", "x1": "دکمه کناری موس ۱", "x2": "دکمه کناری موس ۲",
    "f6": "F6", "f7": "F7", "f8": "F8", "f9": "F9",
    "home": "Home", "end": "End", "insert": "Insert",
}
THEME_LABELS = {"dark": "تیره", "light": "روشن", "purple": "بنفش", "blue": "آبی"}
PALETTES = {
    "dark": dict(bg="#10141c", card="#1d2430", field="#2a3443", fg="#f3f6fb", muted="#a7b4c5", accent="#4c82ef", border="#303c4d"),
    "light": dict(bg="#edf2f7", card="#ffffff", field="#e8eff6", fg="#152232", muted="#607286", accent="#326ee7", border="#d6e0eb"),
    "purple": dict(bg="#181323", card="#292038", field="#3a2d4d", fg="#faf4ff", muted="#c6b6d5", accent="#a16ae8", border="#49365f"),
    "blue": dict(bg="#0b1b2b", card="#152c43", field="#23405d", fg="#eff8ff", muted="#a4c2d9", accent="#3c9ce6", border="#2b526f"),
}
GREEN = "#21996a"
RED = "#cf4c5c"
FOOTER = "© بردیا علیزاده ملقب به کبیر | @farland_game"
LINKS = [
    ("YouTube", "https://www.youtube.com/@Farland_game"),
    ("YouTube 2", "https://www.youtube.com/@Farland_animation"),
    ("Rubika Channel", "https://rubika.ir/farland_gam"),
    ("Rubika Channel 2", "https://rubika.ir/Farland_animatio"),
    ("Rubika Page", "https://rubika.ir/farland_game"),
    ("Rubika Page 2", "https://rubika.ir/Farland_animations"),
    ("Instagram", "https://www.instagram.com/farland_game?igsh=MXM2anZhZXEzMXQwYQ"),
    ("Telegram Channel", "https://t.me/Farland_gam"),
    ("Telegram Channel 2", "https://t.me/Farland_animatio"),
    ("Farland Music Bot", "https://t.me/@Farland_Music_bot"),
    ("Twitch", "https://twitch.tv/farlandgame"),
    ("Kick", "https://kick.com/farlandgame"),
    ("Aparat", "https://aparat.com/Farland_Game"),
    ("THE APEX YouTube", "https://www.youtube.com/@THE_APEX_MC"),
    ("THE APEX Telegram", "https://t.me/+-3uY7eIZArVjZDE0"),
    ("گروه تلگرام منهانت", "https://t.me/+DAq20XrkPyZhNjVk"),
    ("حمایت مالی / دونیت ❤️", "https://reymit.ir/farland_game"),
]


class FarlandApp:
    def __init__(self) -> None:
        self.root = tk.Tk()
        self.root.title(TITLE)
        self.root.geometry("520x640")
        self.root.minsize(490, 620)
        self.root.resizable(True, True)
        icon = Path(__file__).with_name("farland.ico")
        if icon.exists():
            try:
                self.root.iconbitmap(str(icon))
            except tk.TclError:
                pass
        self.settings = load_settings()
        self.events: queue.SimpleQueue[tuple[str, object]] = queue.SimpleQueue()
        self.engine = ClickEngine(lambda kind, value: self.events.put((kind, value)))
        self.engine.configure(
            cps={side: self.settings[f"{side}_cps"] for side in ("left", "right")},
            enabled={side: self.settings[f"{side}_enabled"] for side in ("left", "right")},
            hotkey=self.settings["hotkey"],
        )
        self.active = False
        self.about_window: tk.Toplevel | None = None
        self._closing = False
        self._build()
        self.root.protocol("WM_DELETE_WINDOW", self.close)
        self.root.after(20, self._start_engine)
        self.root.after(40, self._poll_events)

    @property
    def colors(self) -> dict[str, str]:
        return PALETTES[self.settings["theme"]]

    def _label(self, parent, text: str, *, size=11, bold=False, color=None, bg=None, **kwargs):
        c = self.colors
        return tk.Label(parent, text=text, font=("Segoe UI", size, "bold" if bold else "normal"),
                        fg=color or c["fg"], bg=bg or c["bg"], **kwargs)

    def _button(self, parent, text: str, command, *, bg=None, fg="#ffffff", size=11, **kwargs):
        return tk.Button(parent, text=text, command=command, font=("Segoe UI", size, "bold"),
                         bg=bg or self.colors["accent"], fg=fg, activeforeground=fg,
                         activebackground=bg or self.colors["accent"], relief="flat",
                         bd=0, cursor="hand2", **kwargs)

    def _build(self) -> None:
        if hasattr(self, "shell"):
            self.shell.destroy()
        c = self.colors
        self.root.configure(bg=c["bg"])
        self.shell = tk.Frame(self.root, bg=c["bg"])
        self.shell.pack(fill="both", expand=True)
        self._label(self.shell, FOOTER, size=9, color=c["muted"],
                    anchor="center").pack(side="bottom", fill="x", pady=(8, 12))
        content = tk.Frame(self.shell, bg=c["bg"])
        content.pack(fill="both", expand=True, padx=24, pady=(12, 0))

        self._label(content, TITLE, size=21, bold=True, anchor="center").pack(fill="x")
        self._label(content, "ساخته‌شده توسط بردیا علیزاده ملقب به کبیر", size=10,
                    color=c["muted"], anchor="center").pack(fill="x", pady=(2, 0))
        self._label(content, "@farland_game", size=10, color=c["accent"],
                    anchor="center").pack(fill="x", pady=(1, 10))

        cards = tk.Frame(content, bg=c["bg"])
        cards.pack(fill="x")
        cards.columnconfigure((0, 1), weight=1, uniform="cards")
        self._card(cards, "left", "کلیک چپ", 0)
        self._card(cards, "right", "کلیک راست", 1)

        status_box = tk.Frame(content, bg=c["card"], highlightbackground=c["border"], highlightthickness=1)
        status_box.pack(fill="x", pady=(10, 0))
        self.status_label = self._label(status_box, "●  اتوکلیکر غیرفعال است", size=12,
                                        bold=True, color=c["muted"], bg=c["card"], anchor="center")
        self.status_label.pack(fill="x", pady=(8, 5))
        self.main_button = self._button(status_box, "فعال‌سازی", self._toggle,
                                        bg=c["accent"], size=13, height=2)
        self.main_button.pack(fill="x", padx=13, pady=(0, 9))

        settings_box = tk.Frame(content, bg=c["card"], highlightbackground=c["border"], highlightthickness=1)
        settings_box.pack(fill="x", pady=(10, 0))
        self._label(settings_box, "تنظیمات", size=13, bold=True, bg=c["card"], anchor="e").pack(fill="x", padx=14, pady=(8, 3))
        row = tk.Frame(settings_box, bg=c["card"])
        row.pack(fill="x", padx=14)
        self._label(row, "کلید میانبر", bg=c["card"], anchor="e").pack(side="right", padx=(8, 0))
        self.hotkey_var = tk.StringVar(value=HOTKEY_LABELS[self.settings["hotkey"]])
        hotkey_menu = tk.OptionMenu(row, self.hotkey_var, *HOTKEY_LABELS.values(), command=self._change_hotkey)
        self._style_menu(hotkey_menu)
        hotkey_menu.pack(side="left", fill="x", expand=True)
        self._label(settings_box, "کلید انتخاب‌شده، اتوکلیکر را روشن یا خاموش می‌کند.", size=9,
                    color=c["muted"], bg=c["card"], anchor="e").pack(fill="x", padx=14, pady=(2, 0))
        self._label(settings_box, "خروج اضطراری: F12", size=10, color=RED,
                    bg=c["card"], anchor="e").pack(fill="x", padx=14, pady=(2, 7))

        bottom = tk.Frame(content, bg=c["bg"])
        bottom.pack(fill="x", pady=(10, 0))
        bottom.columnconfigure(0, weight=1)
        bottom.columnconfigure(1, weight=1)
        self._label(bottom, "تم", size=11, bg=c["bg"], width=4,
                    anchor="center").grid(row=0, column=2, sticky="e", padx=(8, 0))
        self.theme_var = tk.StringVar(value=THEME_LABELS[self.settings["theme"]])
        theme_menu = tk.OptionMenu(bottom, self.theme_var, *THEME_LABELS.values(), command=self._change_theme)
        self._style_menu(theme_menu)
        theme_menu.grid(row=0, column=1, sticky="ew", padx=(8, 0))
        self._button(bottom, "درباره Farland و لینک‌ها", self._open_about,
                     bg=c["field"], fg=c["fg"], size=10, padx=11).grid(row=0, column=0, sticky="ew", ipady=7)

        self._refresh_active()

    def _style_menu(self, menu: tk.OptionMenu) -> None:
        c = self.colors
        menu.configure(font=("Segoe UI", 10), bg=c["field"], fg=c["fg"],
                       activebackground=c["accent"], activeforeground="#ffffff",
                       relief="flat", bd=0, highlightthickness=0, cursor="hand2")
        menu["menu"].configure(font=("Segoe UI", 10), bg=c["card"], fg=c["fg"],
                               activebackground=c["accent"], activeforeground="#ffffff")

    def _card(self, parent, side: str, title: str, column: int) -> None:
        c = self.colors
        card = tk.Frame(parent, bg=c["card"], highlightbackground=c["border"], highlightthickness=1)
        card.grid(row=0, column=column, sticky="nsew", padx=(0, 7) if column == 0 else (7, 0))
        self._label(card, title, size=13, bold=True, bg=c["card"], anchor="center").pack(fill="x", pady=(10, 5))
        value = tk.StringVar(value=str(self.settings[f"{side}_cps"]))
        if not hasattr(self, "cps_vars"):
            self.cps_vars = {}
        self.cps_vars[side] = value
        entry = tk.Entry(card, textvariable=value, justify="center", font=("Segoe UI", 22, "bold"),
                         bg=c["field"], fg=c["fg"], insertbackground=c["fg"], relief="flat",
                         highlightthickness=1, highlightbackground=c["border"], width=4)
        entry.pack(padx=22, fill="x", ipady=3)
        entry.bind("<FocusOut>", lambda _event, s=side: self._commit_cps(s))
        entry.bind("<Return>", lambda _event, s=side: self._commit_cps(s))
        self._label(card, "کلیک در ثانیه (تا ۱۰٬۰۰۰)", size=9, color=c["muted"],
                    bg=c["card"], anchor="center").pack(fill="x", pady=(3, 5))
        button = self._button(card, "", lambda s=side: self._toggle_side(s), size=10, height=2)
        button.pack(fill="x", padx=10, pady=(0, 8))
        if not hasattr(self, "side_buttons"):
            self.side_buttons = {}
        self.side_buttons[side] = button
        self._refresh_side(side)

    def _commit_cps(self, side: str) -> None:
        raw = self.cps_vars[side].get().strip()
        try:
            value = int(raw)
        except ValueError:
            value = None
        if value is None or not 1 <= value <= MAX_CPS:
            self.cps_vars[side].set(str(self.settings[f"{side}_cps"]))
            self.root.bell()
            return
        self.settings[f"{side}_cps"] = value
        self.engine.configure(cps={side: value})
        self._save()

    def _refresh_side(self, side: str) -> None:
        label = "کلیک چپ" if side == "left" else "کلیک راست"
        enabled = self.settings[f"{side}_enabled"]
        color = GREEN if enabled else RED
        self.side_buttons[side].configure(text=f"{label} {'فعال است' if enabled else 'غیرفعال است'}",
                                          bg=color, activebackground=color)

    def _toggle_side(self, side: str) -> None:
        self._commit_cps(side)
        enabled = not self.settings[f"{side}_enabled"]
        self.settings[f"{side}_enabled"] = enabled
        self.engine.configure(enabled={side: enabled})
        self._refresh_side(side)
        self._save()

    def _toggle(self) -> None:
        for side in ("left", "right"):
            self._commit_cps(side)
        self.engine.toggle()

    def _refresh_active(self) -> None:
        if self.active:
            self.status_label.configure(text="●  اتوکلیکر فعال است", fg=GREEN)
            self.main_button.configure(text="غیرفعال‌سازی", bg=RED, activebackground=RED)
        else:
            self.status_label.configure(text="●  اتوکلیکر غیرفعال است", fg=self.colors["muted"])
            self.main_button.configure(text="فعال‌سازی", bg=self.colors["accent"],
                                       activebackground=self.colors["accent"])

    def _change_hotkey(self, label: str) -> None:
        key = next(key for key, value in HOTKEY_LABELS.items() if value == label)
        self.settings["hotkey"] = key
        self.engine.configure(hotkey=key)
        self._save()

    def _change_theme(self, label: str) -> None:
        theme = next(key for key, value in THEME_LABELS.items() if value == label)
        if theme == self.settings["theme"]:
            return
        for side in ("left", "right"):
            self._commit_cps(side)
        self.settings["theme"] = theme
        self._save()
        self.side_buttons = {}
        self.cps_vars = {}
        self._build()
        if self.about_window and self.about_window.winfo_exists():
            self.about_window.destroy()
            self.about_window = None
            self._open_about()

    def _save(self) -> None:
        try:
            save_settings(self.settings)
        except OSError as exc:
            messagebox.showwarning(TITLE, f"ذخیره تنظیمات انجام نشد:\n{exc}", parent=self.root)

    def _open_about(self) -> None:
        if self.about_window and self.about_window.winfo_exists():
            self.about_window.lift()
            self.about_window.focus_force()
            return
        c = self.colors
        window = tk.Toplevel(self.root, bg=c["bg"])
        self.about_window = window
        window.title("درباره Farland")
        window.geometry("500x600")
        window.minsize(430, 450)
        self._label(window, "درباره Farland", size=20, bold=True, anchor="center").pack(fill="x", pady=(15, 3))
        self._label(window, "بردیا علیزاده ملقب به کبیر", size=11, anchor="center").pack(fill="x")
        self._label(window, "Farland_game  |  Telegram: @farland_game", size=10,
                    color=c["muted"], anchor="center").pack(fill="x", pady=(2, 10))

        holder = tk.Frame(window, bg=c["bg"])
        holder.pack(fill="both", expand=True, padx=17)
        canvas = tk.Canvas(holder, bg=c["bg"], highlightthickness=0)
        scrollbar = tk.Scrollbar(holder, orient="vertical", command=canvas.yview)
        inner = tk.Frame(canvas, bg=c["bg"])
        inner.bind("<Configure>", lambda _event: canvas.configure(scrollregion=canvas.bbox("all")))
        canvas.create_window((0, 0), window=inner, anchor="nw", tags="inner")
        canvas.bind("<Configure>", lambda event: canvas.itemconfigure("inner", width=event.width))
        canvas.configure(yscrollcommand=scrollbar.set)
        scrollbar.pack(side="right", fill="y")
        canvas.pack(side="left", fill="both", expand=True)
        for index, (title, url) in enumerate(LINKS):
            self._button(inner, title, lambda u=url: webbrowser.open(u),
                         bg=c["card"], fg=c["fg"], size=10, anchor="center").pack(fill="x", pady=3, ipady=6)
            if title == "Farland Music Bot":
                self._label(inner, "برای پیدا کردن موسیقی، لینک ویدیو را برای ربات ارسال کنید.",
                            size=9, color=c["muted"], anchor="e").pack(fill="x", pady=(1, 5))
        self._label(window, FOOTER, size=9, color=c["muted"], anchor="center").pack(fill="x", pady=10)

    def _start_engine(self) -> None:
        try:
            self.engine.start()
        except Exception as exc:
            messagebox.showerror(TITLE, f"ثبت میانبرهای سراسری ممکن نشد:\n{exc}", parent=self.root)
            self.close()

    def _poll_events(self) -> None:
        if self._closing:
            return
        try:
            while True:
                kind, value = self.events.get_nowait()
                if kind == "active":
                    self.active = bool(value)
                    self._refresh_active()
                elif kind == "emergency":
                    self.close()
                    return
                elif kind == "error":
                    self.active = False
                    self._refresh_active()
                    messagebox.showerror(TITLE, f"ایجاد کلیک ممکن نشد:\n{value}", parent=self.root)
        except queue.Empty:
            pass
        self.root.after(40, self._poll_events)

    def close(self) -> None:
        if self._closing:
            return
        self._closing = True
        self.engine.stop()
        self._save()
        self.root.destroy()

    def run(self) -> None:
        self.root.mainloop()


if __name__ == "__main__":
    if sys.platform != "win32":
        raise SystemExit("Farland Auto Clicker requires Windows")
    FarlandApp().run()
