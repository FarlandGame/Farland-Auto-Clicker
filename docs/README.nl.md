# Farland_autcliker

[English](../README.md) | [日本語](README.ja.md) | [فارسی](README.fa.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Español](README.es.md) | [Português (Brasil)](README.pt-BR.md) | [Italiano](README.it.md) | [Nederlands](README.nl.md) | [Polski](README.pl.md) | [Українська](README.uk.md) | [Türkçe](README.tr.md) | [Русский](README.ru.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [한국어](README.ko.md) | [हिन्दी](README.hi.md) | [Bahasa Indonesia](README.id.md)

Een autoclicker voor Windows waarbij elke fysieke klik een onafhankelijke reeks extra klikken van één seconde start, met afzonderlijke instellingen voor links en rechts en een Perzische interface.

**Gemaakt door Bardiya Alizadeh (Kabir), bekend als Farland_game.**

**[Download de Windows-ZIP](https://github.com/FarlandGame/Farland_autcliker/releases/latest/download/Farland_autcliker.zip)** · [Alle releases](https://github.com/FarlandGame/Farland_autcliker/releases)

![Interface van Farland_autcliker](../preview.png)

Farland_autcliker is een Windows-desktoptoepassing gemaakt door **Bardiya Alizadeh (Kabir), bekend als Farland_game**. Het kenmerkende onderdeel is hoe de automatisering begint: **elke fysieke muisklik start een eigen reeks extra klikken van één seconde**. De toepassing is bedoeld voor mensen die met hun eigen muisinvoer willen bepalen wanneer een reeks begint, terwijl ze de linker- en rechterknop onafhankelijk instellen. De toepassing combineert dit gedrag met een Perzische interface, aanpasbare bediening, opgeslagen voorkeuren en een direct uitvoerbaar Windows-programma.

## Hoe je klikken extra klikken worden

Schakel de autoclicker in en klik vervolgens met de linker- of rechtermuisknop. De oorspronkelijke fysieke klik wordt normaal doorgegeven en het programma plant extra klikken voor dezelfde knop gedurende de volgende seconde. Als links bijvoorbeeld is ingesteld op **20 CPS**, plant één fysieke linkermuisklik **20 extra linkermuisklikken**. Inclusief de fysieke klik vraagt deze handeling in totaal 21 klikken aan; de verwerking daarvan hangt af van de doeltoepassing.

Een tweede fysieke klik start een nieuwe reeks, ook als de eerste nog loopt. Twee van zulke linkermuisklikken plannen 40 extra klikken binnen hun overlappende tijdvensters van één seconde. De instelling beschrijft dus **elke afzonderlijke reeks**, geen algemene limiet voor alle overlappende activiteit. Zonder nieuwe fysieke klikken worden geen nieuwe reeksen gemaakt; al geplande reeksen gaan door totdat ze klaar zijn of totdat je de autoclicker stopt.

## Wat deze werkwijze anders maakt

Een bekende [werkwijze met herhaling tot je stopt](https://www.opautoclicker.com/) voert na activering een herhaalde reeks uit. Farland_autcliker onderscheidt zich door **reeksen die door fysieke klikken worden gestart**, met afzonderlijke instellingen voor elke kant.

| Handeling | Herhalen tot je stopt | Farland_autcliker |
| --- | --- | --- |
| Extra klikken starten | De herhaalreeks starten | Activeren en daarna fysiek klikken |
| Een nieuwe fysieke klik | Niet nodig om de herhaling te laten doorgaan | Start een eigen extra reeks |
| Een reeks beëindigen | De herhaalreeks stoppen | Elke reeks voltooit de planning van één seconde |

Deze vergelijking beschrijft twee werkwijzen; afzonderlijke autoclickers kunnen extra modi aanbieden. De gedocumenteerde sterke punten van Farland zijn de manier waarop reeksen starten en de onafhankelijke bediening.

## Links en rechts onafhankelijk instellen

Stel voor elke knop een andere snelheid in, van **1 tot 10.000 CPS**, en schakel elke kant afzonderlijk in. Je kunt bijvoorbeeld links 20 CPS en rechts 8 CPS instellen: een linkermuisklik start een reeks voor de linkerknop, terwijl een rechtermuisklik een onafhankelijke reeks voor de rechterknop start. Als je één kant uitschakelt, blijven de fysieke klikken daarvan normaal werken zonder nieuwe extra klikken te maken.

## Bediening die bij jouw instellingen past

Schakel de activering aan of uit met de hoofdknop in de interface of een gekozen algemene sneltoets: de middelste muisknop, een van de twee zijknoppen, F6–F9, Home, End of Insert. **F12** is een noodstop en sluit de toepassing af. Vier thema's — donker, licht, paars en blauw — laten je het uiterlijk kiezen. Kliksnelheden, ingeschakelde kanten, de sneltoets en het thema worden voor de volgende sessie opgeslagen. Ongeldige invoer voor de kliksnelheid wordt teruggezet naar de vorige geldige waarde.

## Herhaalde invoer zorgvuldig verwerken

De engine onderscheidt fysieke muisinvoer van door Windows geïnjecteerde klikken, zodat de zelf gegenereerde klikken geen nieuwe reeksen starten. Een scheduler beheert overlappende reeksen en verzendt klikken bij hoge snelheden in kleine groepen. **10.000 CPS is de instelbare bovengrens, geen garantie voor een gemeten snelheid**: de daadwerkelijke levering hangt af van de computer, de invoerverwerking van Windows en de doeltoepassing.

## Downloaden en verkennen

De openbare Windows-ZIP bevat het uitvoerbare bestand, de broncode, een voorbeeld van de interface en documentatie in het Engels, Japans en Perzisch. Pak het bestand uit en open `Farland-Auto-Clicker/dist/Farland Auto Clicker.exe`; voor het meegeleverde uitvoerbare bestand hoef je Python niet apart te installeren. De broncode is bedoeld voor Windows 10 of 11 en Python 3.10 of nieuwer en gebruikt Tkinter en de Windows-API. De repository bevat daarnaast zes tests voor de planning, overlappende kanten, annulering, sneltoetsen en filtering van geïnjecteerde invoer; deze gebruiken gesimuleerde klikken.

## Snel aan de slag

1. Download `Farland_autcliker.zip` en pak het bestand uit.
2. Open `Farland-Auto-Clicker/dist/Farland Auto Clicker.exe`. De verpakte toepassing vereist geen aparte Python-installatie.
3. Stel de klikken per seconde (CPS) voor links en rechts in en schakel de benodigde kanten in.
4. Druk op de middelste muisknop of de hoofdknop om de autoclicker te activeren.
5. Elke fysieke linker- of rechtermuisklik start extra klikken voor dezelfde knop gedurende de volgende seconde.
6. Druk op **F12** om alle geplande klikken te stoppen en af te sluiten.

## Bediening en instellingen

| Bediening | Actie |
| --- | --- |
| Hoofdknop / geselecteerde sneltoets | De autoclicker aan- of uitzetten |
| F12 | Noodstop en afsluiten |
| Enter / een CPS-veld verlaten | Een geldige kliksnelheid toepassen |

Een ongeldige kliksnelheid wordt teruggezet naar de vorige waarde. De instellingen worden opgeslagen in `%APPDATA%\Farland Auto Clicker\settings.json`.

## Uitvoeren vanuit de broncode

Vereist **Windows 10 of 11** en **Python 3.10 of nieuwer**, inclusief Tkinter. Er is geen pakket van derden nodig om de broncode uit te voeren.

```powershell
py main.py
```

## Het Windows-programma bouwen

Vanuit de projectmap:

```powershell
py -m pip install -r requirements.txt
py create_icon.py
py -m PyInstaller --noconfirm --clean "Farland Auto Clicker.spec"
```

De uitvoer is `dist/Farland Auto Clicker.exe`. Om een toepassing te bedienen die als administrator wordt uitgevoerd, start je de autoclicker met hetzelfde machtigingsniveau; Windows beperkt invoer naar toepassingen met hogere rechten.

## Projectstructuur

| Bestand | Doel |
| --- | --- |
| `main.py` | Tkinter-interface, bediening, thema's en links van de maker |
| `click_engine.py` | Windows-invoerhooks en klikplanner |
| `settings.py` | Gevalideerde instellingen met atomaire JSON-opslag |
| `create_icon.py`, `farland.ico` | Toepassingspictogram |
| `Farland Auto Clicker.spec` | PyInstaller-buildconfiguratie |
| `test_click_engine.py` | Tests voor het gedrag van scheduler en hooks |
| `docs/` | Japanse en Perzische documentatie |

De release-ZIP bevat het bestaande uitvoerbare Windows-bestand en de bronbestanden. Buildcaches en tijdelijke bestanden zijn uitgesloten.

## Tests

Op Windows:

```powershell
py -B -m unittest -v test_click_engine
```

Deze tests gebruiken een gesimuleerde klikverzender; ze genereren geen echte muisklikken.

## Maker

**Bardiya Alizadeh (Kabir) · Farland_game**

[GitHub-portfolio](https://github.com/FarlandGame)

### Kanalen en sociale links

| Platform | Kanalen / pagina's |
| --- | --- |
| GitHub | [FarlandGame](https://github.com/FarlandGame) |
| YouTube | [Farland_game](https://www.youtube.com/@Farland_game) · [Farland_animation](https://www.youtube.com/@Farland_animation) |
| Rubika-kanalen | [farland_gam](https://rubika.ir/farland_gam) · [Farland_animatio](https://rubika.ir/Farland_animatio) |
| Rubika-pagina's | [farland_game](https://rubika.ir/farland_game) · [Farland_animations](https://rubika.ir/Farland_animations) |
| Instagram | [farland_game](https://www.instagram.com/farland_game/) |
| Telegram-kanalen | [Farland_gam](https://t.me/Farland_gam) · [Farland_animatio](https://t.me/Farland_animatio) |
| Twitch | [farlandgame](https://twitch.tv/farlandgame) |
| Kick | [farlandgame](https://kick.com/farlandgame) |
| Aparat | [Farland_Game](https://aparat.com/Farland_Game) |
| SoundCloud | [Bardiya Kabir](https://soundcloud.com/bardiya-kabir-798008614) |

### Telegram-muziekbot

[Farland Music Bot](https://t.me/Farland_Music_bot) — Stuur de videolink van een nummer naar onze Telegram-bot om het nummer te vinden.

### Community en familie

- **THE APEX:** [YouTube](https://www.youtube.com/@THE_APEX_MC) · [Telegram](https://t.me/+-3uY7eIZArVjZDE0)
- **Manhunt:** [Telegram-groep](https://t.me/+DAq20XrkPyZhNjVk)
- **Het kanaal van mijn broer:** [ArmiyaFabix op YouTube](https://www.youtube.com/@ArmiyaFabix)

### Steun mijn werk

[Doneer via Reymit](https://reymit.ir/farland_game) ❤️
