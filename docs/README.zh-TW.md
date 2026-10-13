# Farland_autcliker

[English](../README.md) | [日本語](README.ja.md) | [فارسی](README.fa.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Español](README.es.md) | [Português (Brasil)](README.pt-BR.md) | [Italiano](README.it.md) | [Nederlands](README.nl.md) | [Polski](README.pl.md) | [Українська](README.uk.md) | [Türkçe](README.tr.md) | [Русский](README.ru.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [한국어](README.ko.md) | [हिन्दी](README.hi.md) | [Bahasa Indonesia](README.id.md)

一款 Windows 自動點擊器：每次實際按下滑鼠按鈕，都會啟動一組獨立、持續一秒的額外點擊。左右鍵可分別控制，程式介面為波斯語。

**由 Bardiya Alizadeh（Kabir）創作，藝名 Farland_game。**

**[下載 Windows ZIP 壓縮檔](https://github.com/FarlandGame/Farland_autcliker/releases/latest/download/Farland_autcliker.zip)** · [所有版本](https://github.com/FarlandGame/Farland_autcliker/releases)

![Farland_autcliker 介面](../preview.png)

Farland_autcliker 是由 **Bardiya Alizadeh（Kabir，藝名 Farland_game）** 開發的 Windows 桌面應用程式。它的主要特色是自動點擊的啟動方式：**每次實際滑鼠點擊都會啟動各自的一秒額外點擊序列**。它適合希望透過自己的滑鼠操作決定何時啟動點擊序列，並獨立控制左右鍵的使用者。程式將這項機制與波斯語介面、可自訂的控制方式、設定儲存，以及可直接執行的 Windows 執行檔結合在一起。

## 你的點擊如何變成額外點擊

啟用點擊器後，按下滑鼠左鍵或右鍵。原始的實際點擊會正常傳遞，程式則在接下來的一秒內為同一個按鈕安排額外點擊。例如，將左鍵設為 **20 CPS** 時，一次實際左鍵點擊會安排 **20 次額外左鍵點擊**。加上實際點擊，這次操作共請求 21 次點擊；實際結果取決於目標應用程式處理輸入的方式。

即使第一組點擊尚未結束，第二次實際點擊也會啟動新的一組。在這種情況下，兩次實際左鍵點擊會在各自互相重疊的一秒時段內安排共 40 次額外點擊。因此，這個數值描述的是**每一組獨立點擊序列**，而非所有重疊活動的總上限。沒有新的實際點擊，就不會建立新的序列；已安排的序列會繼續執行，直到完成或你停止點擊器。

## 這種操作方式有何不同

常見的[持續重複直到停止的操作方式](https://www.opautoclicker.com/)會在啟用後持續重複一段點擊序列。Farland_autcliker 的特色是**由實際點擊觸發短時點擊序列**，左右鍵分別設定。

| 操作 | 持續重複直到停止 | Farland_autcliker |
| --- | --- | --- |
| 開始額外點擊 | 啟動重複序列 | 啟用後，再實際點擊滑鼠 |
| 新的實際點擊 | 維持重複時不需要再次點擊 | 啟動自己的一組額外點擊 |
| 結束一組點擊 | 停止重複序列 | 每組完成自己的一秒安排 |

此表比較的是兩種操作方式；不同自動點擊器可能還提供其他模式。Farland 已記錄的優勢是它的觸發機制與獨立控制。

## 左右鍵獨立控制

為每個按鈕分別設定 **1 至 10,000 CPS** 的速度，並單獨啟用任一側。例如，左鍵可設為 20 CPS，右鍵設為 8 CPS：實際左鍵點擊啟動左鍵序列，實際右鍵點擊啟動獨立的右鍵序列。停用某一側後，該按鈕的實際點擊仍正常運作，但不會再產生新的額外點擊。

## 適合你的控制方式

透過主介面按鈕或所選的全域快捷鍵切換啟用狀態：滑鼠中鍵、任一個滑鼠側鍵、F6–F9、Home、End 或 Insert。**F12** 可緊急停止並結束程式。深色、淺色、紫色和藍色四種佈景主題可供選擇。點擊速度、啟用的左右鍵、快捷鍵和佈景主題都會儲存以供下次使用。輸入無效的點擊速度時，會還原之前的有效值。

## 謹慎處理重複輸入

引擎能區分實際滑鼠輸入與 Windows 注入的點擊，因此自身產生的點擊不會再次啟動新的序列。排程器管理互相重疊的序列，並以小批次傳送高速點擊。**10,000 CPS 是可設定的上限，並非經過測量的速度保證**：實際傳遞情況取決於電腦效能、Windows 的輸入處理以及目標應用程式。

## 下載並了解專案

公開的 Windows ZIP 壓縮檔包含執行檔、原始碼、介面預覽，以及英語、日語和波斯語文件。解壓縮後開啟 `Farland-Auto-Clicker/dist/Farland Auto Clicker.exe`；打包後的程式不需要另外安裝 Python。原始碼以 Windows 10 或 11 和 Python 3.10 以上版本為目標，使用 Tkinter 與 Windows API。儲存庫也包含六項測試，用於檢查排程、左右鍵序列重疊、取消、快捷鍵和注入輸入過濾；測試使用模擬點擊。

## 快速開始

1. 下載並解壓縮 `Farland_autcliker.zip`。
2. 開啟 `Farland-Auto-Clicker/dist/Farland Auto Clicker.exe`。打包後的程式不需要另外安裝 Python。
3. 設定左右鍵的每秒點擊次數（CPS），並啟用需要的按鈕。
4. 按下滑鼠中鍵或主切換按鈕，啟用點擊器。
5. 每次實際左鍵或右鍵點擊，都會在接下來的一秒內為同一按鈕啟動一組額外點擊。
6. 按 **F12** 停止所有等待執行的點擊並結束程式。

## 控制與設定

| 控制項 | 操作 |
| --- | --- |
| 主按鈕 / 所選快捷鍵 | 切換自動點擊器的啟用狀態 |
| F12 | 緊急停止並結束程式 |
| Enter / 離開 CPS 輸入欄位 | 套用有效的點擊速度 |

無效的點擊速度輸入會還原為之前的值。設定儲存在 `%APPDATA%\Farland Auto Clicker\settings.json`。

## 從原始碼執行

需要 **Windows 10 或 11** 和 **Python 3.10 以上版本**，並包含 Tkinter。執行原始碼不需要第三方套件。

```powershell
py main.py
```

## 建置 Windows 執行檔

在專案目錄中執行：

```powershell
py -m pip install -r requirements.txt
py create_icon.py
py -m PyInstaller --noconfirm --clean "Farland Auto Clicker.spec"
```

輸出檔案為 `dist/Farland Auto Clicker.exe`。如需操作以系統管理員身分執行的應用程式，請以相同權限執行點擊器；Windows 會限制向權限較高的應用程式傳送輸入。

## 專案結構

| 檔案 | 用途 |
| --- | --- |
| `main.py` | Tkinter 介面、控制項、佈景主題和創作者連結 |
| `click_engine.py` | Windows 輸入掛鉤與點擊排程器 |
| `settings.py` | 設定驗證與 JSON 原子儲存 |
| `create_icon.py`, `farland.ico` | 程式圖示 |
| `Farland Auto Clicker.spec` | PyInstaller 建置設定 |
| `test_click_engine.py` | 排程器和輸入掛鉤行為測試 |
| `docs/` | 日語和波斯語文件 |

發行版 ZIP 壓縮檔包含現有的 Windows 執行檔與原始碼檔案，不包含建置快取與暫存檔。

## 測試

在 Windows 上執行：

```powershell
py -B -m unittest -v test_click_engine
```

這些測試使用模擬點擊傳送器，不會產生實際的滑鼠點擊。

## 創作者

**Bardiya Alizadeh（Kabir）· Farland_game**

[GitHub 作品集](https://github.com/FarlandGame)

### 頻道與社群連結

| 平台 | 頻道 / 頁面 |
| --- | --- |
| GitHub | [FarlandGame](https://github.com/FarlandGame) |
| YouTube | [Farland_game](https://www.youtube.com/@Farland_game) · [Farland_animation](https://www.youtube.com/@Farland_animation) |
| Rubika 頻道 | [farland_gam](https://rubika.ir/farland_gam) · [Farland_animatio](https://rubika.ir/Farland_animatio) |
| Rubika 頁面 | [farland_game](https://rubika.ir/farland_game) · [Farland_animations](https://rubika.ir/Farland_animations) |
| Instagram | [farland_game](https://www.instagram.com/farland_game/) |
| Telegram 頻道 | [Farland_gam](https://t.me/Farland_gam) · [Farland_animatio](https://t.me/Farland_animatio) |
| Twitch | [farlandgame](https://twitch.tv/farlandgame) |
| Kick | [farlandgame](https://kick.com/farlandgame) |
| Aparat | [Farland_Game](https://aparat.com/Farland_Game) |
| SoundCloud | [Bardiya Kabir](https://soundcloud.com/bardiya-kabir-798008614) |

### Telegram 音樂機器人

[Farland Music Bot](https://t.me/Farland_Music_bot) — 將歌曲的影片連結傳送給我們的 Telegram 機器人，以尋找該曲目。

### 社群與家人

- **THE APEX：** [YouTube](https://www.youtube.com/@THE_APEX_MC) · [Telegram](https://t.me/+-3uY7eIZArVjZDE0)
- **Manhunt：** [Telegram 群組](https://t.me/+DAq20XrkPyZhNjVk)
- **我兄弟的頻道：** [YouTube 上的 ArmiyaFabix](https://www.youtube.com/@ArmiyaFabix)

### 支持我的創作

[透過 Reymit 捐款](https://reymit.ir/farland_game) ❤️
