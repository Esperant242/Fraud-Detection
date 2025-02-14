from flask import render_template, request
from app import app
import pickle
import numpy as np

# Charger le modèle et le scaler
with open('./models/xgb_model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

with open('./models/scaler.pkl', 'rb') as scaler_file:
    scaler = pickle.load(scaler_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        # Récupérer les données du formulaire
        data = request.form.to_dict()
        
        # Convertir les valeurs en float et les mettre dans l'ordre attendu par le modèle
        features = [
            float(data['V1']),
            float(data['V2']),
            float(data['V3']),
            float(data['V4']),
            float(data['V5']),
            float(data['V6']),
            float(data['V7']),
            float(data['V8']),
            float(data['V9']),
            float(data['V10']),
            float(data['V11']),
            float(data['V12']),
            float(data['V13']),
            float(data['V14']),
            float(data['V15']),
            float(data['V16']),
            float(data['V17']),
            float(data['V18']),
            float(data['V19']),
            float(data['V20']),
            float(data['V21']),
            float(data['V22']),
            float(data['V23']),
            float(data['V24']),
            float(data['V25']),
            float(data['V26']),
            float(data['V27']),
            float(data['V28']),
            float(data['Amount'])
        ]

        # Prétraiter les données avec le scaler
        features = scaler.transform([features])

        # Faire la prédiction
        prediction = model.predict(features)

        # Renvoyer le résultat
        return render_template('index.html', prediction_text=f'La prédiction est : {prediction[0]}')
    
    except ValueError:
        return render_template('index.html', prediction_text="Erreur : Veuillez entrer des nombres valides.")