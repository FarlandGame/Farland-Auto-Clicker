# Farland Auto Clicker

[English](README.md) | [日本語](docs/README.ja.md) | [فارسی](docs/README.fa.md)

A Windows auto clicker with a Persian interface, independent left/right click settings, customizable hotkeys, and an emergency stop.

**Created by Bardiya Alizadeh (Kabir), known as Farland_game.**

**[Download the Windows ZIP](https://github.com/FarlandGame/Farland-Auto-Clicker/releases/latest/download/Farland-Auto-Clicker.zip)** · [All releases](https://github.com/FarlandGame/Farland-Auto-Clicker/releases)

![Farland Auto Clicker interface](preview.png)

## Quick start

1. Download and extract `Farland-Auto-Clicker.zip`.
2. Open `Farland-Auto-Clicker/dist/Farland Auto Clicker.exe`. The packaged application does not require a separate Python installation.
3. Set the left and right clicks per second (CPS) and enable the sides you need.
4. Press the middle mouse button or the main toggle button to activate the clicker.
5. Each physical left/right click starts a burst of additional clicks for that same button over the following second.
6. Press **F12** to stop all pending clicks and exit.

## Features

- Independent left/right click rates, configurable from **1 to 10,000 CPS**.
- Enable or disable each mouse button separately.
- Configurable toggle: middle mouse, side mouse buttons, F6–F9, Home, End, or Insert.
- Four interface themes: dark, light, purple, and blue.
- Settings saved between sessions.
- A scheduler supports overlapping click bursts and batches high click rates.
- Windows-injected clicks are filtered to prevent them from starting additional bursts.

The physical click is still delivered normally. Each burst schedules the configured number of **additional** clicks. Several physical clicks can start overlapping bursts. The 10,000 CPS setting is the configurable ceiling; actual delivery depends on the computer, Windows input processing, and the target application's limits.

## Controls and settings

| Control | Action |
| --- | --- |
| Main button / selected hotkey | Toggle the auto clicker |
| F12 | Emergency stop and exit |
| Enter / leaving a CPS field | Apply a valid click-rate value |

Invalid click-rate input reverts to its previous value. Settings are stored in `%APPDATA%\Farland Auto Clicker\settings.json`.

## Run from source

Requires **Windows 10 or 11** and **Python 3.10 or later**, including Tkinter. No third-party package is needed to run the source.

```powershell
py main.py
```

## Build the Windows executable

From the project directory:

```powershell
py -m pip install -r requirements.txt
py create_icon.py
py -m PyInstaller --noconfirm --clean "Farland Auto Clicker.spec"
```

The output is `dist/Farland Auto Clicker.exe`. To interact with an application running as administrator, run the clicker at the same privilege level; Windows restricts input to higher-privilege applications.

## Project structure

| File | Purpose |
| --- | --- |
| `main.py` | Tkinter interface, controls, themes, and creator links |
| `click_engine.py` | Windows input hooks and click scheduler |
| `settings.py` | Validated settings with atomic JSON saves |
| `create_icon.py`, `farland.ico` | Application icon |
| `Farland Auto Clicker.spec` | PyInstaller build configuration |
| `test_click_engine.py` | Scheduler and hook behavior tests |
| `docs/` | Japanese and Persian documentation |

The release ZIP includes the existing Windows executable and the source files. Build caches and temporary files are excluded.

## Tests

On Windows:

```powershell
py -B -m unittest -v test_click_engine
```

These tests use a simulated click sender; they do not generate real mouse clicks.

## Creator

**Bardiya Alizadeh (Kabir) · Farland_game**

[GitHub portfolio](https://github.com/FarlandGame)

### Channels and social links

| Platform | Channels / pages |
| --- | --- |
| YouTube | [Farland_game](https://www.youtube.com/@Farland_game) · [Farland_animation](https://www.youtube.com/@Farland_animation) |
| Rubika channels | [farland_gam](https://rubika.ir/farland_gam) · [Farland_animatio](https://rubika.ir/Farland_animatio) |
| Rubika pages | [farland_game](https://rubika.ir/farland_game) · [Farland_animations](https://rubika.ir/Farland_animations) |
| Instagram | [farland_game](https://www.instagram.com/farland_game/) |
| Telegram channels | [Farland_gam](https://t.me/Farland_gam) · [Farland_animatio](https://t.me/Farland_animatio) |
| Twitch | [farlandgame](https://twitch.tv/farlandgame) |
| Kick | [farlandgame](https://kick.com/farlandgame) |
| Aparat | [Farland_Game](https://aparat.com/Farland_Game) |
| SoundCloud | [Bardiya Kabir](https://soundcloud.com/bardiya-kabir-798008614) |

### Telegram music bot

[Farland Music Bot](https://t.me/Farland_Music_bot) — Send a song's video link to our Telegram bot to find the track.

### Community and family

- **THE APEX:** [YouTube](https://www.youtube.com/@THE_APEX_MC) · [Telegram](https://t.me/+-3uY7eIZArVjZDE0)
- **Manhunt:** [Telegram group](https://t.me/+DAq20XrkPyZhNjVk)
- **My brother's channel:** [ArmiyaFabix on YouTube](https://www.youtube.com/@ArmiyaFabix)

### Support my work

[Donate via Reymit](https://reymit.ir/farland_game) ❤️
