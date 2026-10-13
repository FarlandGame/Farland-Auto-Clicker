# Farland_autcliker

[English](../README.md) | [日本語](README.ja.md) | [فارسی](README.fa.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Español](README.es.md) | [Português (Brasil)](README.pt-BR.md) | [Italiano](README.it.md) | [Nederlands](README.nl.md) | [Polski](README.pl.md) | [Українська](README.uk.md) | [Türkçe](README.tr.md) | [Русский](README.ru.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [한국어](README.ko.md) | [हिन्दी](README.hi.md) | [Bahasa Indonesia](README.id.md)

Ein Auto-Clicker für Windows, bei dem jeder physische Klick eine unabhängige, einsekündige Folge zusätzlicher Klicks auslöst, mit getrennten Einstellungen für links und rechts und einer persischen Benutzeroberfläche.

**Entwickelt von Bardiya Alizadeh (Kabir), bekannt als Farland_game.**

**[Windows-ZIP herunterladen](https://github.com/FarlandGame/Farland_autcliker/releases/latest/download/Farland_autcliker.zip)** · [Alle Veröffentlichungen](https://github.com/FarlandGame/Farland_autcliker/releases)

![Benutzeroberfläche von Farland_autcliker](../preview.png)

Farland_autcliker ist eine Windows-Desktopanwendung von **Bardiya Alizadeh (Kabir), bekannt als Farland_game**. Ihr besonderes Merkmal ist der Beginn der Automatisierung: **Jeder physische Mausklick startet seine eigene, einsekündige Folge zusätzlicher Klicks**. Sie richtet sich an Menschen, die mit ihren eigenen Mauseingaben bestimmen möchten, wann eine Klickfolge beginnt, und dabei die linke und rechte Taste unabhängig einstellen wollen. Die Anwendung verbindet dieses Verhalten mit einer persischen Benutzeroberfläche, anpassbaren Bedienelementen, gespeicherten Einstellungen und einer sofort ausführbaren Windows-Datei.

## Wie aus deinen Klicks zusätzliche Klicks werden

Aktiviere den Clicker und klicke dann mit der linken oder rechten Maustaste. Der ursprüngliche physische Klick wird normal weitergegeben; das Programm plant für dieselbe Taste zusätzliche Klicks innerhalb der folgenden Sekunde. Ist die linke Seite beispielsweise auf **20 CPS** eingestellt, plant ein physischer Linksklick **20 zusätzliche Linksklicks**. Zusammen mit dem physischen Klick werden für diese Interaktion insgesamt 21 Klicks angefordert; die tatsächliche Verarbeitung hängt von der Zielanwendung ab.

Ein zweiter physischer Klick startet eine weitere Folge, selbst wenn die erste noch läuft. Zwei solche Linksklicks planen 40 zusätzliche Klicks über ihre sich überschneidenden Einsekundenfenster. Die Einstellung beschreibt also **jede einzelne Klickfolge**, keine globale Obergrenze für alle überlappenden Vorgänge. Ohne neue physische Klicks entstehen keine neuen Folgen; bereits geplante Folgen laufen weiter, bis sie abgeschlossen sind oder du den Clicker stoppst.

## Was diesen Ablauf besonders macht

Ein vertrauter [Ablauf mit Wiederholung bis zum Stoppen](https://www.opautoclicker.com/) führt nach der Aktivierung eine wiederholte Klicksequenz aus. Farland_autcliker zeichnet sich durch **Klickfolgen aus, die von physischen Klicks ausgelöst werden**, mit getrennten Einstellungen für beide Seiten.

| Interaktion | Wiederholung bis zum Stoppen | Farland_autcliker |
| --- | --- | --- |
| Zusätzliche Klicks starten | Wiederholungssequenz starten | Aktivieren, dann physisch klicken |
| Neuer physischer Klick | Zum Fortsetzen der Wiederholung nicht erforderlich | Startet seine eigene zusätzliche Klickfolge |
| Sequenz beenden | Wiederholungssequenz stoppen | Jede Folge beendet ihren einsekündigen Zeitplan |

Dieser Vergleich beschreibt zwei Arbeitsweisen; einzelne Auto-Clicker können weitere Modi anbieten. Die dokumentierten Stärken von Farland sind sein Auslöseverhalten und die unabhängigen Einstellungen.

## Linke und rechte Taste unabhängig einstellen

Lege für jede Taste eine eigene Rate von **1 bis 10.000 CPS** fest und aktiviere jede Seite separat. Du kannst beispielsweise links 20 CPS und rechts 8 CPS einstellen: Ein Linksklick startet eine Folge für die linke Taste, während ein Rechtsklick eine unabhängige Folge für die rechte Taste startet. Wenn du eine Seite deaktivierst, funktionieren ihre physischen Klicks weiterhin normal, lösen aber keine neuen zusätzlichen Klicks aus.

## Bedienelemente passend zu deinem Setup

Schalte die Aktivierung mit der Hauptschaltfläche oder einem gewählten globalen Tastenkürzel um: mittlere Maustaste, eine der beiden seitlichen Maustasten, F6–F9, Home, End oder Insert. **F12** dient als Notstopp und beendet die Anwendung. Vier Designs — dunkel, hell, violett und blau — ermöglichen die Wahl des Erscheinungsbilds. Klickraten, aktivierte Seiten, Tastenkürzel und Design werden für die nächste Sitzung gespeichert. Ungültige Eingaben für die Klickrate werden auf den letzten gültigen Wert zurückgesetzt.

## Wiederholte Eingaben gezielt verarbeiten

Die Engine unterscheidet physische Mauseingaben von durch Windows injizierten Klicks, damit die selbst erzeugten Klicks keine neuen Folgen auslösen. Ein Scheduler verwaltet überlappende Folgen und sendet Klicks bei hohen Raten in kleinen Paketen. **10.000 CPS ist die einstellbare Obergrenze, keine Garantie für eine gemessene Geschwindigkeit**: Die tatsächliche Übermittlung hängt vom Computer, der Windows-Eingabeverarbeitung und der Zielanwendung ab.

## Herunterladen und kennenlernen

Die öffentliche Windows-ZIP enthält die ausführbare Datei, den Quellcode, eine Vorschau der Benutzeroberfläche sowie englische, japanische und persische Dokumentation. Entpacke sie und öffne `Farland-Auto-Clicker/dist/Farland Auto Clicker.exe`; die mitgelieferte ausführbare Datei benötigt keine separate Python-Installation. Der Quellcode richtet sich an Windows 10 oder 11 und Python 3.10 oder höher und nutzt Tkinter sowie die Windows-API. Das Repository enthält außerdem sechs Tests für Zeitplanung, überlappende Seiten, Abbruch, Tastenkürzel und das Filtern injizierter Eingaben; sie verwenden simulierte Klicks.

## Schnellstart

1. Lade `Farland_autcliker.zip` herunter und entpacke die Datei.
2. Öffne `Farland-Auto-Clicker/dist/Farland Auto Clicker.exe`. Die gebündelte Anwendung benötigt keine separate Python-Installation.
3. Lege die Klicks pro Sekunde (CPS) für links und rechts fest und aktiviere die gewünschten Seiten.
4. Drücke die mittlere Maustaste oder die Hauptschaltfläche, um den Clicker zu aktivieren.
5. Jeder physische Links- oder Rechtsklick startet für dieselbe Taste zusätzliche Klicks innerhalb der folgenden Sekunde.
6. Drücke **F12**, um alle ausstehenden Klicks zu stoppen und die Anwendung zu beenden.

## Bedienung und Einstellungen

| Bedienelement | Aktion |
| --- | --- |
| Hauptschaltfläche / gewähltes Tastenkürzel | Auto-Clicker ein- oder ausschalten |
| F12 | Notstopp und Beenden |
| Enter / Verlassen eines CPS-Felds | Gültige Klickrate übernehmen |

Eine ungültige Klickrate wird auf ihren vorherigen Wert zurückgesetzt. Die Einstellungen liegen in `%APPDATA%\Farland Auto Clicker\settings.json`.

## Aus dem Quellcode starten

Erforderlich sind **Windows 10 oder 11** und **Python 3.10 oder höher**, einschließlich Tkinter. Zum Ausführen des Quellcodes wird kein Paket eines Drittanbieters benötigt.

```powershell
py main.py
```

## Ausführbare Windows-Datei erstellen

Im Projektverzeichnis:

```powershell
py -m pip install -r requirements.txt
py create_icon.py
py -m PyInstaller --noconfirm --clean "Farland Auto Clicker.spec"
```

Das Ergebnis ist `dist/Farland Auto Clicker.exe`. Um mit einer Anwendung zu interagieren, die als Administrator läuft, starte den Clicker mit denselben Berechtigungen; Windows beschränkt Eingaben an Anwendungen mit höheren Berechtigungen.

## Projektstruktur

| Datei | Zweck |
| --- | --- |
| `main.py` | Tkinter-Oberfläche, Bedienelemente, Designs und Links zum Entwickler |
| `click_engine.py` | Windows-Eingabe-Hooks und Klick-Scheduler |
| `settings.py` | Validierte Einstellungen mit atomaren JSON-Speicherungen |
| `create_icon.py`, `farland.ico` | Anwendungssymbol |
| `Farland Auto Clicker.spec` | PyInstaller-Buildkonfiguration |
| `test_click_engine.py` | Tests für Scheduler- und Hook-Verhalten |
| `docs/` | Japanische und persische Dokumentation |

Die Release-ZIP enthält die vorhandene ausführbare Windows-Datei und die Quelldateien. Build-Caches und temporäre Dateien sind ausgeschlossen.

## Tests

Unter Windows:

```powershell
py -B -m unittest -v test_click_engine
```

Diese Tests verwenden einen simulierten Klicksender; sie erzeugen keine echten Mausklicks.

## Entwickler

**Bardiya Alizadeh (Kabir) · Farland_game**

[GitHub-Portfolio](https://github.com/FarlandGame)

### Kanäle und soziale Links

| Plattform | Kanäle / Seiten |
| --- | --- |
| GitHub | [FarlandGame](https://github.com/FarlandGame) |
| YouTube | [Farland_game](https://www.youtube.com/@Farland_game) · [Farland_animation](https://www.youtube.com/@Farland_animation) |
| Rubika-Kanäle | [farland_gam](https://rubika.ir/farland_gam) · [Farland_animatio](https://rubika.ir/Farland_animatio) |
| Rubika-Seiten | [farland_game](https://rubika.ir/farland_game) · [Farland_animations](https://rubika.ir/Farland_animations) |
| Instagram | [farland_game](https://www.instagram.com/farland_game/) |
| Telegram-Kanäle | [Farland_gam](https://t.me/Farland_gam) · [Farland_animatio](https://t.me/Farland_animatio) |
| Twitch | [farlandgame](https://twitch.tv/farlandgame) |
| Kick | [farlandgame](https://kick.com/farlandgame) |
| Aparat | [Farland_Game](https://aparat.com/Farland_Game) |
| SoundCloud | [Bardiya Kabir](https://soundcloud.com/bardiya-kabir-798008614) |

### Telegram-Musikbot

[Farland Music Bot](https://t.me/Farland_Music_bot) — Sende unserem Telegram-Bot den Videolink eines Lieds, um den Titel zu finden.

### Community und Familie

- **THE APEX:** [YouTube](https://www.youtube.com/@THE_APEX_MC) · [Telegram](https://t.me/+-3uY7eIZArVjZDE0)
- **Manhunt:** [Telegram-Gruppe](https://t.me/+DAq20XrkPyZhNjVk)
- **Kanal meines Bruders:** [ArmiyaFabix auf YouTube](https://www.youtube.com/@ArmiyaFabix)

### Meine Arbeit unterstützen

[Über Reymit spenden](https://reymit.ir/farland_game) ❤️
