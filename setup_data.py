import os
import pandas as pd

def fix_and_process():
    data_dir = 'data'
    files = os.listdir(data_dir)
    print(f"Files found in data folder: {files}")

    orders_file = None
    returns_file = None

    # Find the files regardless of the long names
    for f in files:
        if 'Orders' in f and f.endswith('.csv'):
            orders_file = f
        if 'Returns' in f and f.endswith('.csv'):
            returns_file = f

    if not orders_file or not returns_file:
        print("❌ Error: Could not find Orders or Returns CSV in the data folder!")
        return

    print(f"✅ Found Orders: {orders_file}")
    print(f"✅ Found Returns: {returns_file}")

    # Load and process
    orders = pd.read_csv(os.path.join(data_dir, orders_file), encoding='latin1')
    returns = pd.read_csv(os.path.join(data_dir, returns_file), encoding='latin1')

    # Merging
    df = pd.merge(orders, returns.drop(columns=['Market'], errors='ignore'), on='Order ID', how='left')
    df['Returned'] = df['Returned'].fillna('No')
    
    # Ensure Profit is numeric
    df['Profit'] = pd.to_numeric(df['Profit'], errors='coerce').fillna(0)
    df['Actual_Profit'] = df.apply(lambda x: 0 if x['Returned'] == 'Yes' else x['Profit'], axis=1)

    # Save the file that the ML model is looking for
    output_path = os.path.join(data_dir, 'processed_data.csv')
    df.to_csv(output_path, index=False)
    print(f"🚀 SUCCESS! Created {output_path}")

if __name__ == "__main__":
    fix_and_process()