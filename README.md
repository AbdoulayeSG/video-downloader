# 👻 Video Downloader

Une application de bureau simple, rapide et sans prise de tête pour télécharger des vidéos depuis le web, propulsée par **yt-dlp** et une interface graphique **Tkinter**.

![Python](https://img.shields.io/badge/Python-3.12-blue?logo=python)
![Platform](https://img.shields.io/badge/Platform-Linux-informational?logo=linux)
![License](https://img.shields.io/badge/License-MIT-green)

---

## ✨ Aperçu

Colle un lien, choisis un dossier, clique — et ta vidéo est téléchargée. Pas besoin de retenir des commandes en ligne, tout se passe dans une fenêtre simple et sombre.

---

## 🚀 Fonctionnalités

- 🔗 Téléchargement de vidéos à partir d'un simple lien
- 📁 Choix du dossier de destination
- ⚙️ Vérifie automatiquement si `yt-dlp` est installé, et l'installe si besoin
- 🎨 Interface sombre, légère et sans dépendances lourdes
- 🌍 Compatible avec des centaines de sites (pas seulement YouTube) grâce à `yt-dlp`

---

## 🛠️ Prérequis

| Outil | Requis |
|---|---|
| Python 3.8+ | ✅ |
| `yt-dlp` | Installé automatiquement au premier lancement si absent |
| Linux (testé sur Linux Mint) | ✅ |

---

## 📦 Installation

Clone le projet, puis lance-le directement — aucune dépendance externe à installer manuellement grâce au module `tkinter` inclus dans Python.

```bash
git clone <lien-du-repo>
cd video-downloader
python3 interfacev1.py
```

> 💡 Si `tkinter` n'est pas installé sur ta machine :
> ```bash
> sudo apt install python3-tk
> ```

---

## 🎮 Utilisation

1. Lance l'application :
   ```bash
   python3 interfacev1.py
   ```
2. Colle le **lien de la vidéo** dans le champ correspondant
3. Colle le **chemin du dossier** où tu veux enregistrer la vidéo
4. Clique sur **"ok!"**
5. Le téléchargement démarre — la vidéo apparaît dans le dossier choisi 🎉

---

## 📂 Structure du projet

```
video-downloader/
├── interfacev1.py     # Point d'entrée de l'application
├── logo.png           # Icône de l'application
└── README.md          # Ce fichier
```

---

## 🧩 Comment ça marche

L'application repose sur deux briques principales :

- **Tkinter** pour l'interface graphique (champs, boutons, fenêtre)
- **yt-dlp** en arrière-plan (via `subprocess`) pour effectuer le téléchargement réel de la vidéo

Au clic sur le bouton, l'app vérifie la présence de `yt-dlp`, l'installe si nécessaire, se positionne dans le dossier choisi, puis lance le téléchargement avec le nom original de la vidéo.

---

## 🗺️ Roadmap

- [ ] Bouton "Parcourir" pour choisir le dossier via une fenêtre système
- [ ] Barre de progression pendant le téléchargement
- [ ] Choix du format (vidéo / audio uniquement)
- [ ] Gestion des erreurs affichée dans l'interface (lien invalide, dossier introuvable, etc.)
- [ ] Compilation en exécutable autonome avec PyInstaller

---

## ⚖️ Avertissement

Cet outil est destiné à un usage personnel et légal. Assure-toi de respecter les conditions d'utilisation des plateformes ainsi que les droits d'auteur des contenus que tu télécharges.

---

## 📜 Licence

Ce projet est distribué sous licence MIT — libre à toi de l'utiliser, le modifier et le partager.
