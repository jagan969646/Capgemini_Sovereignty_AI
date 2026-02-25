import os
import pandas as pd
from dotenv import load_dotenv
# If you are using the Mock version for the interview:
from ai_consultant import run_consultant 

load_dotenv()

def start_agent():
    print(f"🚀 Project {os.getenv('PROJECT_NAME')} is running in {os.getenv('ENVIRONMENT')} mode.")
    
    # Check if data exists
    if os.path.exists('data/processed_data.csv'):
        print("🔍 Data found. Starting analysis...")
        # This calls the logic we tested earlier
        run_consultant() 
    else:
        print("❌ Error: processed_data.csv missing. Run data_engine.py first.")

if __name__ == "__main__":
    start_agent()