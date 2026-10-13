# Farland_autcliker

[English](../README.md) | [日本語](README.ja.md) | [فارسی](README.fa.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Español](README.es.md) | [Português (Brasil)](README.pt-BR.md) | [Italiano](README.it.md) | [Nederlands](README.nl.md) | [Polski](README.pl.md) | [Українська](README.uk.md) | [Türkçe](README.tr.md) | [Русский](README.ru.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [한국어](README.ko.md) | [हिन्दी](README.hi.md) | [Bahasa Indonesia](README.id.md)

Un autoclicker para Windows en el que cada clic físico inicia una ráfaga independiente de clics adicionales durante un segundo, con controles separados para los botones izquierdo y derecho y una interfaz en persa.

**Creado por Bardiya Alizadeh (Kabir), conocido como Farland_game.**

**[Descargar el ZIP para Windows](https://github.com/FarlandGame/Farland_autcliker/releases/latest/download/Farland_autcliker.zip)** · [Todas las versiones](https://github.com/FarlandGame/Farland_autcliker/releases)

![Interfaz de Farland_autcliker](../preview.png)

Farland_autcliker es una aplicación de escritorio para Windows creada por **Bardiya Alizadeh (Kabir), conocido como Farland_game**. Su característica distintiva es cómo empieza la automatización: **cada clic físico del ratón inicia su propia ráfaga de clics adicionales durante un segundo**. Está diseñada para quienes quieren decidir cuándo empieza una ráfaga mediante sus propios clics, mientras controlan los botones izquierdo y derecho por separado. La aplicación combina este comportamiento con una interfaz en persa, controles personalizables, preferencias guardadas y un ejecutable para Windows listo para usar.

## Cómo tus clics se convierten en clics adicionales

Activa el autoclicker y después haz clic con el botón izquierdo o derecho. El clic físico original se envía normalmente y el programa programa clics adicionales para ese mismo botón durante el segundo siguiente. Por ejemplo, con el lado izquierdo configurado en **20 CPS**, un clic izquierdo físico programa **20 clics izquierdos adicionales**. Incluyendo el clic físico, esa interacción solicita 21 clics en total, sujetos al procesamiento de entradas de la aplicación de destino.

Un segundo clic físico inicia otra ráfaga, aunque la primera siga en marcha. Dos clics izquierdos de este tipo programan 40 clics adicionales a lo largo de sus intervalos de un segundo superpuestos. Por tanto, el ajuste describe **cada ráfaga individual**, no un límite global de toda la actividad superpuesta. Cuando no hay nuevos clics físicos, no se crean nuevas ráfagas; las que ya están programadas continúan hasta terminar o hasta que detengas el autoclicker.

## Qué distingue este funcionamiento

Un [funcionamiento habitual de repetición hasta detenerlo](https://www.opautoclicker.com/) ejecuta una secuencia repetida después de activarlo. Farland_autcliker se distingue por **las ráfagas activadas por clics físicos**, con ajustes separados para cada lado.

| Interacción | Repetición hasta detenerla | Farland_autcliker |
| --- | --- | --- |
| Iniciar clics adicionales | Iniciar la secuencia de repetición | Activar y después hacer clic físicamente |
| Un nuevo clic físico | No hace falta para mantener la repetición | Inicia su propia ráfaga adicional |
| Terminar una secuencia | Detener la secuencia de repetición | Cada ráfaga completa su programación de un segundo |

Esta comparación describe dos formas de funcionamiento; algunos autoclickers pueden ofrecer otros modos. Las ventajas documentadas de Farland son su forma de activación y sus controles independientes.

## Control independiente izquierdo y derecho

Establece una frecuencia diferente para cada botón, de **1 a 10.000 CPS**, y activa cada lado por separado. Por ejemplo, puedes configurar 20 CPS a la izquierda y 8 CPS a la derecha: un clic izquierdo inicia su ráfaga de clics izquierdos, mientras que uno derecho inicia una ráfaga independiente de clics derechos. Al desactivar un lado, sus clics físicos siguen funcionando normalmente sin crear nuevos clics adicionales.

## Controles adaptados a tu configuración

Activa o desactiva el programa con el botón principal de la interfaz o un atajo global elegido: el botón central del ratón, cualquiera de los dos botones laterales, F6–F9, Home, End o Insert. **F12** proporciona una parada de emergencia y cierra la aplicación. Cuatro temas —oscuro, claro, morado y azul— permiten elegir la apariencia. Las frecuencias de clic, los lados activados, el atajo y el tema se guardan para la siguiente sesión. Los valores de frecuencia no válidos vuelven al último valor válido.

## Tratamiento cuidadoso de las entradas repetidas

El motor distingue la entrada física del ratón de los clics inyectados por Windows, de modo que sus propios clics generados no inician nuevas ráfagas. Un planificador gestiona las ráfagas superpuestas y envía los clics de alta frecuencia en pequeños lotes. **10.000 CPS es el máximo configurable, no una garantía de velocidad medida**: la entrega real depende del ordenador, del procesamiento de entradas de Windows y de la aplicación de destino.

## Descargar y explorar

El ZIP público para Windows incluye el ejecutable, el código fuente, una vista previa de la interfaz y documentación en inglés, japonés y persa. Extráelo y abre `Farland-Auto-Clicker/dist/Farland Auto Clicker.exe`; el ejecutable empaquetado no necesita una instalación independiente de Python. El código fuente está dirigido a Windows 10 u 11 y Python 3.10 o posterior, y utiliza Tkinter y la API de Windows. El repositorio también incluye seis pruebas de planificación, superposición de lados, cancelación, atajos y filtrado de entradas inyectadas; utilizan clics simulados.

## Inicio rápido

1. Descarga y extrae `Farland_autcliker.zip`.
2. Abre `Farland-Auto-Clicker/dist/Farland Auto Clicker.exe`. La aplicación empaquetada no requiere una instalación independiente de Python.
3. Configura los clics por segundo (CPS) de los botones izquierdo y derecho y activa los lados que necesites.
4. Pulsa el botón central del ratón o el botón principal para activar el autoclicker.
5. Cada clic físico izquierdo o derecho inicia una ráfaga de clics adicionales para ese mismo botón durante el segundo siguiente.
6. Pulsa **F12** para detener todos los clics pendientes y salir.

## Controles y ajustes

| Control | Acción |
| --- | --- |
| Botón principal / atajo seleccionado | Activar o desactivar el autoclicker |
| F12 | Parada de emergencia y salida |
| Enter / salir de un campo CPS | Aplicar un valor válido de frecuencia de clic |

Una frecuencia de clic no válida vuelve a su valor anterior. Los ajustes se guardan en `%APPDATA%\Farland Auto Clicker\settings.json`.

## Ejecutar desde el código fuente

Requiere **Windows 10 u 11** y **Python 3.10 o posterior**, incluido Tkinter. No se necesita ningún paquete de terceros para ejecutar el código fuente.

```powershell
py main.py
```

## Crear el ejecutable de Windows

Desde el directorio del proyecto:

```powershell
py -m pip install -r requirements.txt
py create_icon.py
py -m PyInstaller --noconfirm --clean "Farland Auto Clicker.spec"
```

El resultado es `dist/Farland Auto Clicker.exe`. Para interactuar con una aplicación que se ejecuta como administrador, ejecuta el autoclicker con el mismo nivel de privilegios; Windows restringe la entrada a aplicaciones con privilegios superiores.

## Estructura del proyecto

| Archivo | Función |
| --- | --- |
| `main.py` | Interfaz Tkinter, controles, temas y enlaces del creador |
| `click_engine.py` | Hooks de entrada de Windows y planificador de clics |
| `settings.py` | Ajustes validados con guardado atómico de JSON |
| `create_icon.py`, `farland.ico` | Icono de la aplicación |
| `Farland Auto Clicker.spec` | Configuración de compilación de PyInstaller |
| `test_click_engine.py` | Pruebas de comportamiento del planificador y los hooks |
| `docs/` | Documentación en japonés y persa |

El ZIP de la versión publicada incluye el ejecutable de Windows existente y los archivos fuente. Se excluyen las cachés de compilación y los archivos temporales.

## Pruebas

En Windows:

```powershell
py -B -m unittest -v test_click_engine
```

Estas pruebas utilizan un emisor de clics simulado; no generan clics reales del ratón.

## Creador

**Bardiya Alizadeh (Kabir) · Farland_game**

[Portafolio de GitHub](https://github.com/FarlandGame)

### Canales y enlaces sociales

| Plataforma | Canales / páginas |
| --- | --- |
| GitHub | [FarlandGame](https://github.com/FarlandGame) |
| YouTube | [Farland_game](https://www.youtube.com/@Farland_game) · [Farland_animation](https://www.youtube.com/@Farland_animation) |
| Canales de Rubika | [farland_gam](https://rubika.ir/farland_gam) · [Farland_animatio](https://rubika.ir/Farland_animatio) |
| Páginas de Rubika | [farland_game](https://rubika.ir/farland_game) · [Farland_animations](https://rubika.ir/Farland_animations) |
| Instagram | [farland_game](https://www.instagram.com/farland_game/) |
| Canales de Telegram | [Farland_gam](https://t.me/Farland_gam) · [Farland_animatio](https://t.me/Farland_animatio) |
| Twitch | [farlandgame](https://twitch.tv/farlandgame) |
| Kick | [farlandgame](https://kick.com/farlandgame) |
| Aparat | [Farland_Game](https://aparat.com/Farland_Game) |
| SoundCloud | [Bardiya Kabir](https://soundcloud.com/bardiya-kabir-798008614) |

### Bot de música de Telegram

[Farland Music Bot](https://t.me/Farland_Music_bot) — Envía el enlace del vídeo de una canción a nuestro bot de Telegram para encontrar el tema.

### Comunidad y familia

- **THE APEX:** [YouTube](https://www.youtube.com/@THE_APEX_MC) · [Telegram](https://t.me/+-3uY7eIZArVjZDE0)
- **Manhunt:** [Grupo de Telegram](https://t.me/+DAq20XrkPyZhNjVk)
- **El canal de mi hermano:** [ArmiyaFabix en YouTube](https://www.youtube.com/@ArmiyaFabix)

### Apoya mi trabajo

[Donar mediante Reymit](https://reymit.ir/farland_game) ❤️
