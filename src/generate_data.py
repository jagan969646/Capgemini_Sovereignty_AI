import pandas as pd
import numpy as np
from datetime import datetime, timedelta
import os

def generate_retail_data(rows=1000):
    np.random.seed(42)
    
    # 1. Generate Basic Info
    categories = ['Electronics', 'Office Supplies', 'Furniture', 'Technology']
    regions = ['North', 'South', 'East', 'West', 'Central']
    
    data = {
        'order_id': [f'ORD-{1000+i}' for i in range(rows)],
        'order_date': [datetime(2023, 1, 1) + timedelta(days=np.random.randint(0, 365)) for i in range(rows)],
        'category': [np.random.choice(categories) for _ in range(rows)],
        'region': [np.random.choice(regions) for _ in range(rows)],
        'sales': np.random.uniform(100, 5000, rows).round(2),
        'quantity': np.random.randint(1, 15, rows),
        'discount': np.random.choice([0, 0.1, 0.2, 0.3], rows),
        'lead_time': np.random.randint(1, 12, rows) 
    }
    
    df = pd.DataFrame(data)
    
    # 2. Add Business Logic (Consulting Style)
    # Calculate Profit based on Category and Discount
    df['cost'] = df['sales'] * np.random.uniform(0.5, 0.8, rows)
    df['profit'] = (df['sales'] - df['cost']) - (df['sales'] * df['discount'])
    
    # 3. Add "Inventory" columns for your AI to analyze
    # Renamed to 'current_stock' to match common ERP systems
    df['current_stock'] = np.random.randint(5, 100, rows)
    
    # Ensuring 'data' directory exists
    os.makedirs('data', exist_ok=True)
    
    # Save to your data folder
    df.to_csv('data/raw_orders.csv', index=False)
    print("✅ Success: data/raw_orders.csv generated with Lead Time metrics.")

if __name__ == "__main__":
    generate_retail_data()