# Farland_autcliker

[English](../README.md) | [日本語](README.ja.md) | [فارسی](README.fa.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Español](README.es.md) | [Português (Brasil)](README.pt-BR.md) | [Italiano](README.it.md) | [Nederlands](README.nl.md) | [Polski](README.pl.md) | [Українська](README.uk.md) | [Türkçe](README.tr.md) | [Русский](README.ru.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [한국어](README.ko.md) | [हिन्दी](README.hi.md) | [Bahasa Indonesia](README.id.md)

Her fiziksel tıklamada birbirinden bağımsız, bir saniyelik ek tıklama serisi başlatan; sol ve sağ tuş için ayrı kontrollere ve Farsça arayüze sahip bir Windows otomatik tıklama uygulaması.

**Farland_game adıyla tanınan Bardiya Alizadeh (Kabir) tarafından geliştirildi.**

**[Windows ZIP dosyasını indir](https://github.com/FarlandGame/Farland_autcliker/releases/latest/download/Farland_autcliker.zip)** · [Tüm sürümler](https://github.com/FarlandGame/Farland_autcliker/releases)

![Farland_autcliker arayüzü](../preview.png)

Farland_autcliker, **Farland_game adıyla tanınan Bardiya Alizadeh (Kabir)** tarafından geliştirilen bir Windows masaüstü uygulamasıdır. Onu öne çıkaran özellik, otomasyonun başlama şeklidir: **her fiziksel fare tıklaması, kendi bir saniyelik ek tıklama serisini başlatır**. Sol ve sağ tuşu bağımsız olarak kontrol ederken bir serinin ne zaman başlayacağına kendi fare girişleriyle karar vermek isteyenler için tasarlanmıştır. Bu davranışı Farsça arayüz, özelleştirilebilir kontroller, kaydedilen tercihler ve çalıştırmaya hazır Windows uygulamasıyla bir araya getirir.

## Tıklamalarınız nasıl ek tıklamalara dönüşür?

Tıklayıcıyı etkinleştirin, ardından farenin sol veya sağ tuşuna basın. İlk fiziksel tıklama normal şekilde iletilir; uygulama aynı tuş için sonraki bir saniyeye ek tıklamalar planlar. Örneğin sol taraf **20 CPS** olarak ayarlandığında, bir fiziksel sol tıklama **20 ek sol tıklama** planlar. Fiziksel tıklama da sayıldığında bu işlem toplam 21 tıklama talep eder; sonuç hedef uygulamanın girdileri nasıl işlediğine bağlıdır.

İlk seri hâlâ sürerken bile ikinci fiziksel tıklama yeni bir seri başlatır. Bu şekilde yapılan iki sol tıklama, birbiriyle örtüşen bir saniyelik aralıklarda 40 ek tıklama planlar. Yani ayar, aynı anda çalışan tüm işlemler için genel bir sınırı değil, **her bir seriyi ayrı ayrı** tanımlar. Yeni fiziksel tıklama olmadığında yeni seri oluşturulmaz; önceden planlanmış seriler tamamlanana veya tıklayıcıyı durdurana kadar sürer.

## Bu kullanım biçimini farklı kılan nedir?

Bilinen [durdurulana kadar tekrarlama biçimi](https://www.opautoclicker.com/), etkinleştirildikten sonra tekrarlanan bir tıklama dizisi çalıştırır. Farland_autcliker'ın farkı, her taraf için ayrı ayarlarla **fiziksel tıklamayla tetiklenen seriler** kullanmasıdır.

| Etkileşim | Durdurulana kadar tekrarlama | Farland_autcliker |
| --- | --- | --- |
| Ek tıklamaları başlatma | Tekrarlama dizisini başlatırsınız | Etkinleştirir, sonra fiziksel olarak tıklarsınız |
| Yeni bir fiziksel tıklama | Tekrarın sürmesi için gerekli değildir | Kendine ait ek bir seri başlatır |
| Bir diziyi sonlandırma | Tekrarlama dizisini durdurursunuz | Her seri, bir saniyelik planını tamamlar |

Bu karşılaştırma iki kullanım biçimini anlatır; farklı otomatik tıklayıcılar ek modlar da sunabilir. Farland'ın belgelenen güçlü yanları, tetikleme davranışı ve bağımsız kontrolleridir.

## Sol ve sağ tuş için bağımsız kontrol

Her tuş için **1 ile 10.000 CPS** arasında farklı bir hız seçin ve her tarafı ayrı ayrı etkinleştirin. Örneğin solda 20 CPS, sağda 8 CPS ayarlayabilirsiniz: sol tıklama sol tuş serisini başlatırken sağ tıklama bağımsız bir sağ tuş serisi başlatır. Bir tarafı devre dışı bıraktığınızda o tarafın fiziksel tıklamaları normal çalışmaya devam eder, ancak yeni ek tıklamalar oluşturmaz.

## Kullanımınıza uygun kontroller

Ana arayüz düğmesiyle veya seçtiğiniz sistem genelinde çalışan kısayolla etkinleştirme durumunu değiştirin: orta fare tuşu, iki yan fare tuşundan biri, F6–F9, Home, End veya Insert. **F12**, acil durdurma yapar ve uygulamadan çıkar. Koyu, açık, mor ve mavi olmak üzere dört tema arasından görünümü seçebilirsiniz. Tıklama hızları, etkin taraflar, kısayol ve tema sonraki oturum için kaydedilir. Geçersiz tıklama hızı girişleri önceki geçerli değere döner.

## Tekrarlanan girdilerin dikkatli işlenmesi

Motor, fiziksel fare girdilerini Windows tarafından enjekte edilen tıklamalardan ayırır; böylece kendi ürettiği tıklamalar yeni seriler başlatmaz. Bir zamanlayıcı, örtüşen serileri yönetir ve yüksek hızlı tıklamaları küçük gruplar hâlinde gönderir. **10.000 CPS, ayarlanabilir üst sınırdır; ölçülmüş bir hız garantisi değildir**. Gerçekte iletilen tıklamalar bilgisayara, Windows'un girdi işlemesine ve hedef uygulamaya bağlıdır.

## İndirin ve inceleyin

Herkese açık Windows ZIP dosyası çalıştırılabilir uygulamayı, kaynak kodu, arayüz önizlemesini ve İngilizce, Japonca, Farsça belgeleri içerir. Arşivi açıp `Farland-Auto-Clicker/dist/Farland Auto Clicker.exe` dosyasını çalıştırın; paketlenmiş uygulama ayrı bir Python kurulumu gerektirmez. Kaynak kod Windows 10 veya 11 ve Python 3.10 veya üzerini hedefler; Tkinter ve Windows API kullanır. Depoda zamanlama, örtüşen sol/sağ seriler, iptal, kısayollar ve enjekte edilmiş girdilerin süzülmesi için altı test de bulunur; bunlar simüle edilmiş tıklamalar kullanır.

## Hızlı başlangıç

1. `Farland_autcliker.zip` dosyasını indirin ve arşivden çıkarın.
2. `Farland-Auto-Clicker/dist/Farland Auto Clicker.exe` dosyasını açın. Paketlenmiş uygulama ayrı bir Python kurulumu gerektirmez.
3. Sol ve sağ tuşun saniyedeki tıklama sayısını (CPS) ayarlayın ve ihtiyacınız olan tarafları etkinleştirin.
4. Tıklayıcıyı etkinleştirmek için orta fare tuşuna veya ana açma/kapama düğmesine basın.
5. Her fiziksel sol/sağ tıklama, aynı tuş için sonraki bir saniyeye yayılan ek tıklama serisi başlatır.
6. Bekleyen tüm tıklamaları durdurup çıkmak için **F12** tuşuna basın.

## Kontroller ve ayarlar

| Kontrol | İşlev |
| --- | --- |
| Ana düğme / seçilen kısayol | Otomatik tıklayıcıyı açar veya kapatır |
| F12 | Acil durdurma ve çıkış |
| Enter / CPS alanından çıkma | Geçerli tıklama hızını uygular |

Geçersiz hız girişleri önceki değere geri döner. Ayarlar `%APPDATA%\Farland Auto Clicker\settings.json` dosyasında saklanır.

## Kaynak koddan çalıştırma

Tkinter dâhil **Windows 10 veya 11** ve **Python 3.10 veya üzeri** gerekir. Kaynak kodu çalıştırmak için üçüncü taraf paket gerekmez.

```powershell
py main.py
```

## Windows uygulamasını derleme

Proje klasöründen çalıştırın:

```powershell
py -m pip install -r requirements.txt
py create_icon.py
py -m PyInstaller --noconfirm --clean "Farland Auto Clicker.spec"
```

Çıktı `dist/Farland Auto Clicker.exe` dosyasıdır. Yönetici olarak çalışan bir uygulamayla etkileşim kurmak için tıklayıcıyı aynı yetki düzeyinde çalıştırın; Windows, daha yüksek yetkili uygulamalara gönderilen girdileri sınırlar.

## Proje yapısı

| Dosya | Amaç |
| --- | --- |
| `main.py` | Tkinter arayüzü, kontroller, temalar ve geliştirici bağlantıları |
| `click_engine.py` | Windows girdi kancaları ve tıklama zamanlayıcısı |
| `settings.py` | Atomik JSON kaydıyla doğrulanan ayarlar |
| `create_icon.py`, `farland.ico` | Uygulama simgesi |
| `Farland Auto Clicker.spec` | PyInstaller derleme yapılandırması |
| `test_click_engine.py` | Zamanlayıcı ve girdi kancası davranış testleri |
| `docs/` | Japonca ve Farsça belgeler |

Sürüm ZIP dosyası mevcut Windows uygulamasını ve kaynak dosyaları içerir. Derleme önbellekleri ve geçici dosyalar pakete alınmaz.

## Testler

Windows'ta:

```powershell
py -B -m unittest -v test_click_engine
```

Bu testler simüle edilmiş bir tıklama göndericisi kullanır; gerçek fare tıklaması üretmez.

## Geliştirici

**Bardiya Alizadeh (Kabir) · Farland_game**

[GitHub portföyü](https://github.com/FarlandGame)

### Kanallar ve sosyal bağlantılar

| Platform | Kanallar / sayfalar |
| --- | --- |
| GitHub | [FarlandGame](https://github.com/FarlandGame) |
| YouTube | [Farland_game](https://www.youtube.com/@Farland_game) · [Farland_animation](https://www.youtube.com/@Farland_animation) |
| Rubika kanalları | [farland_gam](https://rubika.ir/farland_gam) · [Farland_animatio](https://rubika.ir/Farland_animatio) |
| Rubika sayfaları | [farland_game](https://rubika.ir/farland_game) · [Farland_animations](https://rubika.ir/Farland_animations) |
| Instagram | [farland_game](https://www.instagram.com/farland_game/) |
| Telegram kanalları | [Farland_gam](https://t.me/Farland_gam) · [Farland_animatio](https://t.me/Farland_animatio) |
| Twitch | [farlandgame](https://twitch.tv/farlandgame) |
| Kick | [farlandgame](https://kick.com/farlandgame) |
| Aparat | [Farland_Game](https://aparat.com/Farland_Game) |
| SoundCloud | [Bardiya Kabir](https://soundcloud.com/bardiya-kabir-798008614) |

### Telegram müzik botu

[Farland Music Bot](https://t.me/Farland_Music_bot) — Şarkıyı bulmak için şarkının video bağlantısını Telegram botumuza gönderin.

### Topluluk ve aile

- **THE APEX:** [YouTube](https://www.youtube.com/@THE_APEX_MC) · [Telegram](https://t.me/+-3uY7eIZArVjZDE0)
- **Manhunt:** [Telegram grubu](https://t.me/+DAq20XrkPyZhNjVk)
- **Kardeşimin kanalı:** [YouTube'da ArmiyaFabix](https://www.youtube.com/@ArmiyaFabix)

### Çalışmalarımı destekleyin

[Reymit üzerinden bağış yapın](https://reymit.ir/farland_game) ❤️
