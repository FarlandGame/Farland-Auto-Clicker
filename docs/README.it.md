# Farland_autcliker

[English](../README.md) | [日本語](README.ja.md) | [فارسی](README.fa.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Español](README.es.md) | [Português (Brasil)](README.pt-BR.md) | [Italiano](README.it.md) | [Nederlands](README.nl.md) | [Polski](README.pl.md) | [Українська](README.uk.md) | [Türkçe](README.tr.md) | [Русский](README.ru.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [한국어](README.ko.md) | [हिन्दी](README.hi.md) | [Bahasa Indonesia](README.id.md)

Un autoclicker per Windows in cui ogni clic fisico avvia una sequenza indipendente di clic aggiuntivi della durata di un secondo, con controlli separati per i pulsanti sinistro e destro e un'interfaccia in persiano.

**Creato da Bardiya Alizadeh (Kabir), conosciuto come Farland_game.**

**[Scarica lo ZIP per Windows](https://github.com/FarlandGame/Farland_autcliker/releases/latest/download/Farland_autcliker.zip)** · [Tutte le versioni](https://github.com/FarlandGame/Farland_autcliker/releases)

![Interfaccia di Farland_autcliker](../preview.png)

Farland_autcliker è un'applicazione desktop per Windows creata da **Bardiya Alizadeh (Kabir), conosciuto come Farland_game**. La sua caratteristica distintiva è il modo in cui inizia l'automazione: **ogni clic fisico del mouse avvia una propria sequenza di clic aggiuntivi della durata di un secondo**. È pensata per chi vuole decidere quando avviare una sequenza usando il proprio mouse, regolando i pulsanti sinistro e destro indipendentemente. L'applicazione combina questo comportamento con un'interfaccia in persiano, controlli personalizzabili, preferenze salvate e un eseguibile Windows pronto all'uso.

## Come i tuoi clic diventano clic aggiuntivi

Attiva l'autoclicker, quindi fai clic con il pulsante sinistro o destro del mouse. Il clic fisico originale viene trasmesso normalmente e il programma pianifica clic aggiuntivi per lo stesso pulsante durante il secondo successivo. Per esempio, con il lato sinistro impostato a **20 CPS**, un clic sinistro fisico pianifica **20 clic sinistri aggiuntivi**. Compreso il clic fisico, questa interazione richiede 21 clic in totale, subordinatamente alla gestione degli input da parte dell'applicazione di destinazione.

Un secondo clic fisico avvia un'altra sequenza, anche se la prima è ancora in corso. Due clic sinistri di questo tipo pianificano 40 clic aggiuntivi nell'arco delle rispettive finestre di un secondo, che si sovrappongono. L'impostazione descrive quindi **ogni singola sequenza**, non un limite globale per tutte le attività sovrapposte. Se non vengono effettuati nuovi clic fisici, non vengono create nuove sequenze; quelle già pianificate continuano fino al completamento o finché non arresti l'autoclicker.

## Cosa distingue questo funzionamento

Un [funzionamento comune con ripetizione fino all'arresto](https://www.opautoclicker.com/) esegue una sequenza ripetuta dopo l'attivazione. Farland_autcliker si distingue per **le sequenze attivate dai clic fisici**, con impostazioni separate per ciascun lato.

| Interazione | Ripetizione fino all'arresto | Farland_autcliker |
| --- | --- | --- |
| Avviare clic aggiuntivi | Avviare la sequenza di ripetizione | Attivare e poi fare clic fisicamente |
| Un nuovo clic fisico | Non serve per continuare la ripetizione | Avvia una propria sequenza aggiuntiva |
| Terminare una sequenza | Arrestare la sequenza di ripetizione | Ogni sequenza completa la propria pianificazione di un secondo |

Questo confronto descrive due modalità di funzionamento; i singoli autoclicker possono offrire altre modalità. I punti di forza documentati di Farland sono il comportamento di attivazione e i controlli indipendenti.

## Controllo indipendente dei pulsanti sinistro e destro

Imposta una frequenza diversa per ogni pulsante, da **1 a 10.000 CPS**, e attiva ciascun lato separatamente. Per esempio, puoi configurare 20 CPS a sinistra e 8 CPS a destra: un clic sinistro avvia una sequenza per il pulsante sinistro, mentre un clic destro avvia una sequenza indipendente per il pulsante destro. Disattivando un lato, i suoi clic fisici continuano a funzionare normalmente senza creare nuovi clic aggiuntivi.

## Controlli adatti alla tua configurazione

Attiva o disattiva il programma con il pulsante principale dell'interfaccia oppure con un tasto rapido globale a scelta: pulsante centrale del mouse, uno dei due pulsanti laterali, F6–F9, Home, End o Insert. **F12** fornisce un arresto di emergenza e chiude l'applicazione. Quattro temi — scuro, chiaro, viola e blu — consentono di scegliere l'aspetto. Frequenze di clic, lati attivati, tasto rapido e tema vengono salvati per la sessione successiva. I valori non validi della frequenza di clic tornano all'ultimo valore valido.

## Gestione attenta degli input ripetuti

Il motore distingue gli input fisici del mouse dai clic iniettati da Windows, così i clic generati dal programma non avviano nuove sequenze. Uno scheduler gestisce le sequenze sovrapposte e invia i clic ad alta frequenza in piccoli gruppi. **10.000 CPS è il limite configurabile, non una garanzia di velocità misurata**: l'invio effettivo dipende dal computer, dall'elaborazione degli input di Windows e dall'applicazione di destinazione.

## Scaricare ed esplorare

Lo ZIP pubblico per Windows include l'eseguibile, il codice sorgente, un'anteprima dell'interfaccia e documentazione in inglese, giapponese e persiano. Estrailo e apri `Farland-Auto-Clicker/dist/Farland Auto Clicker.exe`; l'eseguibile incluso non richiede un'installazione separata di Python. Il codice sorgente è destinato a Windows 10 o 11 e Python 3.10 o successivo e usa Tkinter e l'API Windows. Il repository include inoltre sei test per la pianificazione, la sovrapposizione dei lati, l'annullamento, i tasti rapidi e il filtraggio degli input iniettati; utilizzano clic simulati.

## Avvio rapido

1. Scarica ed estrai `Farland_autcliker.zip`.
2. Apri `Farland-Auto-Clicker/dist/Farland Auto Clicker.exe`. L'applicazione inclusa nel pacchetto non richiede un'installazione separata di Python.
3. Imposta i clic al secondo (CPS) per sinistra e destra e attiva i lati che ti servono.
4. Premi il pulsante centrale del mouse o il pulsante principale per attivare l'autoclicker.
5. Ogni clic fisico sinistro o destro avvia una sequenza di clic aggiuntivi per lo stesso pulsante durante il secondo successivo.
6. Premi **F12** per arrestare tutti i clic in attesa e uscire.

## Controlli e impostazioni

| Controllo | Azione |
| --- | --- |
| Pulsante principale / tasto rapido selezionato | Attivare o disattivare l'autoclicker |
| F12 | Arresto di emergenza e uscita |
| Invio / uscita da un campo CPS | Applicare un valore valido della frequenza di clic |

Una frequenza di clic non valida torna al valore precedente. Le impostazioni sono memorizzate in `%APPDATA%\Farland Auto Clicker\settings.json`.

## Eseguire dal codice sorgente

Richiede **Windows 10 o 11** e **Python 3.10 o successivo**, incluso Tkinter. Per eseguire il codice sorgente non è necessario alcun pacchetto di terze parti.

```powershell
py main.py
```

## Creare l'eseguibile Windows

Dalla cartella del progetto:

```powershell
py -m pip install -r requirements.txt
py create_icon.py
py -m PyInstaller --noconfirm --clean "Farland Auto Clicker.spec"
```

Il risultato è `dist/Farland Auto Clicker.exe`. Per interagire con un'applicazione eseguita come amministratore, avvia l'autoclicker con lo stesso livello di privilegi; Windows limita gli input verso applicazioni con privilegi superiori.

## Struttura del progetto

| File | Funzione |
| --- | --- |
| `main.py` | Interfaccia Tkinter, controlli, temi e collegamenti del creatore |
| `click_engine.py` | Hook di input di Windows e scheduler dei clic |
| `settings.py` | Impostazioni validate con salvataggi JSON atomici |
| `create_icon.py`, `farland.ico` | Icona dell'applicazione |
| `Farland Auto Clicker.spec` | Configurazione di compilazione di PyInstaller |
| `test_click_engine.py` | Test del comportamento di scheduler e hook |
| `docs/` | Documentazione in giapponese e persiano |

Lo ZIP della versione pubblicata include l'eseguibile Windows esistente e i file sorgente. Sono esclusi le cache di compilazione e i file temporanei.

## Test

Su Windows:

```powershell
py -B -m unittest -v test_click_engine
```

Questi test usano un generatore di clic simulato; non producono clic reali del mouse.

## Creatore

**Bardiya Alizadeh (Kabir) · Farland_game**

[Portfolio GitHub](https://github.com/FarlandGame)

### Canali e collegamenti social

| Piattaforma | Canali / pagine |
| --- | --- |
| GitHub | [FarlandGame](https://github.com/FarlandGame) |
| YouTube | [Farland_game](https://www.youtube.com/@Farland_game) · [Farland_animation](https://www.youtube.com/@Farland_animation) |
| Canali Rubika | [farland_gam](https://rubika.ir/farland_gam) · [Farland_animatio](https://rubika.ir/Farland_animatio) |
| Pagine Rubika | [farland_game](https://rubika.ir/farland_game) · [Farland_animations](https://rubika.ir/Farland_animations) |
| Instagram | [farland_game](https://www.instagram.com/farland_game/) |
| Canali Telegram | [Farland_gam](https://t.me/Farland_gam) · [Farland_animatio](https://t.me/Farland_animatio) |
| Twitch | [farlandgame](https://twitch.tv/farlandgame) |
| Kick | [farlandgame](https://kick.com/farlandgame) |
| Aparat | [Farland_Game](https://aparat.com/Farland_Game) |
| SoundCloud | [Bardiya Kabir](https://soundcloud.com/bardiya-kabir-798008614) |

### Bot musicale di Telegram

[Farland Music Bot](https://t.me/Farland_Music_bot) — Invia il collegamento al video di una canzone al nostro bot di Telegram per trovare il brano.

### Comunità e famiglia

- **THE APEX:** [YouTube](https://www.youtube.com/@THE_APEX_MC) · [Telegram](https://t.me/+-3uY7eIZArVjZDE0)
- **Manhunt:** [Gruppo Telegram](https://t.me/+DAq20XrkPyZhNjVk)
- **Il canale di mio fratello:** [ArmiyaFabix su YouTube](https://www.youtube.com/@ArmiyaFabix)

### Sostieni il mio lavoro

[Dona tramite Reymit](https://reymit.ir/farland_game) ❤️
