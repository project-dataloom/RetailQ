import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_data(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df['DayOfWeek'] = df['Date'].dt.dayofweek
    df['Month'] = df['Date'].dt.month

    # Encode categorical features
    le = LabelEncoder()
    df['Weather'] = le.fit_transform(df['Weather'])

    features = ['Product ID', 'Store ID', 'Price', 'Promotion', 'Holiday',
                'Weather', 'Stock Available', 'DayOfWeek', 'Month']
    target = 'Units Sold'

    X = df[features]
    y = df[target]
    return X, y
