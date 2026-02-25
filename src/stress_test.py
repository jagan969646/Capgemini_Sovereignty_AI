import pandas as pd
import numpy as np

def run_scenario_simulation():
    df = pd.read_csv('data/processed_data.csv')
    
    print("\n" + "="*40)
    print("🚩 SCENARIO: 50% SUPPLY CHAIN DISRUPTION")
    print("="*40)
    
    # Simulate a crisis: Lead times double, Costs rise by 20%
    df['crisis_lead_time'] = df['lead_time'] * 2
    df['crisis_safety_stock'] = (df['crisis_lead_time'] * 1.5).astype(int)
    
    # Calculate "Stockout Exposure"
    exposed_items = df[df['current_stock'] < df['crisis_safety_stock']]
    financial_risk = (exposed_items['sales'].sum() * 0.25).round(2)
    
    print(f"Items at Risk: {len(exposed_items)} SKU units")
    print(f"Potential Revenue Loss: ${financial_risk:,.2f}")
    print(f"Mitigation Strategy: Pre-emptive restocking in {df['region'].iloc[0]} required.")
    print("="*40)

if __name__ == "__main__":
    run_scenario_simulation()