# Navigation par Familiarité

**Auteur :** Gabriel Gattaux — Aix-Marseille Université  
**Contact :** gabriel.gattaux@univ-amu.fr  
**Cours :** Navigation Visuelle Basée sur la Familiarité  
**TP :** 2/2  
**Dépôt :** https://github.com/Gaby-253/cours_navigation_familiarite_etudiant  
**Licence :** CC BY-NC 4.0  
**Dernière mise à jour :** 10/11/2025

[![Made by Gabriel Gattaux](https://img.shields.io/badge/made%20by-Gabriel%20Gattaux-0A66C2.svg)](#)
[![License](https://img.shields.io/badge/license-CC%20BY--NC%204.0-orange.svg)](#)
[![Python](https://img.shields.io/badge/python-3.10%2B-blue.svg)](#)

> Matériel pédagogique pour le cours sur la navigation visuelle par familiarité.  
> Merci de citer l’auteur et d’ouvrir une *issue* en cas de bug : `https://github.com/Gaby-253/cours_navigation_familiarite_etudiant/issues`.

## 🗂️ Contenu du dépôt

```
.
├─ TP1/                  # TP1.ipynb (+ éventuel code support non modifiable)
├─ data/                 # Dossier des données (à remplir après téléchargement)
├─ environment.yml       # Spécification de l'environnement Conda (usage local)
├─ Cours.pdf             # Support du cours
└─ README.md
```

## 📝 Description rapide

* **TP1 — Familiarité des vues**

---

## 📝 Rendu

* Envoyez moi vos notebook aprés compilation, au format html par mail.

---

## ▶️ Option A (Recommandé) — Exécuter en ligne (Google Colab)

Aucun prérequis local : ouvrez directement les notebooks dans le navigateur.

* **TP1A sur Colab** :
  [![Ouvrir TP1A dans Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Gaby-253/cours_navigation_familiarite_etudiant/blob/main/TP1/TP1A_garde_le_cap.ipynb)

* **TP1B sur Colab** :
  [![Ouvrir TP1B dans Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Gaby-253/cours_navigation_familiarite_etudiant/blob/main/TP1/TP1B_localiser_sur_route.ipynb)

* **TP2 sur Colab** :
  [![Ouvrir TP2 dans Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/github/Gaby-253/cours_navigation_familiarite_etudiant/blob/main/TP2/TP2_mushroombody.ipynb)

Dans **chaque notebook**, la **première cellule** télécharge et extrait automatiquement les données dans `../data/` à partir du lien ci-dessous.

> Si vous voyez une erreur liée aux paquets, relancez la cellule “setup” puis “Runtime > Restart session” et ré-exécutez le notebook.

---

## 💻 Option B — Exécuter en local (Conda)

### 🧰 Prérequis

* **Git**
* **Conda** (Miniconda recommandé)

  1. Téléchargez l’installateur Miniconda pour votre OS (Windows/macOS/Linux)
  2. Installez et acceptez l’ajout au `PATH`
  3. Redémarrez votre terminal

### ⚙️ Créer l’environnement

```bash
# Depuis la racine du dépôt
conda env create -f environment.yml -n familiarite_antnav
conda activate familiarite_antnav
```

> Alternative (plus rapide) avec **mamba** :
>
> ```bash
> mamba env create -f environment.yml -n familiarite_antnav
> mamba activate familiarite_antnav
> ```

---

## 🗃️ Données (pour Colab **et** local)

* **Téléchargement :** [Lien](https://filesender.renater.fr/download.php?token=ffab855e-64b5-4741-8519-51337987420d&files_ids=61990814)
* **Où placer ?** Extrayez **tout le contenu** directement dans `data/` (à la racine du projet).

### Exemples d’extraction (local)

* **Linux / macOS**

  ```bash
  # .zip
  unzip chemin/vers/donnees.zip -d data/
  # .tar.gz
  tar -xzf chemin/vers/donnees.tar.gz -C data/
  ```
* **Windows (PowerShell)**

  ```powershell
  Expand-Archive -Path "C:\chemin\donnees.zip" -DestinationPath ".\data"
  ```

> Vérifiez qu’après extraction, les fichiers attendus sont **directement** dans `data/` (pas de dossier imbriqué superflu).

---

## 🚀 Démarrage rapide (ordre conseillé)

### A) En ligne (Colab)

1. Cliquez sur le badge **Colab** (TP1A, TP1B ou TP2).
2. Exécutez la cellule **“téléchargement des données”**.
3. Commencez le TP.

### B) En local (Conda)

1. **Cloner le dépôt**

   ```bash
   git clone https://github.com/Gaby-253/cours_navigation_familiarite.git
   cd REPO
   ```
2. **Créer et activer l’environnement**

   ```bash
   conda env create -f environment.yml -n familiarite_antnav
   conda activate familiarite_antnav
   ```
3. **Télécharger les données** : **[LIEN À REMPLACER]**

4. **Extraire dans `data/`**

   ```bash
   unzip ~/Téléchargements/donnees.zip -d data/
   ```
5. **Ouvrir les notebooks**.

---

## 🧪 Vérification rapide

```bash
python -c "import pathlib; p=pathlib.Path('data'); print('OK data/', p.exists(), '->', [x.name for x in p.glob('*')][:5])"
```

Sortie attendue : `True` et aperçu de quelques fichiers/ dossiers présents dans `data/`.

---

## 🐛 Questions, retours, bugs

* **Parlez-moi directement** (cours)
* **Ouvrez une issue GitHub** : `https://github.com/Gaby-253/cours_navigation_familiarite/issues`
* **Écrivez-moi** : `gabriel.gattaux at univ-amu.fr`

Pour accélérer le support, indiquez :

* Le **TP** et l’**étape précise**,
* Votre **OS** et la **version Python**,
* Le **message d’erreur complet** (copier/coller).

---

## 📄 Licence

* **À REMPLACER** (ex. MIT, Apache-2.0, …)

---

### 📌 Notes

* `environment.yml` est dédié à l’usage **local** (Conda).
* Évitez de committer des données volumineuses : préférez le **téléchargement** depuis le notebook.
