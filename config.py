"""
Configuration globale pour le projet ETL Pandémies
"""

# Chemins des dossiers de données
CHEMINS = {
    "DONNEES_BRUTES": "./donnees/brutes/",
    "DONNEES_INTERMEDIAIRES": "./donnees/intermediaires/",
    "DONNEES_TRANSFORMEES": "./donnees/transformees/"
}

# Fichiers sources
FICHIERS_SOURCES = {
    "COVID19": "covid_19_clean_complete.csv",
    "MPOX": "owid-monkeypox-data.csv",
    "WORLDOMETER": "worldometer_coronavirus_daily_data.csv"
}

# Configuration de la base de données
DB_CONFIG = {
    "host": "localhost",
    "user": "root",
    "password": "",
    "database": "epiviz",
    "port": 3306
}

# Paramètres de transformation
PARAMETRES_TRANSFORMATION = {
    "FORMAT_DATE": "%Y-%m-%d",
    "COLONNES_NUMERIQUES": ["Confirmed", "Deaths", "Recovered", "Active", "New_cases", "New_deaths"],
    "VALEUR_MANQUANTE": 0
}

# Structure des tables
STRUCTURE_TABLES = {
    "calendar": ["date_id", "date", "year", "month", "day"],
    "location": ["location_id", "country", "province", "continent", "latitude", "longitude", "who_region"],
    "pandemie": ["pandemie_id", "nom", "description"],
    "data": ["data_id", "date_id", "location_id", "pandemie_id", "confirmed", "deaths", "recovered", "active", "new_cases", "new_deaths"]
}
