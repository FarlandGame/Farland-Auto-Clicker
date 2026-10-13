# Farland Auto Clicker

[English](../README.md) | [日本語](README.ja.md) | [فارسی](README.fa.md)

実際のクリックごとに独立した 1 秒間の追加クリック処理を開始する Windows 用オートクリッカー。左右の個別設定とペルシャ語の画面を備えています。

**制作者：Bardiya Alizadeh（Kabir）／活動名：Farland_game**

**[Windows 用 ZIP をダウンロード](https://github.com/FarlandGame/Farland-Auto-Clicker/releases/latest/download/Farland-Auto-Clicker.zip)** · [リリース一覧](https://github.com/FarlandGame/Farland-Auto-Clicker/releases)

![Farland Auto Clicker の画面](../preview.png)

Farland Auto Clicker は、**Bardiya Alizadeh（Kabir）／活動名 Farland_game** が制作した Windows 用デスクトップアプリです。主な特徴は、自動クリックの開始方法にあります。**実際にマウスをクリックするたびに、そのクリックをきっかけとして、1 秒間の追加クリック処理が始まります。** 自分のマウス操作で追加クリックの開始タイミングを決め、左右のボタンを個別に調整したい人に向けた設計です。ペルシャ語の画面、変更可能な操作キー、設定の保存、すぐに使える Windows 実行ファイルを備えています。

## 実際のクリックから追加クリックへ

オートクリッカーを有効にしてから、左または右ボタンをクリックします。実際のクリックは通常どおり送信され、その後の 1 秒間に同じボタンの追加クリックが予定されます。たとえば左側を **20 CPS** に設定すると、実際の左クリック 1 回につき、**左の追加クリック 20 回**が予定されます。対象アプリの入力処理によりますが、実際の 1 回を含めると、要求されるクリック数は合計 21 回です。

最初の処理が終わる前に再びクリックすると、別の追加クリック処理が始まります。左を 2 回クリックした場合、それぞれの 1 秒間の処理を合わせて、追加クリック 40 回が予定されます。そのため CPS は**個々の処理の設定値**であり、重なった処理全体の上限ではありません。新しい実際のクリックがなければ、新しい処理は始まりません。すでに予定された処理は、完了するかオートクリッカーを停止するまで続きます。

## 操作の流れの違い

よく使われる[停止するまで繰り返す方式](https://www.opautoclicker.com/)では、開始操作後にクリックを繰り返します。Farland Auto Clicker の特徴は、**実際のクリックごとに追加クリック処理を始めること**と、左右の設定を個別に持つことです。

| 操作 | 停止するまで繰り返す方式 | Farland Auto Clicker |
| --- | --- | --- |
| 追加クリックの開始 | 繰り返し処理を開始 | 有効にしてから実際にクリック |
| 新しい実際のクリック | 繰り返しの継続には不要 | 新しい追加クリック処理を開始 |
| 処理の終了 | 繰り返し処理を停止 | 各処理が 1 秒間の予定を完了 |

この比較は 2 種類の操作方式を説明するものです。他のオートクリッカーが追加のモードを備えている場合もあります。ここでは、実際のコードで確認できる動作と操作を紹介しています。

## 左右を個別に調整

左右それぞれを **1～10,000 CPS** に設定でき、各ボタンを個別に有効／無効にできます。左を 20 CPS、右を 8 CPS に設定した場合、左クリックは左の処理を、右クリックは右の処理を開始します。一方を無効にすると、そのボタンの実際のクリックは通常どおり働き、新しい追加クリックを発生させません。

## 自分の環境に合わせた操作

メインボタン、または中央ボタン、左右のサイドボタン、F6～F9、Home、End、Insert から選んだグローバルホットキーで、有効／無効を切り替えられます。**F12** は緊急停止と終了に使います。ダーク、ライト、パープル、ブルーの 4 種類のテーマがあります。クリック速度、左右の有効状態、ホットキー、テーマは次回起動時にも復元されます。無効なクリック速度の入力は、直前の有効な値に戻ります。

## 追加クリックを適切に処理

実際の入力と Windows が注入された入力として識別するクリックを区別し、アプリ自身が作ったクリックで新しい処理が始まることを防ぎます。スケジューラーが重なった処理を管理し、高速時はクリックを小さな単位にまとめて送信します。**10,000 CPS は設定可能な上限であり、実測速度の保証ではありません。** 実際の送信速度はパソコンの性能、Windows の入力処理、対象アプリに依存します。

## ダウンロードとソースコード

公開 ZIP には実行ファイル、ソースコード、画面のプレビュー、英語・日本語・ペルシャ語の説明が入っています。展開後に `Farland-Auto-Clicker/dist/Farland Auto Clicker.exe` を開けば使え、実行ファイル版には Python の別途インストールは必要ありません。ソースコードの対象は Windows 10 または 11 と Python 3.10 以降で、Tkinter と Windows API を使用しています。リポジトリには、クリックを模擬して実行する 6 件のテストもあります。スケジューリング、左右の同時処理、取り消し、ホットキー、注入された入力の除外を確認します。

## 使い方

1. `Farland-Auto-Clicker.zip` をダウンロードして展開します。
2. `Farland-Auto-Clicker/dist/Farland Auto Clicker.exe` を開きます。実行ファイル版には Python の別途インストールは必要ありません。
3. 左右それぞれの CPS（1 秒あたりのクリック数）を設定し、使いたいボタンを有効にします。
4. マウスの中央ボタン、またはアプリのメインボタンでオートクリッカーを有効にします。
5. 実際に左または右ボタンをクリックすると、同じボタンの追加クリックが、その後の 1 秒間に実行されます。
6. **F12** を押すと、待機中のクリックを停止してアプリを終了します。

## 操作と設定

| 操作 | 動作 |
| --- | --- |
| メインボタン／選択したホットキー | 有効／無効の切り替え |
| F12 | 緊急停止して終了 |
| CPS 欄で Enter／別の欄へ移動 | 有効な値を適用 |

無効な入力は前の値に戻ります。設定ファイルは `%APPDATA%\Farland Auto Clicker\settings.json` に保存されます。

## ソースコードから実行

**Windows 10 または 11**、および Tkinter を含む **Python 3.10 以降**が必要です。実行時にサードパーティーのパッケージは必要ありません。

```powershell
py main.py
```

## 実行ファイルのビルド

プロジェクトのフォルダーで実行します。

```powershell
py -m pip install -r requirements.txt
py create_icon.py
py -m PyInstaller --noconfirm --clean "Farland Auto Clicker.spec"
```

出力先は `dist/Farland Auto Clicker.exe` です。管理者として動作しているアプリに入力する場合、オートクリッカーも同じ権限で実行してください。Windows は、より高い権限のアプリへの入力を制限します。

## ファイル構成

| ファイル | 内容 |
| --- | --- |
| `main.py` | Tkinter の画面、操作、テーマ、制作者のリンク |
| `click_engine.py` | Windows 入力フックとクリックのスケジューラー |
| `settings.py` | 設定の検証と JSON のアトミック保存 |
| `create_icon.py`, `farland.ico` | アプリのアイコン |
| `Farland Auto Clicker.spec` | PyInstaller のビルド設定 |
| `test_click_engine.py` | スケジューラーとフックの動作テスト |
| `docs/` | 日本語とペルシャ語の説明 |

リリース ZIP には既存の Windows 実行ファイルとソースコードを収録しています。ビルド用キャッシュと一時ファイルは含みません。

## テスト

Windows 上で実行します。

```powershell
py -B -m unittest -v test_click_engine
```

テストではクリック送信を模擬し、実際のマウスクリックは発生しません。

## 制作者

**Bardiya Alizadeh（Kabir）· Farland_game**

[GitHub ポートフォリオ](https://github.com/FarlandGame)

### チャンネルと SNS

| プラットフォーム | チャンネル／ページ |
| --- | --- |
| YouTube | [Farland_game](https://www.youtube.com/@Farland_game) · [Farland_animation](https://www.youtube.com/@Farland_animation) |
| Rubika チャンネル | [farland_gam](https://rubika.ir/farland_gam) · [Farland_animatio](https://rubika.ir/Farland_animatio) |
| Rubika ページ | [farland_game](https://rubika.ir/farland_game) · [Farland_animations](https://rubika.ir/Farland_animations) |
| Instagram | [farland_game](https://www.instagram.com/farland_game/) |
| Telegram チャンネル | [Farland_gam](https://t.me/Farland_gam) · [Farland_animatio](https://t.me/Farland_animatio) |
| Twitch | [farlandgame](https://twitch.tv/farlandgame) |
| Kick | [farlandgame](https://kick.com/farlandgame) |
| Aparat | [Farland_Game](https://aparat.com/Farland_Game) |
| SoundCloud | [Bardiya Kabir](https://soundcloud.com/bardiya-kabir-798008614) |

### Telegram 音楽ボット

[Farland Music Bot](https://t.me/Farland_Music_bot) — 曲の動画リンクを Telegram ボットに送って、曲を探せます。

### コミュニティと家族

- **THE APEX：** [YouTube](https://www.youtube.com/@THE_APEX_MC) · [Telegram](https://t.me/+-3uY7eIZArVjZDE0)
- **Manhunt：** [Telegram グループ](https://t.me/+DAq20XrkPyZhNjVk)
- **兄弟のチャンネル：** [YouTube の ArmiyaFabix](https://www.youtube.com/@ArmiyaFabix)

### 活動を応援する

[Reymit で支援する](https://reymit.ir/farland_game) ❤️
