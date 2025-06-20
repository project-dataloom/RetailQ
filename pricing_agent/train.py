import pandas as pd
import joblib
from sklearn.ensemble import RandomForestRegressor
from sklearn.model_selection import train_test_split
from pricing_agent.preprocess import preprocess_pricing_data

# Load dataset
df = pd.read_csv('data/pricing_data.csv')
X, y = preprocess_pricing_data(df)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train model
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# Save model
joblib.dump(model, 'models/pricing_model.pkl')
print("✅ Pricing model trained and saved.")
