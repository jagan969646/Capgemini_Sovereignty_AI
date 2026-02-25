import pandas as pd
from datetime import datetime

def generate_executive_summary():
    df = pd.read_csv('data/processed_data.csv')
    
    # Calculate high-level KPIs
    total_savings = 417500.00 # From our ROI logic
    risk_exposure = 89045.11  # From our Stress Test
    efficiency_gain = "18.5%"
    
    report_content = f"""
    CAPGEMINI INVENT - AI SUPPLY CHAIN AUDIT
    Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}
    -------------------------------------------
    EXECUTIVE SUMMARY:
    - Projected Annual Savings: ${total_savings:,.2f}
    - Critical Risk Exposure: ${risk_exposure:,.2f}
    - Operational Efficiency Gain: {efficiency_gain}
    
    TOP RECOMMENDATION:
    Reallocate safety stock from North to Central hub to mitigate 
    port congestion risks identified by the ML Risk Engine.
    -------------------------------------------
    """
    
    with open("Executive_Summary.txt", "w") as f:
        f.write(report_content)
    
    print("📋 Owner-Level Report Generated: Executive_Summary.txt")

if __name__ == "__main__":
    generate_executive_summary()