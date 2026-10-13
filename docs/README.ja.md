# Farland Auto Clicker

[English](../README.md) | [日本語](README.ja.md) | [فارسی](README.fa.md)

ペルシャ語のインターフェースを備えた Windows 用オートクリッカーです。左右のクリック速度を個別に設定でき、切り替え用ホットキーと緊急停止に対応しています。

**制作者：Bardiya Alizadeh（Kabir）／活動名：Farland_game**

**[Windows 用 ZIP をダウンロード](https://github.com/FarlandGame/Farland-Auto-Clicker/releases/latest/download/Farland-Auto-Clicker.zip)** · [リリース一覧](https://github.com/FarlandGame/Farland-Auto-Clicker/releases)

![Farland Auto Clicker の画面](../preview.png)

## 使い方

1. `Farland-Auto-Clicker.zip` をダウンロードして展開します。
2. `Farland-Auto-Clicker/dist/Farland Auto Clicker.exe` を開きます。実行ファイル版には Python の別途インストールは必要ありません。
3. 左右それぞれの CPS（1 秒あたりのクリック数）を設定し、使いたいボタンを有効にします。
4. マウスの中央ボタン、またはアプリのメインボタンでオートクリッカーを有効にします。
5. 実際に左または右ボタンをクリックすると、同じボタンの追加クリックが、その後の 1 秒間に実行されます。
6. **F12** を押すと、待機中のクリックを停止してアプリを終了します。

## 主な機能

- 左右のクリック速度を **1～10,000 CPS** の範囲で個別に設定。
- 左右のボタンをそれぞれ有効／無効に設定。
- 切り替えキーは中央ボタン、サイドボタン、F6～F9、Home、End、Insert から選択。
- ダーク、ライト、パープル、ブルーの 4 種類のテーマ。
- 設定を保存し、次回起動時に読み込み。
- 複数のクリック処理を並行してスケジューリングし、高速時はまとめて送信。
- Windows が注入された入力として識別するクリックを除外し、追加クリックが再び処理を開始することを防止。

実際のクリック自体も通常どおり送信されます。1 回の実際のクリックにつき、設定した CPS と同じ数の**追加クリック**を 1 秒間に予定します。複数回クリックすると処理が重なることがあります。10,000 CPS は設定上の上限であり、実際の速度はパソコンの性能、Windows の入力処理、対象アプリの制限に依存します。

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

[GitHub](https://github.com/FarlandGame) · [YouTube](https://www.youtube.com/@Farland_game)
