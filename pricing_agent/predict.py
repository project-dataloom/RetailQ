import pandas as pd
import joblib
from pricing_agent.preprocess import preprocess_pricing_data

def predict_price(input_df):
    model = joblib.load('models/pricing_model.pkl')
    X, _ = preprocess_pricing_data(input_df)
    predicted_price = model.predict(X)
    return predicted_price
