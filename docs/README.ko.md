# Farland_autcliker

[English](../README.md) | [日本語](README.ja.md) | [فارسی](README.fa.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Español](README.es.md) | [Português (Brasil)](README.pt-BR.md) | [Italiano](README.it.md) | [Nederlands](README.nl.md) | [Polski](README.pl.md) | [Українська](README.uk.md) | [Türkçe](README.tr.md) | [Русский](README.ru.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [한국어](README.ko.md) | [हिन्दी](README.hi.md) | [Bahasa Indonesia](README.id.md)

실제로 마우스를 클릭할 때마다 서로 독립적인 1초짜리 추가 클릭 묶음을 시작하는 Windows 자동 클릭 프로그램입니다. 왼쪽과 오른쪽 버튼을 따로 제어할 수 있으며, 프로그램 인터페이스는 페르시아어입니다.

**Farland_game이라는 이름으로 활동하는 Bardiya Alizadeh(Kabir)가 만들었습니다.**

**[Windows ZIP 다운로드](https://github.com/FarlandGame/Farland_autcliker/releases/latest/download/Farland_autcliker.zip)** · [모든 릴리스](https://github.com/FarlandGame/Farland_autcliker/releases)

![Farland_autcliker 인터페이스](../preview.png)

Farland_autcliker는 **Farland_game이라는 이름으로 활동하는 Bardiya Alizadeh(Kabir)**가 만든 Windows 데스크톱 애플리케이션입니다. 가장 큰 특징은 자동 클릭이 시작되는 방식입니다. **실제 마우스 클릭 한 번마다 별도의 1초짜리 추가 클릭 묶음이 시작됩니다.** 왼쪽과 오른쪽 버튼을 독립적으로 제어하면서 자신의 마우스 입력으로 추가 클릭의 시작 시점을 정하고 싶은 사용자를 위해 설계되었습니다. 이러한 동작에 페르시아어 인터페이스, 사용자 지정 제어, 설정 저장, 바로 실행할 수 있는 Windows 실행 파일을 결합했습니다.

## 실제 클릭이 추가 클릭으로 이어지는 방식

클릭 프로그램을 활성화한 뒤 마우스 왼쪽 또는 오른쪽 버튼을 클릭하세요. 원래의 실제 클릭은 정상적으로 전달되고, 프로그램은 같은 버튼의 추가 클릭을 이후 1초 동안 실행하도록 예약합니다. 예를 들어 왼쪽을 **20 CPS**로 설정하면 실제 왼쪽 클릭 한 번이 **추가 왼쪽 클릭 20회**를 예약합니다. 실제 클릭까지 포함하면 총 21회의 클릭을 요청하는 셈이며, 결과는 대상 애플리케이션의 입력 처리 방식에 따라 달라집니다.

첫 번째 묶음이 아직 실행 중이어도 두 번째 실제 클릭은 새로운 묶음을 시작합니다. 이런 방식으로 왼쪽 버튼을 두 번 실제로 클릭하면 서로 겹치는 1초 구간에 총 40회의 추가 클릭이 예약됩니다. 즉, 이 설정은 겹쳐 실행되는 모든 동작의 전체 상한이 아니라 **각 개별 클릭 묶음**의 속도를 나타냅니다. 새로운 실제 클릭이 없으면 새 묶음도 만들어지지 않습니다. 이미 예약된 묶음은 완료되거나 클릭 프로그램을 중지할 때까지 계속 실행됩니다.

## 이 사용 방식의 차이점

일반적인 [중지할 때까지 반복하는 방식](https://www.opautoclicker.com/)은 활성화 후 클릭을 반복합니다. Farland_autcliker의 차별점은 버튼별로 설정할 수 있는 **실제 클릭으로 시작되는 짧은 클릭 묶음**입니다.

| 동작 | 중지할 때까지 반복하는 방식 | Farland_autcliker |
| --- | --- | --- |
| 추가 클릭 시작 | 반복 클릭을 시작 | 활성화한 뒤 실제로 클릭 |
| 새로운 실제 클릭 | 반복을 유지하기 위해 필요하지 않음 | 별도의 추가 클릭 묶음을 시작 |
| 클릭 순서 종료 | 반복 클릭을 중지 | 각 묶음이 자신의 1초 일정을 완료 |

이 표는 두 가지 사용 방식을 비교합니다. 다른 자동 클릭 프로그램은 추가 모드를 제공할 수도 있습니다. Farland의 문서화된 강점은 클릭을 시작하는 방식과 독립적인 제어입니다.

## 왼쪽과 오른쪽 버튼의 독립적인 제어

각 버튼의 속도를 **1~10,000 CPS** 범위에서 따로 설정하고, 원하는 쪽만 개별적으로 활성화할 수 있습니다. 예를 들어 왼쪽을 20 CPS, 오른쪽을 8 CPS로 설정하면 왼쪽 클릭은 왼쪽 버튼 묶음을, 오른쪽 클릭은 독립적인 오른쪽 버튼 묶음을 시작합니다. 한쪽을 비활성화해도 해당 버튼의 실제 클릭은 정상적으로 작동하지만 새로운 추가 클릭은 생성되지 않습니다.

## 사용 환경에 맞는 조작

메인 인터페이스 버튼이나 선택한 전역 단축키로 활성화 상태를 전환할 수 있습니다. 선택 가능한 키는 마우스 가운데 버튼, 두 측면 버튼 중 하나, F6~F9, Home, End, Insert입니다. **F12**는 긴급 중지와 프로그램 종료를 수행합니다. 어두운 테마, 밝은 테마, 보라색, 파란색의 네 가지 테마 중에서 선택할 수 있습니다. 클릭 속도, 활성화된 버튼, 단축키, 테마는 다음 실행을 위해 저장됩니다. 올바르지 않은 클릭 속도를 입력하면 이전의 유효한 값으로 되돌아갑니다.

## 반복 입력의 신중한 처리

엔진은 실제 마우스 입력과 Windows에서 주입한 클릭을 구분하므로, 프로그램이 생성한 클릭이 새로운 묶음을 시작하지 않습니다. 스케줄러가 겹치는 묶음을 관리하고 빠른 클릭을 작은 묶음으로 나누어 전송합니다. **10,000 CPS는 설정 가능한 최대값이며, 측정된 속도를 보장하는 수치가 아닙니다.** 실제 전달 속도는 컴퓨터, Windows 입력 처리, 대상 애플리케이션에 따라 달라집니다.

## 다운로드하고 살펴보기

공개 Windows ZIP에는 실행 파일, 소스 코드, 인터페이스 미리보기, 영어·일본어·페르시아어 문서가 포함되어 있습니다. 압축을 풀고 `Farland-Auto-Clicker/dist/Farland Auto Clicker.exe`를 여세요. 패키지에 포함된 실행 파일에는 별도의 Python 설치가 필요하지 않습니다. 소스 코드는 Windows 10 또는 11과 Python 3.10 이상을 대상으로 하며 Tkinter와 Windows API를 사용합니다. 저장소에는 일정 예약, 양쪽 버튼의 겹치는 묶음, 취소, 단축키, 주입된 입력 필터링을 위한 여섯 가지 테스트도 있습니다. 테스트에는 모의 클릭이 사용됩니다.

## 빠른 시작

1. `Farland_autcliker.zip`을 다운로드하고 압축을 푸세요.
2. `Farland-Auto-Clicker/dist/Farland Auto Clicker.exe`를 여세요. 패키지에 포함된 애플리케이션에는 별도의 Python 설치가 필요하지 않습니다.
3. 왼쪽과 오른쪽 버튼의 초당 클릭 수(CPS)를 설정하고 필요한 쪽을 활성화하세요.
4. 마우스 가운데 버튼이나 메인 전환 버튼을 눌러 클릭 프로그램을 활성화하세요.
5. 실제 왼쪽 또는 오른쪽 클릭 한 번마다 같은 버튼의 추가 클릭 묶음이 이후 1초 동안 실행됩니다.
6. **F12**를 누르면 대기 중인 모든 클릭을 중지하고 종료합니다.

## 조작 및 설정

| 조작 | 동작 |
| --- | --- |
| 메인 버튼 / 선택한 단축키 | 자동 클릭 프로그램의 활성화 상태 전환 |
| F12 | 긴급 중지 및 종료 |
| Enter / CPS 입력란에서 이동 | 유효한 클릭 속도 적용 |

유효하지 않은 속도를 입력하면 이전 값으로 되돌아갑니다. 설정은 `%APPDATA%\Farland Auto Clicker\settings.json`에 저장됩니다.

## 소스 코드로 실행

Tkinter를 포함한 **Python 3.10 이상**과 **Windows 10 또는 11**이 필요합니다. 소스 코드 실행에는 타사 패키지가 필요하지 않습니다.

```powershell
py main.py
```

## Windows 실행 파일 빌드

프로젝트 폴더에서 실행하세요.

```powershell
py -m pip install -r requirements.txt
py create_icon.py
py -m PyInstaller --noconfirm --clean "Farland Auto Clicker.spec"
```

결과 파일은 `dist/Farland Auto Clicker.exe`입니다. 관리자 권한으로 실행 중인 애플리케이션을 조작하려면 클릭 프로그램도 같은 권한으로 실행하세요. Windows는 더 높은 권한을 가진 애플리케이션으로 보내는 입력을 제한합니다.

## 프로젝트 구조

| 파일 | 역할 |
| --- | --- |
| `main.py` | Tkinter 인터페이스, 조작, 테마, 제작자 링크 |
| `click_engine.py` | Windows 입력 후크와 클릭 스케줄러 |
| `settings.py` | 설정 검증 및 원자적 JSON 저장 |
| `create_icon.py`, `farland.ico` | 애플리케이션 아이콘 |
| `Farland Auto Clicker.spec` | PyInstaller 빌드 설정 |
| `test_click_engine.py` | 스케줄러 및 후크 동작 테스트 |
| `docs/` | 일본어 및 페르시아어 문서 |

릴리스 ZIP에는 기존 Windows 실행 파일과 소스 파일이 포함됩니다. 빌드 캐시와 임시 파일은 제외됩니다.

## 테스트

Windows에서 실행하세요.

```powershell
py -B -m unittest -v test_click_engine
```

이 테스트는 모의 클릭 전송기를 사용하며 실제 마우스 클릭을 생성하지 않습니다.

## 제작자

**Bardiya Alizadeh(Kabir) · Farland_game**

[GitHub 포트폴리오](https://github.com/FarlandGame)

### 채널 및 소셜 링크

| 플랫폼 | 채널 / 페이지 |
| --- | --- |
| GitHub | [FarlandGame](https://github.com/FarlandGame) |
| YouTube | [Farland_game](https://www.youtube.com/@Farland_game) · [Farland_animation](https://www.youtube.com/@Farland_animation) |
| Rubika 채널 | [farland_gam](https://rubika.ir/farland_gam) · [Farland_animatio](https://rubika.ir/Farland_animatio) |
| Rubika 페이지 | [farland_game](https://rubika.ir/farland_game) · [Farland_animations](https://rubika.ir/Farland_animations) |
| Instagram | [farland_game](https://www.instagram.com/farland_game/) |
| Telegram 채널 | [Farland_gam](https://t.me/Farland_gam) · [Farland_animatio](https://t.me/Farland_animatio) |
| Twitch | [farlandgame](https://twitch.tv/farlandgame) |
| Kick | [farlandgame](https://kick.com/farlandgame) |
| Aparat | [Farland_Game](https://aparat.com/Farland_Game) |
| SoundCloud | [Bardiya Kabir](https://soundcloud.com/bardiya-kabir-798008614) |

### Telegram 음악 봇

[Farland Music Bot](https://t.me/Farland_Music_bot) — 노래를 찾으려면 해당 노래의 영상 링크를 저희 Telegram 봇으로 보내세요.

### 커뮤니티와 가족

- **THE APEX:** [YouTube](https://www.youtube.com/@THE_APEX_MC) · [Telegram](https://t.me/+-3uY7eIZArVjZDE0)
- **Manhunt:** [Telegram 그룹](https://t.me/+DAq20XrkPyZhNjVk)
- **제 형제의 채널:** [YouTube의 ArmiyaFabix](https://www.youtube.com/@ArmiyaFabix)

### 제 활동 후원하기

[Reymit으로 후원](https://reymit.ir/farland_game) ❤️
