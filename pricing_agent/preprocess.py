import pandas as pd
from sklearn.preprocessing import LabelEncoder

def preprocess_pricing_data(df):
    df['Date'] = pd.to_datetime(df['Date'])
    df['DayOfWeek'] = df['Date'].dt.dayofweek
    df['Month'] = df['Date'].dt.month

    # Encode categorical features
    le = LabelEncoder()
    df['Season'] = le.fit_transform(df['Season'])

    features = ['Stock Remaining', 'Promotion', 'Cost Price',
                'Competitor Price', 'Season', 'DayOfWeek', 'Month']
    target = 'Price'

    X = df[features]
    y = df[target]

    return X, y
