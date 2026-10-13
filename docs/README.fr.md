# Farland_autcliker

[English](../README.md) | [日本語](README.ja.md) | [فارسی](README.fa.md) | [Deutsch](README.de.md) | [Français](README.fr.md) | [Español](README.es.md) | [Português (Brasil)](README.pt-BR.md) | [Italiano](README.it.md) | [Nederlands](README.nl.md) | [Polski](README.pl.md) | [Українська](README.uk.md) | [Türkçe](README.tr.md) | [Русский](README.ru.md) | [简体中文](README.zh-CN.md) | [繁體中文](README.zh-TW.md) | [한국어](README.ko.md) | [हिन्दी](README.hi.md) | [Bahasa Indonesia](README.id.md)

Un autoclicker pour Windows où chaque clic physique déclenche une rafale indépendante de clics supplémentaires pendant une seconde, avec des réglages distincts pour les boutons gauche et droit et une interface en persan.

**Créé par Bardiya Alizadeh (Kabir), connu sous le nom de Farland_game.**

**[Télécharger le ZIP pour Windows](https://github.com/FarlandGame/Farland_autcliker/releases/latest/download/Farland_autcliker.zip)** · [Toutes les versions](https://github.com/FarlandGame/Farland_autcliker/releases)

![Interface de Farland_autcliker](../preview.png)

Farland_autcliker est une application de bureau Windows créée par **Bardiya Alizadeh (Kabir), connu sous le nom de Farland_game**. Sa particularité tient à la manière dont l'automatisation commence : **chaque clic physique de la souris déclenche sa propre rafale de clics supplémentaires pendant une seconde**. Elle s'adresse aux personnes qui veulent décider du début d'une rafale avec leur propre souris, tout en réglant les boutons gauche et droit indépendamment. L'application associe ce fonctionnement à une interface en persan, des commandes personnalisables, des préférences enregistrées et un exécutable Windows prêt à l'emploi.

## Comment vos clics deviennent des clics supplémentaires

Activez l'autoclicker, puis cliquez avec le bouton gauche ou droit de la souris. Le clic physique initial est transmis normalement, et le programme programme des clics supplémentaires pour ce même bouton pendant la seconde suivante. Par exemple, si le côté gauche est réglé sur **20 CPS**, un clic gauche physique programme **20 clics gauches supplémentaires**. En comptant le clic physique, cette interaction demande 21 clics au total, sous réserve du traitement des entrées par l'application cible.

Un deuxième clic physique déclenche une autre rafale, même si la première est encore en cours. Deux clics gauches de ce type programment 40 clics supplémentaires sur leurs fenêtres d'une seconde qui se chevauchent. Le réglage décrit donc **chaque rafale individuelle**, et non une limite globale de toutes les activités simultanées. Sans nouveau clic physique, aucune nouvelle rafale n'est créée ; les rafales déjà programmées continuent jusqu'à leur fin ou jusqu'à l'arrêt de l'autoclicker.

## Ce qui distingue ce fonctionnement

Un [fonctionnement classique avec répétition jusqu'à l'arrêt](https://www.opautoclicker.com/) exécute une séquence répétée après activation. Farland_autcliker se distingue par **des rafales déclenchées par les clics physiques**, avec des réglages séparés pour chaque côté.

| Interaction | Répétition jusqu'à l'arrêt | Farland_autcliker |
| --- | --- | --- |
| Déclencher des clics supplémentaires | Lancer la séquence répétée | Activer, puis cliquer physiquement |
| Nouveau clic physique | Pas nécessaire pour poursuivre la répétition | Déclenche sa propre rafale supplémentaire |
| Terminer une séquence | Arrêter la séquence répétée | Chaque rafale termine sa programmation d'une seconde |

Cette comparaison décrit deux modes de fonctionnement ; certains autoclickers peuvent proposer d'autres modes. Les points forts documentés de Farland sont son mode de déclenchement et ses commandes indépendantes.

## Réglage indépendant des boutons gauche et droit

Réglez une fréquence différente pour chaque bouton, de **1 à 10 000 CPS**, et activez chaque côté séparément. Vous pouvez par exemple régler 20 CPS à gauche et 8 CPS à droite : un clic gauche déclenche sa rafale de clics gauches, tandis qu'un clic droit déclenche une rafale indépendante de clics droits. Désactiver un côté laisse ses clics physiques fonctionner normalement, sans créer de nouveaux clics supplémentaires.

## Des commandes adaptées à votre configuration

Activez ou désactivez l'autoclicker avec le bouton principal de l'interface ou un raccourci global choisi : bouton central de la souris, l'un des deux boutons latéraux, F6–F9, Home, End ou Insert. **F12** assure l'arrêt d'urgence et ferme l'application. Quatre thèmes — sombre, clair, violet et bleu — permettent de choisir l'apparence. Les fréquences de clic, les côtés activés, le raccourci et le thème sont enregistrés pour la session suivante. Une fréquence de clic invalide est remplacée par la dernière valeur valide.

## Un traitement maîtrisé des entrées répétées

Le moteur distingue les entrées physiques de la souris des clics injectés par Windows, afin que ses propres clics ne déclenchent pas de nouvelles rafales. Un ordonnanceur gère les rafales qui se chevauchent et envoie les clics à haute fréquence par petits lots. **10 000 CPS est le plafond configurable, pas une garantie de vitesse mesurée** : le nombre de clics effectivement transmis dépend de l'ordinateur, du traitement des entrées de Windows et de l'application cible.

## Télécharger et découvrir

Le ZIP public pour Windows contient l'exécutable, le code source, un aperçu de l'interface et de la documentation en anglais, japonais et persan. Extrayez-le, puis ouvrez `Farland-Auto-Clicker/dist/Farland Auto Clicker.exe` ; cet exécutable ne nécessite pas d'installation distincte de Python. Le code source vise Windows 10 ou 11 et Python 3.10 ou version ultérieure, avec Tkinter et l'API Windows. Le dépôt contient aussi six tests portant sur l'ordonnancement, le chevauchement des côtés, l'annulation, les raccourcis et le filtrage des entrées injectées ; ils utilisent des clics simulés.

## Démarrage rapide

1. Téléchargez et extrayez `Farland_autcliker.zip`.
2. Ouvrez `Farland-Auto-Clicker/dist/Farland Auto Clicker.exe`. L'application empaquetée ne nécessite pas d'installation distincte de Python.
3. Réglez les clics par seconde (CPS) pour la gauche et la droite, puis activez les côtés souhaités.
4. Appuyez sur le bouton central de la souris ou sur le bouton principal pour activer l'autoclicker.
5. Chaque clic physique gauche ou droit déclenche des clics supplémentaires pour ce même bouton pendant la seconde suivante.
6. Appuyez sur **F12** pour arrêter tous les clics en attente et quitter.

## Commandes et paramètres

| Commande | Action |
| --- | --- |
| Bouton principal / raccourci choisi | Activer ou désactiver l'autoclicker |
| F12 | Arrêt d'urgence et fermeture |
| Entrée / quitter un champ CPS | Appliquer une fréquence de clic valide |

Une fréquence de clic invalide revient à sa valeur précédente. Les paramètres sont enregistrés dans `%APPDATA%\Farland Auto Clicker\settings.json`.

## Exécuter le code source

Nécessite **Windows 10 ou 11** et **Python 3.10 ou version ultérieure**, avec Tkinter. Aucun paquet tiers n'est nécessaire pour exécuter le code source.

```powershell
py main.py
```

## Construire l'exécutable Windows

Depuis le répertoire du projet :

```powershell
py -m pip install -r requirements.txt
py create_icon.py
py -m PyInstaller --noconfirm --clean "Farland Auto Clicker.spec"
```

Le fichier produit est `dist/Farland Auto Clicker.exe`. Pour interagir avec une application exécutée en tant qu'administrateur, lancez l'autoclicker au même niveau de privilèges ; Windows restreint les entrées destinées aux applications disposant de privilèges supérieurs.

## Structure du projet

| Fichier | Rôle |
| --- | --- |
| `main.py` | Interface Tkinter, commandes, thèmes et liens du créateur |
| `click_engine.py` | Hooks d'entrée Windows et ordonnanceur des clics |
| `settings.py` | Paramètres validés avec sauvegardes JSON atomiques |
| `create_icon.py`, `farland.ico` | Icône de l'application |
| `Farland Auto Clicker.spec` | Configuration de compilation PyInstaller |
| `test_click_engine.py` | Tests du comportement de l'ordonnanceur et des hooks |
| `docs/` | Documentation en japonais et en persan |

Le ZIP de la version publiée contient l'exécutable Windows existant et les fichiers sources. Les caches de compilation et les fichiers temporaires en sont exclus.

## Tests

Sous Windows :

```powershell
py -B -m unittest -v test_click_engine
```

Ces tests utilisent un émetteur de clics simulé ; ils ne produisent pas de vrais clics de souris.

## Créateur

**Bardiya Alizadeh (Kabir) · Farland_game**

[Portfolio GitHub](https://github.com/FarlandGame)

### Chaînes et réseaux sociaux

| Plateforme | Chaînes / pages |
| --- | --- |
| GitHub | [FarlandGame](https://github.com/FarlandGame) |
| YouTube | [Farland_game](https://www.youtube.com/@Farland_game) · [Farland_animation](https://www.youtube.com/@Farland_animation) |
| Chaînes Rubika | [farland_gam](https://rubika.ir/farland_gam) · [Farland_animatio](https://rubika.ir/Farland_animatio) |
| Pages Rubika | [farland_game](https://rubika.ir/farland_game) · [Farland_animations](https://rubika.ir/Farland_animations) |
| Instagram | [farland_game](https://www.instagram.com/farland_game/) |
| Chaînes Telegram | [Farland_gam](https://t.me/Farland_gam) · [Farland_animatio](https://t.me/Farland_animatio) |
| Twitch | [farlandgame](https://twitch.tv/farlandgame) |
| Kick | [farlandgame](https://kick.com/farlandgame) |
| Aparat | [Farland_Game](https://aparat.com/Farland_Game) |
| SoundCloud | [Bardiya Kabir](https://soundcloud.com/bardiya-kabir-798008614) |

### Bot musical Telegram

[Farland Music Bot](https://t.me/Farland_Music_bot) — Envoyez le lien vidéo d'une chanson à notre bot Telegram pour retrouver le morceau.

### Communauté et famille

- **THE APEX :** [YouTube](https://www.youtube.com/@THE_APEX_MC) · [Telegram](https://t.me/+-3uY7eIZArVjZDE0)
- **Manhunt :** [Groupe Telegram](https://t.me/+DAq20XrkPyZhNjVk)
- **La chaîne de mon frère :** [ArmiyaFabix sur YouTube](https://www.youtube.com/@ArmiyaFabix)

### Soutenir mon travail

[Faire un don via Reymit](https://reymit.ir/farland_game) ❤️
