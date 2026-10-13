# Farland_autcliker

[English](../README.md) | [日本語](README.ja.md) | [فارسی](README.fa.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Español](README.es.md) | [Português (Brasil)](README.pt-BR.md) | [Italiano](README.it.md) | [Nederlands](README.nl.md) | [Polski](README.pl.md) | [Українська](README.uk.md) | [Türkçe](README.tr.md) | [Русский](README.ru.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [한국어](README.ko.md) | [हिन्दी](README.hi.md) | [Bahasa Indonesia](README.id.md)

Autoclicker dla systemu Windows, w którym każde fizyczne kliknięcie rozpoczyna niezależną, jednosekundową serię dodatkowych kliknięć, z osobnymi ustawieniami lewego i prawego przycisku oraz interfejsem w języku perskim.

**Autor: Bardiya Alizadeh (Kabir), znany jako Farland_game.**

**[Pobierz plik ZIP dla Windows](https://github.com/FarlandGame/Farland_autcliker/releases/latest/download/Farland_autcliker.zip)** · [Wszystkie wydania](https://github.com/FarlandGame/Farland_autcliker/releases)

![Interfejs Farland_autcliker](../preview.png)

Farland_autcliker to aplikacja na komputery z systemem Windows, którą stworzył **Bardiya Alizadeh (Kabir), znany jako Farland_game**. Jej wyróżnikiem jest sposób rozpoczęcia automatyzacji: **każde fizyczne kliknięcie myszy uruchamia własną, jednosekundową serię dodatkowych kliknięć**. Jest przeznaczona dla osób, które chcą decydować o początku serii za pomocą własnych kliknięć, jednocześnie niezależnie ustawiając lewy i prawy przycisk. Aplikacja łączy takie działanie z perskim interfejsem, konfigurowalnym sterowaniem, zapisanymi preferencjami oraz gotowym do uruchomienia plikiem wykonywalnym dla Windows.

## Jak Twoje kliknięcia zamieniają się w dodatkowe kliknięcia

Włącz autoclicker, a następnie kliknij lewym lub prawym przyciskiem myszy. Oryginalne fizyczne kliknięcie jest przekazywane normalnie, a program planuje dodatkowe kliknięcia tego samego przycisku na kolejną sekundę. Na przykład przy ustawieniu lewego przycisku na **20 CPS** jedno fizyczne kliknięcie lewym przyciskiem planuje **20 dodatkowych kliknięć lewym przyciskiem**. Wraz z fizycznym kliknięciem ta czynność żąda łącznie 21 kliknięć, z zastrzeżeniem sposobu przetwarzania wejścia przez aplikację docelową.

Drugie fizyczne kliknięcie rozpoczyna kolejną serię, nawet jeśli pierwsza nadal trwa. Dwa takie kliknięcia lewym przyciskiem planują 40 dodatkowych kliknięć w ich nakładających się jednosekundowych przedziałach. Ustawienie opisuje więc **każdą pojedynczą serię**, a nie globalny limit wszystkich nakładających się działań. Gdy nie pojawiają się nowe fizyczne kliknięcia, nie powstają nowe serie; już zaplanowane trwają do zakończenia lub do zatrzymania autoclickera.

## Co wyróżnia ten sposób działania

Typowy [tryb powtarzania aż do zatrzymania](https://www.opautoclicker.com/) wykonuje powtarzaną sekwencję po aktywacji. Farland_autcliker wyróżniają **serie wyzwalane fizycznymi kliknięciami**, z oddzielnymi ustawieniami dla każdej strony.

| Czynność | Powtarzanie aż do zatrzymania | Farland_autcliker |
| --- | --- | --- |
| Rozpoczęcie dodatkowych kliknięć | Uruchomienie sekwencji powtarzania | Aktywacja, a następnie fizyczne kliknięcie |
| Nowe fizyczne kliknięcie | Nie jest potrzebne do kontynuowania powtarzania | Rozpoczyna własną dodatkową serię |
| Zakończenie sekwencji | Zatrzymanie sekwencji powtarzania | Każda seria kończy swój jednosekundowy harmonogram |

To porównanie opisuje dwa sposoby działania; poszczególne autoclickery mogą oferować dodatkowe tryby. Udokumentowane zalety Farland to sposób wyzwalania oraz niezależne sterowanie.

## Niezależne ustawienia lewego i prawego przycisku

Ustaw osobną częstotliwość dla każdego przycisku, od **1 do 10 000 CPS**, i włączaj każdą stronę oddzielnie. Możesz na przykład ustawić 20 CPS dla lewego przycisku i 8 CPS dla prawego: kliknięcie lewym rozpoczyna serię dla lewego przycisku, a kliknięcie prawym — niezależną serię dla prawego. Wyłączenie jednej strony pozwala jej fizycznym kliknięciom nadal działać normalnie, bez tworzenia nowych dodatkowych kliknięć.

## Sterowanie dopasowane do Twojej konfiguracji

Włączaj i wyłączaj autoclicker głównym przyciskiem interfejsu lub wybranym globalnym skrótem: środkowym przyciskiem myszy, jednym z dwóch przycisków bocznych, F6–F9, Home, End albo Insert. **F12** służy do awaryjnego zatrzymania i zamknięcia aplikacji. Cztery motywy — ciemny, jasny, fioletowy i niebieski — pozwalają wybrać wygląd. Częstotliwości kliknięć, włączone strony, skrót i motyw są zapisywane na następną sesję. Nieprawidłowe wartości częstotliwości wracają do ostatniej poprawnej wartości.

## Przemyślane przetwarzanie powtarzanych wejść

Silnik rozróżnia fizyczne wejścia myszy od kliknięć wstrzykniętych przez Windows, aby jego własne wygenerowane kliknięcia nie rozpoczynały nowych serii. Harmonogram zarządza nakładającymi się seriami i wysyła kliknięcia o wysokiej częstotliwości w małych partiach. **10 000 CPS to konfigurowalny limit, a nie gwarancja zmierzonej prędkości**: faktyczne dostarczanie kliknięć zależy od komputera, obsługi wejścia w Windows oraz aplikacji docelowej.

## Pobieranie i poznawanie programu

Publiczny plik ZIP dla Windows zawiera plik wykonywalny, kod źródłowy, podgląd interfejsu oraz dokumentację po angielsku, japońsku i persku. Rozpakuj go i otwórz `Farland-Auto-Clicker/dist/Farland Auto Clicker.exe`; dołączony plik wykonywalny nie wymaga osobnej instalacji Pythona. Kod źródłowy jest przeznaczony dla Windows 10 lub 11 oraz Pythona 3.10 lub nowszego i korzysta z Tkinter oraz API Windows. Repozytorium zawiera też sześć testów harmonogramu, nakładania się stron, anulowania, skrótów i filtrowania wstrzykniętych wejść; korzystają one z symulowanych kliknięć.

## Szybki start

1. Pobierz i rozpakuj `Farland_autcliker.zip`.
2. Otwórz `Farland-Auto-Clicker/dist/Farland Auto Clicker.exe`. Spakowana aplikacja nie wymaga osobnej instalacji Pythona.
3. Ustaw liczbę kliknięć na sekundę (CPS) dla lewej i prawej strony oraz włącz potrzebne strony.
4. Naciśnij środkowy przycisk myszy lub główny przycisk, aby aktywować autoclicker.
5. Każde fizyczne kliknięcie lewym lub prawym przyciskiem rozpoczyna serię dodatkowych kliknięć tego samego przycisku w ciągu następnej sekundy.
6. Naciśnij **F12**, aby zatrzymać wszystkie oczekujące kliknięcia i wyjść.

## Sterowanie i ustawienia

| Element sterujący | Działanie |
| --- | --- |
| Główny przycisk / wybrany skrót | Włączanie lub wyłączanie autoclickera |
| F12 | Awaryjne zatrzymanie i wyjście |
| Enter / opuszczenie pola CPS | Zastosowanie poprawnej częstotliwości kliknięć |

Nieprawidłowa częstotliwość kliknięć wraca do poprzedniej wartości. Ustawienia są przechowywane w `%APPDATA%\Farland Auto Clicker\settings.json`.

## Uruchamianie z kodu źródłowego

Wymaga **Windows 10 lub 11** oraz **Pythona 3.10 lub nowszego**, wraz z Tkinter. Uruchomienie kodu źródłowego nie wymaga pakietów innych firm.

```powershell
py main.py
```

## Budowanie pliku wykonywalnego dla Windows

Z katalogu projektu:

```powershell
py -m pip install -r requirements.txt
py create_icon.py
py -m PyInstaller --noconfirm --clean "Farland Auto Clicker.spec"
```

Wynik to `dist/Farland Auto Clicker.exe`. Aby działać na aplikacji uruchomionej jako administrator, uruchom autoclicker z tym samym poziomem uprawnień; Windows ogranicza wejście do aplikacji o wyższych uprawnieniach.

## Struktura projektu

| Plik | Przeznaczenie |
| --- | --- |
| `main.py` | Interfejs Tkinter, sterowanie, motywy i linki autora |
| `click_engine.py` | Hooki wejścia Windows i harmonogram kliknięć |
| `settings.py` | Walidowane ustawienia z atomowym zapisem JSON |
| `create_icon.py`, `farland.ico` | Ikona aplikacji |
| `Farland Auto Clicker.spec` | Konfiguracja kompilacji PyInstaller |
| `test_click_engine.py` | Testy zachowania harmonogramu i hooków |
| `docs/` | Dokumentacja w języku japońskim i perskim |

Plik ZIP wydania zawiera istniejący plik wykonywalny dla Windows oraz pliki źródłowe. Pamięci podręczne kompilacji i pliki tymczasowe są wykluczone.

## Testy

W systemie Windows:

```powershell
py -B -m unittest -v test_click_engine
```

Testy te korzystają z symulowanego nadajnika kliknięć; nie generują prawdziwych kliknięć myszy.

## Autor

**Bardiya Alizadeh (Kabir) · Farland_game**

[Portfolio na GitHubie](https://github.com/FarlandGame)

### Kanały i linki społecznościowe

| Platforma | Kanały / strony |
| --- | --- |
| GitHub | [FarlandGame](https://github.com/FarlandGame) |
| YouTube | [Farland_game](https://www.youtube.com/@Farland_game) · [Farland_animation](https://www.youtube.com/@Farland_animation) |
| Kanały Rubika | [farland_gam](https://rubika.ir/farland_gam) · [Farland_animatio](https://rubika.ir/Farland_animatio) |
| Strony Rubika | [farland_game](https://rubika.ir/farland_game) · [Farland_animations](https://rubika.ir/Farland_animations) |
| Instagram | [farland_game](https://www.instagram.com/farland_game/) |
| Kanały Telegram | [Farland_gam](https://t.me/Farland_gam) · [Farland_animatio](https://t.me/Farland_animatio) |
| Twitch | [farlandgame](https://twitch.tv/farlandgame) |
| Kick | [farlandgame](https://kick.com/farlandgame) |
| Aparat | [Farland_Game](https://aparat.com/Farland_Game) |
| SoundCloud | [Bardiya Kabir](https://soundcloud.com/bardiya-kabir-798008614) |

### Muzyczny bot Telegram

[Farland Music Bot](https://t.me/Farland_Music_bot) — Wyślij link do filmu z piosenką naszemu botowi na Telegramie, aby znaleźć utwór.

### Społeczność i rodzina

- **THE APEX:** [YouTube](https://www.youtube.com/@THE_APEX_MC) · [Telegram](https://t.me/+-3uY7eIZArVjZDE0)
- **Manhunt:** [Grupa Telegram](https://t.me/+DAq20XrkPyZhNjVk)
- **Kanał mojego brata:** [ArmiyaFabix na YouTube](https://www.youtube.com/@ArmiyaFabix)

### Wesprzyj moją pracę

[Przekaż darowiznę przez Reymit](https://reymit.ir/farland_game) ❤️
