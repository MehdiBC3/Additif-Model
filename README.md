# Additif-Model

📈 **Modèle Additif de Prédiction des Ventes**

Ce projet implémente un **modèle additif de régression linéaire** permettant de prédire les ventes mensuelles de maillots de bain à partir de données temporelles enrichies par des variables saisonnières (mois de l'année).

---

## 🗂️ Structure du projet

* `main.py` — Script principal pour exécuter le projet
* `Additif.py` — Implémentation du modèle de régression linéaire
* `data_preparation.py` — Prétraitement et transformation des données
* `vente_maillots_de_bain.csv` — Données de ventes mensuelles
* `Projet-Maths.png` — Illustration du projet (graphe ou résumé visuel)

---

## 🧠 Objectif

Ce projet vise à :

* Capturer la **tendance temporelle** via un index numérique,
* Intégrer la **saisonnalité mensuelle** à l’aide de variables fictives (one-hot encoding),
* Évaluer la performance sur des ensembles **d'entraînement** et **de test**,
* Visualiser les prédictions avec un **intervalle de confiance** à 95 %.

---

## ⚙️ Installation

Installez les bibliothèques nécessaires avec :

```bash
pip install numpy pandas matplotlib scikit-learn
```

---

## ▶️ Utilisation

Lancez simplement le script principal :

```bash
python main.py
```

Ce script :

* Charge et prépare les données à partir de `vente_maillots_de_bain.csv`,
* Sépare les données en train/test avec codage des mois,
* Entraîne un modèle de régression linéaire,
* Affiche les **erreurs absolues moyennes** sur les jeux de données,
* Génère une **visualisation** des prédictions avec un intervalle de confiance.

---

## 📊 Données

Le fichier `vente_maillots_de_bain.csv` contient :

* `Years` : dates mensuelles des mesures,
* `Sales` : nombre de ventes par mois.

Un encodage **one-hot** est appliqué sur la colonne `month_name` pour modéliser la saisonnalité.

---

## 📈 Modèle

Le modèle est une **régression linéaire additive** utilisant :

* Une variable temporelle : `index_mesure`,
* Des variables catégorielles : `month_name_...`.

La performance est mesurée par l’**erreur absolue moyenne (MAE)** sur les ensembles d'entraînement et de test.
Un **intervalle de confiance** à 95 % est également tracé sur les prédictions de test.

---

## 🖼️ Visualisation

Le graphe final montre :

* Les ventes réelles (train et test),
* Les prédictions du modèle,
* L’**intervalle de confiance** sur les prédictions test.

![Projet-Maths](https://github.com/MehdiBC3/Additif-Model/assets/156785256/3faeecac-ae3c-4672-839a-dd3cc6b6cbcf)
