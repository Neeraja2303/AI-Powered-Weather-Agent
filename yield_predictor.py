import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

def train_model(data_path='data/crop_yield_data.csv'):
    df = pd.read_csv(data_path)
    X = df[['rainfall', 'temperature', 'soil_nitrogen', 'ph']]
    y = df['yield_kg_per_hectare']

    model = RandomForestRegressor()
    model.fit(X, y)
    joblib.dump(model, 'model/trained_model.pkl')
    return model

import joblib

def predict_yield(rainfall, temperature, nitrogen, ph):
    model = joblib.load('model/trained_model.pkl')  # Make sure path is correct
    features = [[rainfall, temperature, nitrogen, ph]]
    prediction = model.predict(features)
    return prediction[0]
