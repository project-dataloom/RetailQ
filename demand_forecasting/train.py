import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from demand_forecasting.preprocess import preprocess_data

# Load data
df = pd.read_csv('data/demand_data.csv')

# Preprocess
X, y = preprocess_data(df)

# Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'models/demand_forecast_model.pkl')
print("✅ Model trained and saved.")
