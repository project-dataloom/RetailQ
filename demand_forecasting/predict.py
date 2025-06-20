import pandas as pd
import joblib
from demand_forecasting.preprocess import preprocess_data

def predict(input_df):
    model = joblib.load('models/demand_forecast_model.pkl')
    X, _ = preprocess_data(input_df)
    predictions = model.predict(X)
    return predictions
