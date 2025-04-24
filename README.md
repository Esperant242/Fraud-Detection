# 🕵️‍♂️ Détection de fraude par carte bancaire

Ce projet vise à détecter des transactions frauduleuses à l’aide de techniques avancées de data science. Il combine visualisation, prétraitement, modélisation supervisée (XGBoost), non supervisée (Isolation Forest), et optimisation d'hyperparamètres (Hyperopt).

## 📊 Objectifs

- Analyser et visualiser des transactions bancaires
- Prétraiter les données pour améliorer la qualité des modèles
- Identifier les transactions frauduleuses en utilisant des approches supervisées et non supervisées
- Optimiser les performances des modèles via Hyperopt
- Évaluer la robustesse et l’interprétabilité des résultats

## 🧰 Technologies utilisées

- Python 3.10+
- Pandas, NumPy
- Seaborn, Matplotlib
- Scikit-learn
- XGBoost
- Hyperopt
- Imbalanced-learn (SMOTE)

## ⚙️ Pipeline

1. **Exploration des données**
   - Analyse exploratoire (EDA)
   - Visualisation des variables principales
2. **Prétraitement**
   - Standardisation
   - Rééquilibrage des classes avec SMOTE
3. **Modélisation**
   - Modèles supervisés : XGBoost
   - Modèles non supervisés : Isolation Forest
4. **Optimisation**
   - Hyperopt pour la recherche d’hyperparamètres
5. **Évaluation**
   - Matrice de confusion, courbe ROC, AUC
   - Interprétation des résultats avec importance des variables

## 📁 Structure du projet

```bash
fraud_detection/
│
├── notebooks/            # Notebooks d'analyse et de modélisation
├── models/               # Modèles entraînés
├── requirements.txt      # Dépendances du projet
└── README.md             # Ce fichier
