"""Small, validated, atomic JSON settings store."""

from __future__ import annotations

import json
import os
from pathlib import Path

from click_engine import HOTKEYS, MAX_CPS


APP_DIR = Path(os.environ.get("APPDATA", Path.home())) / "Farland Auto Clicker"
SETTINGS_FILE = APP_DIR / "settings.json"
THEMES = ("dark", "light", "purple", "blue")
DEFAULTS = {
    "left_cps": 10,
    "right_cps": 10,
    "left_enabled": True,
    "right_enabled": True,
    "hotkey": "middle",
    "theme": "dark",
}


def load_settings() -> dict:
    values = DEFAULTS.copy()
    try:
        data = json.loads(SETTINGS_FILE.read_text(encoding="utf-8"))
    except (OSError, ValueError, UnicodeError):
        return values
    if not isinstance(data, dict):
        return values
    for side in ("left", "right"):
        number = data.get(f"{side}_cps")
        if type(number) is int and 1 <= number <= MAX_CPS:
            values[f"{side}_cps"] = number
        enabled = data.get(f"{side}_enabled")
        if type(enabled) is bool:
            values[f"{side}_enabled"] = enabled
    if isinstance(data.get("hotkey"), str) and data["hotkey"] in HOTKEYS:
        values["hotkey"] = data["hotkey"]
    if data.get("theme") in THEMES:
        values["theme"] = data["theme"]
    return values


def save_settings(values: dict) -> None:
    APP_DIR.mkdir(parents=True, exist_ok=True)
    temporary = SETTINGS_FILE.with_suffix(".tmp")
    temporary.write_text(json.dumps(values, ensure_ascii=False, indent=2), encoding="utf-8")
    os.replace(temporary, SETTINGS_FILE)
