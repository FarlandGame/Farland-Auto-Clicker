# Farland_autcliker

[English](../README.md) | [日本語](README.ja.md) | [فارسی](README.fa.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Español](README.es.md) | [Português (Brasil)](README.pt-BR.md) | [Italiano](README.it.md) | [Nederlands](README.nl.md) | [Polski](README.pl.md) | [Українська](README.uk.md) | [Türkçe](README.tr.md) | [Русский](README.ru.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [한국어](README.ko.md) | [हिन्दी](README.hi.md) | [Bahasa Indonesia](README.id.md)

一款 Windows 自动点击器：每次实际按下鼠标按钮，都会启动一组独立、持续一秒的额外点击。左右键可分别控制，程序界面为波斯语。

**由 Bardiya Alizadeh（Kabir）创作，艺名 Farland_game。**

**[下载 Windows ZIP 压缩包](https://github.com/FarlandGame/Farland_autcliker/releases/latest/download/Farland_autcliker.zip)** · [全部版本](https://github.com/FarlandGame/Farland_autcliker/releases)

![Farland_autcliker 界面](../preview.png)

Farland_autcliker 是由 **Bardiya Alizadeh（Kabir，艺名 Farland_game）** 开发的 Windows 桌面应用。它的主要特色是自动点击的启动方式：**每次实际鼠标点击都会启动各自的一秒额外点击序列**。它适合希望通过自己的鼠标操作决定何时启动点击序列，并独立控制左右键的用户。程序将这一机制与波斯语界面、可自定义的控制方式、设置保存和开箱即用的 Windows 可执行文件结合在一起。

## 你的点击如何变成额外点击

启用点击器后，按下鼠标左键或右键。原始的实际点击会正常传递，程序则在接下来的一秒内为同一个按钮安排额外点击。例如，将左键设置为 **20 CPS** 时，一次实际左键点击会安排 **20 次额外左键点击**。加上实际点击，这次操作共请求 21 次点击；实际结果取决于目标应用对输入的处理方式。

即使第一组点击尚未结束，第二次实际点击也会启动新的一组。这种情况下，两次实际左键点击会在各自相互重叠的一秒时间段内安排共 40 次额外点击。因此，这个数值描述的是**每一组独立点击序列**，并非所有重叠活动的全局上限。不发生新的实际点击时，就不会创建新的序列；已经安排的序列会继续执行，直到完成或你停止点击器。

## 这种操作方式有何不同

常见的[持续重复直到停止的操作方式](https://www.opautoclicker.com/)会在启用后不断重复一段点击序列。Farland_autcliker 的特点是**由实际点击触发短时点击序列**，左右键分别设置。

| 操作 | 持续重复直到停止 | Farland_autcliker |
| --- | --- | --- |
| 开始额外点击 | 启动重复序列 | 启用后，再实际点击鼠标 |
| 新的实际点击 | 维持重复时无需再点击 | 启动自己的一组额外点击 |
| 结束一组点击 | 停止重复序列 | 每组完成自己的一秒安排 |

此表比较的是两种操作方式；不同自动点击器可能还提供其他模式。Farland 已记录的优势是它的触发机制和独立控制。

## 左右键独立控制

为每个按钮分别设置 **1 至 10,000 CPS** 的速度，并单独启用任意一侧。例如，左键可设为 20 CPS，右键设为 8 CPS：实际左键点击启动左键序列，实际右键点击启动独立的右键序列。禁用某一侧后，该按钮的实际点击仍正常工作，但不会再产生新的额外点击。

## 适合你的控制方式

通过主界面的按钮或所选全局快捷键切换启用状态：鼠标中键、任意一个鼠标侧键、F6–F9、Home、End 或 Insert。**F12** 可紧急停止并退出程序。深色、浅色、紫色和蓝色四种主题可供选择。点击速度、启用的左右键、快捷键和主题都会保存供下次使用。输入无效的点击速度时，会恢复之前的有效值。

## 谨慎处理重复输入

引擎能区分实际鼠标输入与 Windows 注入的点击，因此自身生成的点击不会再启动新的序列。调度器管理相互重叠的序列，并以小批次发送高速点击。**10,000 CPS 是可配置的上限，并非经过测量的速度保证**：实际传递情况取决于电脑性能、Windows 的输入处理以及目标应用。

## 下载并了解项目

公开的 Windows ZIP 包包含可执行文件、源代码、界面预览以及英语、日语和波斯语文档。解压后打开 `Farland-Auto-Clicker/dist/Farland Auto Clicker.exe`；打包后的程序不需要另外安装 Python。源代码面向 Windows 10 或 11 和 Python 3.10 及以上版本，使用 Tkinter 与 Windows API。仓库还包含六项测试，用于检查调度、左右键序列重叠、取消、快捷键和注入输入过滤；测试使用模拟点击。

## 快速开始

1. 下载并解压 `Farland_autcliker.zip`。
2. 打开 `Farland-Auto-Clicker/dist/Farland Auto Clicker.exe`。打包后的程序不需要另外安装 Python。
3. 设置左右键的每秒点击次数（CPS），并启用需要的按钮。
4. 按下鼠标中键或主切换按钮，启用点击器。
5. 每次实际左键或右键点击，都会在接下来的一秒内为同一按钮启动一组额外点击。
6. 按 **F12** 停止所有等待执行的点击并退出。

## 控制与设置

| 控制项 | 操作 |
| --- | --- |
| 主按钮 / 所选快捷键 | 切换自动点击器的启用状态 |
| F12 | 紧急停止并退出 |
| Enter / 离开 CPS 输入框 | 应用有效的点击速度 |

无效的点击速度输入会恢复为之前的值。设置保存在 `%APPDATA%\Farland Auto Clicker\settings.json`。

## 从源代码运行

需要 **Windows 10 或 11** 和 **Python 3.10 及以上版本**，并包含 Tkinter。运行源代码不需要第三方软件包。

```powershell
py main.py
```

## 构建 Windows 可执行文件

在项目目录中执行：

```powershell
py -m pip install -r requirements.txt
py create_icon.py
py -m PyInstaller --noconfirm --clean "Farland Auto Clicker.spec"
```

输出文件为 `dist/Farland Auto Clicker.exe`。如需操作以管理员身份运行的应用，请以相同权限运行点击器；Windows 会限制向更高权限应用发送输入。

## 项目结构

| 文件 | 用途 |
| --- | --- |
| `main.py` | Tkinter 界面、控制项、主题和创作者链接 |
| `click_engine.py` | Windows 输入钩子与点击调度器 |
| `settings.py` | 设置验证与 JSON 原子保存 |
| `create_icon.py`, `farland.ico` | 程序图标 |
| `Farland Auto Clicker.spec` | PyInstaller 构建配置 |
| `test_click_engine.py` | 调度器和钩子行为测试 |
| `docs/` | 日语和波斯语文档 |

发行版 ZIP 包包含现有的 Windows 可执行文件与源文件，不包含构建缓存和临时文件。

## 测试

在 Windows 上执行：

```powershell
py -B -m unittest -v test_click_engine
```

这些测试使用模拟点击发送器，不会产生真实的鼠标点击。

## 创作者

**Bardiya Alizadeh（Kabir）· Farland_game**

[GitHub 作品集](https://github.com/FarlandGame)

### 频道与社交链接

| 平台 | 频道 / 页面 |
| --- | --- |
| GitHub | [FarlandGame](https://github.com/FarlandGame) |
| YouTube | [Farland_game](https://www.youtube.com/@Farland_game) · [Farland_animation](https://www.youtube.com/@Farland_animation) |
| Rubika 频道 | [farland_gam](https://rubika.ir/farland_gam) · [Farland_animatio](https://rubika.ir/Farland_animatio) |
| Rubika 页面 | [farland_game](https://rubika.ir/farland_game) · [Farland_animations](https://rubika.ir/Farland_animations) |
| Instagram | [farland_game](https://www.instagram.com/farland_game/) |
| Telegram 频道 | [Farland_gam](https://t.me/Farland_gam) · [Farland_animatio](https://t.me/Farland_animatio) |
| Twitch | [farlandgame](https://twitch.tv/farlandgame) |
| Kick | [farlandgame](https://kick.com/farlandgame) |
| Aparat | [Farland_Game](https://aparat.com/Farland_Game) |
| SoundCloud | [Bardiya Kabir](https://soundcloud.com/bardiya-kabir-798008614) |

### Telegram 音乐机器人

[Farland Music Bot](https://t.me/Farland_Music_bot) — 把歌曲的视频链接发送给我们的 Telegram 机器人，以查找该曲目。

### 社群与家人

- **THE APEX：** [YouTube](https://www.youtube.com/@THE_APEX_MC) · [Telegram](https://t.me/+-3uY7eIZArVjZDE0)
- **Manhunt：** [Telegram 群组](https://t.me/+DAq20XrkPyZhNjVk)
- **我兄弟的频道：** [YouTube 上的 ArmiyaFabix](https://www.youtube.com/@ArmiyaFabix)

### 支持我的创作

[通过 Reymit 捐赠](https://reymit.ir/farland_game) ❤️
