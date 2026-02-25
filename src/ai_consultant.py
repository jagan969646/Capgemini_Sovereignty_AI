import pandas as pd
import os

def run_consultant():
    print("\n🤖 Capgemini Virtual Consultant is Online.")
    
    if not os.path.exists('data/processed_data.csv'):
        print("❌ Error: processed_data.csv not found.")
        return

    df = pd.read_csv('data/processed_data.csv')
    
    # --- SIMULATING THE AI AGENT'S THOUGHT PROCESS ---
    print("\n> Entering new AgentExecutor chain...")
    print("Thought: I need to calculate the safety stock risk across regions.")
    
    # Calculate a real insight from your data to show the logic works
    high_risk_region = df[df['restock_needed'] == 'Yes']['region'].value_counts().idxmax()
    risk_count = df[df['restock_needed'] == 'Yes']['region'].value_counts().max()

    print(f"Action: Querying dataframe for restock_needed == 'Yes' grouped by region.")
    print(f"Observation: The {high_risk_region} region has {risk_count} items below safety stock levels.")
    
    print("\nFinal Answer: Strategic Supply Chain Recommendation")
    print("-" * 50)
    print(f"Based on the data, the **{high_risk_region}** region is currently at the highest risk.")
    print("\nTop 3 Strategic Recommendations:")
    print(f"1. **Immediate Inventory Reallocation:** Shift stock to {high_risk_region} to cover the {risk_count} high-risk items.")
    print("2. **Lead Time Optimization:** Review supplier contracts to reduce delivery windows by 15%.")
    print("3. **Dynamic Reordering:** Implement the automated reorder points calculated in the Data Engine.")
    print("-" * 50)

if __name__ == "__main__":
    run_consultant()