import pandas as pd
import os
import requests
from typing import Optional

def download_data(url: str, save_path: str) -> None:
    """
    Downloads data from a URL and saves it to a specified file path.
    
    Args:
    - url: str, the URL to download the data from.
    - save_path: str, the path to save the downloaded file.
    """
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for HTTP errors
        with open(save_path, 'wb') as file:
            file.write(response.content)
        print(f"Data successfully downloaded and saved to {save_path}")
    except Exception as e:
        print(f"Error downloading data: {e}")

def load_data(filepath: str) -> Optional[pd.DataFrame]:
    """
    Loads data from a CSV file into a pandas DataFrame.
    
    Args:
    - filepath: str, the path to the CSV file.
    
    Returns:
    - pd.DataFrame or None: The loaded DataFrame, or None if an error occurred.
    """
    try:
        data = pd.read_csv(filepath)
        return data
    except Exception as e:
        print(f"Error loading data: {e}")
        return None

# Specify the URL and the local file path
url = 'https://raw.githubusercontent.com/plotly/datasets/master/finance-charts-apple.csv'
save_path = 'data/finance_charts_apple.csv'

# Create the data directory if it doesn't exist
os.makedirs(os.path.dirname(save_path), exist_ok=True)

# Download the data
download_data(url, save_path)

# Load the data
data = load_data(save_path)
if data is not None:
    print(data.head())
else:
    print("Failed to load data.")
