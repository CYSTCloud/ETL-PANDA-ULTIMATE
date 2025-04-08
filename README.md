
# ETL Projet Pandémies

Ce projet implémente un processus ETL (Extract, Transform, Load) complet pour l'analyse des données de pandémies, notamment COVID-19 et MPOX.

## Prérequis

### Environnement
- Python 3.8 ou supérieur
- MySQL 8.0 ou supérieur
- Jupyter Notebook

### Installation

1. Cloner le dépôt :
   ```bash
   git clone https://github.com/CYSTCloud/ETL-PANDA-ULTIMATE.git
   cd ETL-PANDA-ULTIMATE
   ```

2. Installer les dépendances :
   ```bash
   pip install -r requirements.txt
   ```

3. Configurer la base de données MySQL :
   - Créer une base de données nommée `epiviz`
   - Les paramètres de connexion peuvent être modifiés dans le fichier `config.py`

4. Télécharger les données brutes :
   - Placer les fichiers CSV sources dans le dossier `donnees/brutes/`
   - Sources des données :
     - COVID-19 : [JHU CSSE COVID-19 Data](https://github.com/CSSEGISandData/COVID-19)
     - MPOX : [Our World in Data - Monkeypox](https://github.com/owid/monkeypox)
     - Worldometer : [Worldometer Coronavirus](https://www.worldometers.info/coronavirus/)

## Structure du projet

```
ETL_Projet_Pandemies/
├── donnees/
│   ├── brutes/             # Données brutes (fichiers CSV sources)
│   ├── intermediaires/     # Données extraites et nettoyées
│   └── transformees/       # Tables normalisées prêtes pour le chargement
├── notebooks/
│   ├── extraction/         # Notebooks pour l'extraction des données
│   ├── transformation/     # Notebooks pour la transformation des données
│   └── chargement/         # Notebooks pour le chargement des données
└── README.md               # Documentation du projet
```

## Processus ETL

### 1. Extraction

Cette étape consiste à extraire les données brutes des fichiers CSV sources :
- `covid_19_clean_complete.csv` : Données COVID-19
- `owid-monkeypox-data.csv` : Données MPOX
- `worldometer_coronavirus_daily_data.csv` : Données COVID-19 quotidiennes

Les notebooks d'extraction se trouvent dans le dossier `notebooks/extraction/`.

### 2. Transformation

Cette étape consiste à transformer les données extraites :

1. **Nettoyage des données** :
   - Conversion des dates
   - Gestion des valeurs manquantes
   - Standardisation des formats

2. **Suppression des doublons** :
   - Élimination des entrées en double par pays et date

3. **Agrégation des données** (étape cruciale souvent oubliée) :
   - Regroupement des données par pays et date
   - Calcul des sommes pour les métriques numériques

4. **Normalisation des données** :
   - Création des tables selon le schéma epiviz :
     - `calendrier` : Table des dates
     - `localisation` : Table des pays et continents
     - `pandemie` : Table des types de pandémies
     - `donnees` : Table principale avec les métriques

Les notebooks de transformation se trouvent dans le dossier `notebooks/transformation/`.

### 3. Chargement

Cette étape consiste à charger les données transformées dans la base de données MySQL :

1. **Préparation de la base de données** :
   - Désactivation temporaire des contraintes de clé étrangère
   - Vidage des tables existantes

2. **Chargement des données** :
   - Chargement par lots dans l'ordre des dépendances :
     1. `calendar`
     2. `location`
     3. `pandemie`
     4. `data`

3. **Vérification des données** :
   - Contrôle du nombre d'entrées dans chaque table
   - Exemples de requêtes pour vérifier la cohérence des données

Les notebooks de chargement se trouvent dans le dossier `notebooks/chargement/`.

## Points critiques à ne pas oublier

1. **Agrégation des données** : Cette étape est cruciale pour réduire le volume et préparer les données à la normalisation.

2. **Gestion des contraintes de clé étrangère** : Désactiver temporairement les contraintes avant de vider les tables pour éviter les erreurs de référence.

3. **Conversion des types de données** : Convertir explicitement les types NumPy en types Python standard pour éviter les erreurs avec MySQL Connector.

4. **Ordre des opérations** : Respecter l'ordre logique du processus ETL - Extraction → Nettoyage → Suppression des doublons → Agrégation → Normalisation → Chargement.

5. **Validation des données** : Toujours vérifier les données chargées pour s'assurer qu'elles sont correctes et cohérentes.

## Configuration de la base de données

Les paramètres de connexion à la base de données sont :
- Nom de la base de données : epiviz
- Utilisateur : root
- Mot de passe : (aucun)
- Hôte : localhost
- Port : 3306

## Structure de la base de données

La base de données epiviz a une structure relationnelle avec les tables principales suivantes :
1. `calendar` - stocke les dates
2. `location` - stocke les pays et continents
3. `pandemie` - stocke les types de pandémies
4. `data` - table principale qui stocke les données de cas avec des clés étrangères vers les autres tables
