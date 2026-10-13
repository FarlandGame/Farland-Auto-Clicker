# Farland_autcliker

[English](../README.md) | [日本語](README.ja.md) | [فارسی](README.fa.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Español](README.es.md) | [Português (Brasil)](README.pt-BR.md) | [Italiano](README.it.md) | [Nederlands](README.nl.md) | [Polski](README.pl.md) | [Українська](README.uk.md) | [Türkçe](README.tr.md) | [Русский](README.ru.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [한국어](README.ko.md) | [हिन्दी](README.hi.md) | [Bahasa Indonesia](README.id.md)

Um autoclicker para Windows em que cada clique físico inicia uma sequência independente de cliques adicionais durante um segundo, com controles separados para os botões esquerdo e direito e uma interface em persa.

**Criado por Bardiya Alizadeh (Kabir), conhecido como Farland_game.**

**[Baixar o ZIP para Windows](https://github.com/FarlandGame/Farland_autcliker/releases/latest/download/Farland_autcliker.zip)** · [Todas as versões](https://github.com/FarlandGame/Farland_autcliker/releases)

![Interface do Farland_autcliker](../preview.png)

Farland_autcliker é um aplicativo de desktop para Windows criado por **Bardiya Alizadeh (Kabir), conhecido como Farland_game**. Sua característica principal é a forma como a automação começa: **cada clique físico do mouse inicia sua própria sequência de cliques adicionais durante um segundo**. Ele foi desenvolvido para quem deseja decidir quando uma sequência começa por meio dos próprios cliques, mantendo o controle independente dos botões esquerdo e direito. O aplicativo combina esse comportamento com uma interface em persa, controles personalizáveis, preferências salvas e um executável para Windows pronto para usar.

## Como seus cliques se tornam cliques adicionais

Ative o autoclicker e depois clique com o botão esquerdo ou direito do mouse. O clique físico original é enviado normalmente, e o programa agenda cliques adicionais para esse mesmo botão durante o segundo seguinte. Por exemplo, com o lado esquerdo configurado para **20 CPS**, um clique esquerdo físico agenda **20 cliques esquerdos adicionais**. Contando o clique físico, essa interação solicita 21 cliques no total, sujeitos ao processamento de entrada do aplicativo de destino.

Um segundo clique físico inicia outra sequência, mesmo se a primeira ainda estiver em execução. Dois cliques esquerdos desse tipo agendam 40 cliques adicionais ao longo de seus intervalos de um segundo que se sobrepõem. Isso significa que a configuração descreve **cada sequência individual**, e não um limite global para toda a atividade sobreposta. Quando não há novos cliques físicos, não são criadas novas sequências; as já agendadas continuam até terminar ou até você parar o autoclicker.

## O que diferencia esse funcionamento

Um [funcionamento conhecido de repetição até ser interrompido](https://www.opautoclicker.com/) executa uma sequência repetida após a ativação. O diferencial do Farland_autcliker são **as sequências acionadas por cliques físicos**, com configurações separadas para cada lado.

| Interação | Repetição até ser interrompida | Farland_autcliker |
| --- | --- | --- |
| Iniciar cliques adicionais | Iniciar a sequência de repetição | Ativar e depois clicar fisicamente |
| Um novo clique físico | Não é necessário para manter a repetição | Inicia sua própria sequência adicional |
| Encerrar uma sequência | Parar a sequência de repetição | Cada sequência conclui seu agendamento de um segundo |

Esta comparação descreve duas formas de funcionamento; autoclickers individuais podem oferecer modos adicionais. Os pontos fortes documentados do Farland são a forma de acionamento e os controles independentes.

## Controle independente dos lados esquerdo e direito

Defina uma frequência diferente para cada botão, de **1 a 10.000 CPS**, e ative cada lado separadamente. Por exemplo, você pode configurar 20 CPS à esquerda e 8 CPS à direita: um clique esquerdo inicia sua sequência de cliques esquerdos, enquanto um clique direito inicia uma sequência independente de cliques direitos. Desativar um lado mantém seus cliques físicos funcionando normalmente, sem criar novos cliques adicionais.

## Controles que se adaptam à sua configuração

Ative ou desative o programa pelo botão principal da interface ou por um atalho global escolhido: botão do meio do mouse, qualquer um dos dois botões laterais, F6–F9, Home, End ou Insert. **F12** fornece uma parada de emergência e fecha o aplicativo. Quatro temas — escuro, claro, roxo e azul — permitem escolher a aparência. As frequências de clique, os lados ativados, o atalho e o tema são salvos para a próxima sessão. Valores de frequência inválidos voltam ao último valor válido.

## Tratamento cuidadoso das entradas repetidas

O mecanismo distingue as entradas físicas do mouse dos cliques injetados pelo Windows, para que seus próprios cliques gerados não iniciem novas sequências. Um agendador gerencia as sequências sobrepostas e envia cliques de alta frequência em pequenos lotes. **10.000 CPS é o limite configurável, não uma garantia de velocidade medida**: a entrega real depende do computador, do processamento de entrada do Windows e do aplicativo de destino.

## Baixar e explorar

O ZIP público para Windows inclui o executável, o código-fonte, uma prévia da interface e documentação em inglês, japonês e persa. Extraia-o e abra `Farland-Auto-Clicker/dist/Farland Auto Clicker.exe`; o executável empacotado não precisa de uma instalação separada do Python. O código-fonte é voltado para Windows 10 ou 11 e Python 3.10 ou posterior, usando Tkinter e a API do Windows. O repositório também inclui seis testes de agendamento, sobreposição dos lados, cancelamento, atalhos e filtragem de entradas injetadas; eles usam cliques simulados.

## Início rápido

1. Baixe e extraia `Farland_autcliker.zip`.
2. Abra `Farland-Auto-Clicker/dist/Farland Auto Clicker.exe`. O aplicativo empacotado não exige uma instalação separada do Python.
3. Defina os cliques por segundo (CPS) dos botões esquerdo e direito e ative os lados necessários.
4. Pressione o botão do meio do mouse ou o botão principal para ativar o autoclicker.
5. Cada clique físico esquerdo ou direito inicia uma sequência de cliques adicionais para esse mesmo botão durante o segundo seguinte.
6. Pressione **F12** para parar todos os cliques pendentes e sair.

## Controles e configurações

| Controle | Ação |
| --- | --- |
| Botão principal / atalho selecionado | Ativar ou desativar o autoclicker |
| F12 | Parada de emergência e saída |
| Enter / sair de um campo CPS | Aplicar um valor válido de frequência de clique |

Uma frequência de clique inválida volta ao valor anterior. As configurações são armazenadas em `%APPDATA%\Farland Auto Clicker\settings.json`.

## Executar pelo código-fonte

Requer **Windows 10 ou 11** e **Python 3.10 ou posterior**, incluindo Tkinter. Nenhum pacote de terceiros é necessário para executar o código-fonte.

```powershell
py main.py
```

## Gerar o executável para Windows

No diretório do projeto:

```powershell
py -m pip install -r requirements.txt
py create_icon.py
py -m PyInstaller --noconfirm --clean "Farland Auto Clicker.spec"
```

O arquivo gerado é `dist/Farland Auto Clicker.exe`. Para interagir com um aplicativo executado como administrador, execute o autoclicker com o mesmo nível de privilégios; o Windows restringe a entrada em aplicativos com privilégios mais altos.

## Estrutura do projeto

| Arquivo | Finalidade |
| --- | --- |
| `main.py` | Interface Tkinter, controles, temas e links do criador |
| `click_engine.py` | Hooks de entrada do Windows e agendador de cliques |
| `settings.py` | Configurações validadas com gravações atômicas de JSON |
| `create_icon.py`, `farland.ico` | Ícone do aplicativo |
| `Farland Auto Clicker.spec` | Configuração de compilação do PyInstaller |
| `test_click_engine.py` | Testes do comportamento do agendador e dos hooks |
| `docs/` | Documentação em japonês e persa |

O ZIP da versão publicada inclui o executável existente para Windows e os arquivos-fonte. Caches de compilação e arquivos temporários são excluídos.

## Testes

No Windows:

```powershell
py -B -m unittest -v test_click_engine
```

Esses testes usam um emissor de cliques simulado; eles não geram cliques reais do mouse.

## Criador

**Bardiya Alizadeh (Kabir) · Farland_game**

[Portfólio no GitHub](https://github.com/FarlandGame)

### Canais e links sociais

| Plataforma | Canais / páginas |
| --- | --- |
| GitHub | [FarlandGame](https://github.com/FarlandGame) |
| YouTube | [Farland_game](https://www.youtube.com/@Farland_game) · [Farland_animation](https://www.youtube.com/@Farland_animation) |
| Canais no Rubika | [farland_gam](https://rubika.ir/farland_gam) · [Farland_animatio](https://rubika.ir/Farland_animatio) |
| Páginas no Rubika | [farland_game](https://rubika.ir/farland_game) · [Farland_animations](https://rubika.ir/Farland_animations) |
| Instagram | [farland_game](https://www.instagram.com/farland_game/) |
| Canais no Telegram | [Farland_gam](https://t.me/Farland_gam) · [Farland_animatio](https://t.me/Farland_animatio) |
| Twitch | [farlandgame](https://twitch.tv/farlandgame) |
| Kick | [farlandgame](https://kick.com/farlandgame) |
| Aparat | [Farland_Game](https://aparat.com/Farland_Game) |
| SoundCloud | [Bardiya Kabir](https://soundcloud.com/bardiya-kabir-798008614) |

### Bot de música no Telegram

[Farland Music Bot](https://t.me/Farland_Music_bot) — Envie o link do vídeo de uma música ao nosso bot do Telegram para encontrar a faixa.

### Comunidade e família

- **THE APEX:** [YouTube](https://www.youtube.com/@THE_APEX_MC) · [Telegram](https://t.me/+-3uY7eIZArVjZDE0)
- **Manhunt:** [Grupo no Telegram](https://t.me/+DAq20XrkPyZhNjVk)
- **Canal do meu irmão:** [ArmiyaFabix no YouTube](https://www.youtube.com/@ArmiyaFabix)

### Apoie meu trabalho

[Doe pelo Reymit](https://reymit.ir/farland_game) ❤️
