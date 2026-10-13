# Farland_autcliker

[English](../README.md) | [日本語](README.ja.md) | [فارسی](README.fa.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Español](README.es.md) | [Português (Brasil)](README.pt-BR.md) | [Italiano](README.it.md) | [Nederlands](README.nl.md) | [Polski](README.pl.md) | [Українська](README.uk.md) | [Türkçe](README.tr.md) | [Русский](README.ru.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [한국어](README.ko.md) | [हिन्दी](README.hi.md) | [Bahasa Indonesia](README.id.md)

Pengklik otomatis untuk Windows yang memulai rangkaian klik tambahan secara mandiri selama satu detik setiap kali ada klik fisik, dengan kontrol tombol kiri/kanan terpisah dan antarmuka berbahasa Persia.

**Dibuat oleh Bardiya Alizadeh (Kabir), yang dikenal sebagai Farland_game.**

**[Unduh ZIP untuk Windows](https://github.com/FarlandGame/Farland_autcliker/releases/latest/download/Farland_autcliker.zip)** · [Semua rilis](https://github.com/FarlandGame/Farland_autcliker/releases)

![Antarmuka Farland_autcliker](../preview.png)

Farland_autcliker adalah aplikasi desktop Windows yang dibuat oleh **Bardiya Alizadeh (Kabir), yang dikenal sebagai Farland_game**. Ciri utamanya adalah cara otomatisasi dimulai: **setiap klik mouse fisik memulai rangkaian klik tambahannya sendiri selama satu detik**. Aplikasi ini dirancang bagi pengguna yang ingin menentukan kapan rangkaian dimulai melalui input mouse mereka sendiri, sekaligus mengendalikan tombol kiri dan kanan secara terpisah. Perilaku ini dipadukan dengan antarmuka berbahasa Persia, kontrol yang dapat disesuaikan, preferensi tersimpan, dan berkas eksekusi Windows yang siap dijalankan.

## Bagaimana klik Anda menjadi klik tambahan

Aktifkan pengklik, lalu klik tombol kiri atau kanan mouse. Klik fisik asli diteruskan seperti biasa, dan program menjadwalkan klik tambahan untuk tombol yang sama selama satu detik berikutnya. Sebagai contoh, jika sisi kiri diatur ke **20 CPS**, satu klik kiri fisik menjadwalkan **20 klik kiri tambahan**. Termasuk klik fisik, interaksi tersebut meminta total 21 klik, dengan hasil yang bergantung pada cara aplikasi tujuan menangani input.

Klik fisik kedua memulai rangkaian baru meskipun rangkaian pertama masih berjalan. Dua klik kiri seperti ini menjadwalkan 40 klik tambahan dalam jendela satu detik masing-masing yang saling tumpang tindih. Artinya, pengaturan tersebut menjelaskan **setiap rangkaian secara terpisah**, bukan batas keseluruhan untuk semua aktivitas yang tumpang tindih. Tanpa klik fisik baru, tidak ada rangkaian baru yang dibuat; rangkaian yang sudah dijadwalkan terus berjalan sampai selesai atau sampai Anda menghentikan pengklik.

## Apa yang membedakan cara kerjanya

[Cara kerja berulang sampai dihentikan](https://www.opautoclicker.com/) yang umum dikenal menjalankan urutan berulang setelah diaktifkan. Keunikan Farland_autcliker adalah **rangkaian yang dipicu oleh klik fisik**, dengan pengaturan terpisah untuk setiap sisi.

| Interaksi | Berulang sampai dihentikan | Farland_autcliker |
| --- | --- | --- |
| Memulai klik tambahan | Memulai urutan berulang | Aktifkan, lalu lakukan klik fisik |
| Klik fisik baru | Tidak diperlukan agar pengulangan terus berjalan | Memulai rangkaian tambahannya sendiri |
| Mengakhiri urutan | Hentikan urutan berulang | Setiap rangkaian menyelesaikan jadwal satu detiknya |

Perbandingan ini menjelaskan dua cara kerja; pengklik otomatis lain dapat menawarkan mode tambahan. Kelebihan Farland yang didokumentasikan adalah perilaku pemicu dan kontrol independennya.

## Kontrol kiri dan kanan yang independen

Atur kecepatan berbeda untuk setiap tombol, dari **1 hingga 10.000 CPS**, dan aktifkan masing-masing sisi secara terpisah. Misalnya, Anda dapat mengatur 20 CPS di kiri dan 8 CPS di kanan: klik kiri memulai rangkaian tombol kiri, sedangkan klik kanan memulai rangkaian tombol kanan yang independen. Jika satu sisi dinonaktifkan, klik fisik pada sisi tersebut tetap bekerja seperti biasa tanpa membuat klik tambahan baru.

## Kontrol yang sesuai dengan kebutuhan Anda

Ubah status aktif melalui tombol utama antarmuka atau tombol pintas global pilihan Anda: tombol tengah mouse, salah satu dari dua tombol samping mouse, F6–F9, Home, End, atau Insert. **F12** melakukan penghentian darurat dan menutup aplikasi. Empat tema—gelap, terang, ungu, dan biru—tersedia untuk memilih tampilan. Kecepatan klik, sisi yang diaktifkan, tombol pintas, dan tema disimpan untuk sesi berikutnya. Nilai kecepatan klik yang tidak valid dikembalikan ke nilai valid sebelumnya.

## Menangani input berulang dengan cermat

Mesin membedakan input mouse fisik dari klik yang disuntikkan melalui Windows, sehingga klik yang dihasilkannya sendiri tidak memulai rangkaian baru. Penjadwal mengelola rangkaian yang tumpang tindih dan mengirim klik berkecepatan tinggi dalam kelompok kecil. **10.000 CPS adalah batas atas yang dapat diatur, bukan jaminan kecepatan hasil pengukuran**: pengiriman nyata bergantung pada komputer, pemrosesan input Windows, dan aplikasi tujuan.

## Unduh dan jelajahi

ZIP Windows yang tersedia untuk umum mencakup berkas eksekusi, kode sumber, pratinjau antarmuka, dan dokumentasi berbahasa Inggris, Jepang, serta Persia. Ekstrak arsip dan buka `Farland-Auto-Clicker/dist/Farland Auto Clicker.exe`; berkas eksekusi dalam paket tidak memerlukan pemasangan Python secara terpisah. Kode sumber ditujukan untuk Windows 10 atau 11 dan Python 3.10 atau yang lebih baru, menggunakan Tkinter dan Windows API. Repositori juga menyediakan enam pengujian untuk penjadwalan, rangkaian kedua sisi yang tumpang tindih, pembatalan, tombol pintas, dan penyaringan input yang disuntikkan; semuanya menggunakan klik simulasi.

## Mulai cepat

1. Unduh dan ekstrak `Farland_autcliker.zip`.
2. Buka `Farland-Auto-Clicker/dist/Farland Auto Clicker.exe`. Aplikasi dalam paket tidak memerlukan pemasangan Python secara terpisah.
3. Atur jumlah klik per detik (CPS) untuk kiri dan kanan, lalu aktifkan sisi yang diperlukan.
4. Tekan tombol tengah mouse atau tombol pengalih utama untuk mengaktifkan pengklik.
5. Setiap klik kiri/kanan fisik memulai rangkaian klik tambahan pada tombol yang sama selama satu detik berikutnya.
6. Tekan **F12** untuk menghentikan semua klik yang masih menunggu dan keluar.

## Kontrol dan pengaturan

| Kontrol | Tindakan |
| --- | --- |
| Tombol utama / tombol pintas terpilih | Mengaktifkan atau menonaktifkan pengklik otomatis |
| F12 | Penghentian darurat dan keluar |
| Enter / meninggalkan kolom CPS | Menerapkan nilai kecepatan klik yang valid |

Input kecepatan klik yang tidak valid dikembalikan ke nilai sebelumnya. Pengaturan disimpan di `%APPDATA%\Farland Auto Clicker\settings.json`.

## Menjalankan dari kode sumber

Memerlukan **Windows 10 atau 11** dan **Python 3.10 atau yang lebih baru**, termasuk Tkinter. Tidak diperlukan paket pihak ketiga untuk menjalankan kode sumber.

```powershell
py main.py
```

## Membangun berkas eksekusi Windows

Jalankan dari direktori proyek:

```powershell
py -m pip install -r requirements.txt
py create_icon.py
py -m PyInstaller --noconfirm --clean "Farland Auto Clicker.spec"
```

Hasilnya adalah `dist/Farland Auto Clicker.exe`. Untuk berinteraksi dengan aplikasi yang berjalan sebagai administrator, jalankan pengklik dengan tingkat hak akses yang sama; Windows membatasi input ke aplikasi dengan hak akses lebih tinggi.

## Struktur proyek

| Berkas | Fungsi |
| --- | --- |
| `main.py` | Antarmuka Tkinter, kontrol, tema, dan tautan pembuat |
| `click_engine.py` | Hook input Windows dan penjadwal klik |
| `settings.py` | Validasi pengaturan dan penyimpanan JSON secara atomik |
| `create_icon.py`, `farland.ico` | Ikon aplikasi |
| `Farland Auto Clicker.spec` | Konfigurasi pembangunan PyInstaller |
| `test_click_engine.py` | Pengujian perilaku penjadwal dan hook |
| `docs/` | Dokumentasi berbahasa Jepang dan Persia |

ZIP rilis mencakup berkas eksekusi Windows yang sudah ada dan berkas sumber. Cache pembangunan dan berkas sementara tidak disertakan.

## Pengujian

Di Windows:

```powershell
py -B -m unittest -v test_click_engine
```

Pengujian ini menggunakan pengirim klik simulasi; tidak menghasilkan klik mouse nyata.

## Pembuat

**Bardiya Alizadeh (Kabir) · Farland_game**

[Portofolio GitHub](https://github.com/FarlandGame)

### Kanal dan tautan sosial

| Platform | Kanal / halaman |
| --- | --- |
| GitHub | [FarlandGame](https://github.com/FarlandGame) |
| YouTube | [Farland_game](https://www.youtube.com/@Farland_game) · [Farland_animation](https://www.youtube.com/@Farland_animation) |
| Kanal Rubika | [farland_gam](https://rubika.ir/farland_gam) · [Farland_animatio](https://rubika.ir/Farland_animatio) |
| Halaman Rubika | [farland_game](https://rubika.ir/farland_game) · [Farland_animations](https://rubika.ir/Farland_animations) |
| Instagram | [farland_game](https://www.instagram.com/farland_game/) |
| Kanal Telegram | [Farland_gam](https://t.me/Farland_gam) · [Farland_animatio](https://t.me/Farland_animatio) |
| Twitch | [farlandgame](https://twitch.tv/farlandgame) |
| Kick | [farlandgame](https://kick.com/farlandgame) |
| Aparat | [Farland_Game](https://aparat.com/Farland_Game) |
| SoundCloud | [Bardiya Kabir](https://soundcloud.com/bardiya-kabir-798008614) |

### Bot musik Telegram

[Farland Music Bot](https://t.me/Farland_Music_bot) — Kirim tautan video sebuah lagu ke bot Telegram kami untuk menemukan lagunya.

### Komunitas dan keluarga

- **THE APEX:** [YouTube](https://www.youtube.com/@THE_APEX_MC) · [Telegram](https://t.me/+-3uY7eIZArVjZDE0)
- **Manhunt:** [Grup Telegram](https://t.me/+DAq20XrkPyZhNjVk)
- **Kanal saudara saya:** [ArmiyaFabix di YouTube](https://www.youtube.com/@ArmiyaFabix)

### Dukung karya saya

[Donasi melalui Reymit](https://reymit.ir/farland_game) ❤️
