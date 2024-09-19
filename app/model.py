# app/model.py

import pickle
import numpy as np
import pandas as pd
import os

class FraudDetectionModel:
    def __init__(self, model_path='models/xgb_model.pkl', scaler_path='models/scaler.pkl'):
        """
        Initialiser le modèle de détection de fraude en chargeant le modèle entraîné et le scaler.
        
        Args:
            model_path (str): Chemin vers le fichier du modèle entraîné.
            scaler_path (str): Chemin vers le fichier du scaler.
        """
        self.model_path = model_path
        self.scaler_path = scaler_path
        self.model = self.load_model()
        self.scaler = self.load_scaler()

    def load_model(self):
        """
        Charger le modèle entraîné depuis le disque.
        
        Returns:
            model: Modèle entraîné.
        """
        if not os.path.exists(self.model_path):
            raise FileNotFoundError(f"Le modèle n'a pas été trouvé à l'emplacement {self.model_path}")
        
        with open(self.model_path, 'rb') as file:
            model = pickle.load(file)
        return model

    def load_scaler(self):
        """
        Charger le scaler depuis le disque.
        
        Returns:
            scaler: Objet scaler entraîné.
        """
        if not os.path.exists(self.scaler_path):
            raise FileNotFoundError(f"Le scaler n'a pas été trouvé à l'emplacement {self.scaler_path}")
        
        with open(self.scaler_path, 'rb') as file:
            scaler = pickle.load(file)
        return scaler

    def preprocess(self, input_data):
        """
        Prétraiter les données d'entrée en appliquant le scaler.
        
        Args:
            input_data (dict or pandas.DataFrame): Données d'entrée pour la prédiction.
        
        Returns:
            numpy.ndarray: Données prétraitées prêtes pour la prédiction.
        """
        if isinstance(input_data, dict):
            input_df = pd.DataFrame([input_data])
        elif isinstance(input_data, pd.DataFrame):
            input_df = input_data
        else:
            raise ValueError("Les données d'entrée doivent être un dictionnaire ou un DataFrame pandas.")
        
        # Assurez-vous que les colonnes sont dans le bon ordre
        features = self.scaler.feature_names_in_ if hasattr(self.scaler, 'feature_names_in_') else input_df.columns
        input_df = input_df[features]
        
        # Appliquer le scaler
        input_scaled = self.scaler.transform(input_df)
        return input_scaled

    def predict(self, input_data):
        """
        Générer des prédictions pour les données d'entrée.
        
        Args:
            input_data (dict or pandas.DataFrame): Données d'entrée pour la prédiction.
        
        Returns:
            dict: Résultats des prédictions incluant la probabilité de fraude.
        """
        input_scaled = self.preprocess(input_data)
        prediction = self.model.predict(input_scaled)
        prediction_proba = self.model.predict_proba(input_scaled)[:, 1]  # Probabilité de classe 1 (fraude)
        
        result = {
            "prediction": int(prediction[0]),
            "probability": float(prediction_proba[0])
        }
        return result
