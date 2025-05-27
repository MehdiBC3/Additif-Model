# Additif-Model
📈 Modèle Additif de Prédiction des Ventes
Ce projet implémente un modèle additif de régression linéaire permettant de prédire les ventes mensuelles de maillots de bain à partir de données temporelles enrichies par des variables saisonnières (mois de l'année).

🗂️ Structure du projet

├── main.py                       # Script principal pour exécuter le projet
├── Additif.py                   # Implémentation du modèle de régression linéaire
├── data_preparation.py          # Prétraitement et transformation des données
├── vente_maillots_de_bain.csv   # Données de ventes avec date et ventes mensuelles
├── Projet-Maths.png             # Image du projet (visualisation ou illustration)

🧠 Objectif
L'objectif est d'appliquer un modèle additif basé sur la régression linéaire pour :

capturer la tendance temporelle via un index temporel,

intégrer la saisonnalité mensuelle avec des variables fictives (dummies),

évaluer les performances sur des ensembles d'entraînement et de test,

visualiser les prédictions avec un intervalle de confiance.

⚙️ Installation
Assurez-vous d'avoir les bibliothèques suivantes installées :

pip install numpy pandas matplotlib scikit-learn

▶️ Utilisation
Lancez le script principal :

python main.py

Ce script :

Charge et prépare les données depuis vente_maillots_de_bain.csv.

Sépare les données en entraînement/test avec codage des mois.

Entraîne un modèle de régression.

Affiche les erreurs absolues moyennes sur les jeux de train/test.

Génère une visualisation des ventes réelles vs prédites avec intervalle de confiance à 95 %.

📊 Données
Le fichier vente_maillots_de_bain.csv contient :

Years : dates mensuelles des mesures,

Sales : nombre de ventes par mois.

Un encodage one-hot est appliqué sur les mois (month_name) pour intégrer la saisonnalité dans le modèle.

📈 Modèle
Le modèle utilisé est une régression linéaire avec :

une variable temporelle (index_mesure) pour la tendance,

des variables catégorielles (month_name_...) pour la saisonnalité.

La performance est mesurée via l'erreur absolue moyenne (MAE) sur les ensembles de train/test.

Un intervalle de confiance (95%) est également tracé pour les prédictions sur l'ensemble de test.

🖼️ Visualisation
Le graphe final affiche :

![Projet-Maths](https://github.com/MehdiBC3/Additif-Model/assets/156785256/3faeecac-ae3c-4672-839a-dd3cc6b6cbcf)

Les ventes réelles (train/test),

Les prédictions du modèle,

L'intervalle de confiance sur les prédictions test.
