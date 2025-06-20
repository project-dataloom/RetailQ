import pandas as pd
from pricing_agent.predict import predict_price

# Simulated pricing input for prediction
price_input = pd.DataFrame([{
    'Product ID': 101,
    'Store ID': 1,
    'Date': '2025-06-01',
    'Price': 0,  # Placeholder
    'Units Sold': 0,
    'Stock Remaining': 60,
    'Cost Price': 75.00,
    'Promotion': 1,
    'Competitor Price': 95.00,
    'Season': 'Summer'
}])

predicted = predict_price(price_input)
print(f"💰 Suggested Price: ₹{predicted[0]:.2f}")
