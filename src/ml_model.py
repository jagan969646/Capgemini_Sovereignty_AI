import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

def train_restock_predictor():
    df = pd.read_csv('data/processed_data.csv')
    
    # Features: Sales, Quantity, Discount, and Current Stock
    X = df[['sales', 'quantity', 'discount', 'current_stock']]
    y = df['restock_needed'].apply(lambda x: 1 if x == 'Yes' else 0)
    
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
    
    model = RandomForestClassifier()
    model.fit(X_train, y_train)
    
    predictions = model.predict(X_test)
    print(f"🤖 Model Accuracy: {accuracy_score(y_test, predictions) * 100:.2f}%")
    return model

if __name__ == "__main__":
    train_restock_predictor()