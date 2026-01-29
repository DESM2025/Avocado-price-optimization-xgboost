import os
import requests

DATA_URL = "https://raw.githubusercontent.com/erkansirin78/datasets/master/avocado.csv"

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
RAW_PATH = os.path.join(BASE_DIR, 'data', 'avocado_raw.csv')
os.makedirs(os.path.dirname(RAW_PATH), exist_ok=True)

def download():
    response = requests.get(DATA_URL)
    response.raise_for_status()
            
    with open(RAW_PATH, 'wb') as f:
        f.write(response.content)
            
    print(f"archivo guardado en: {RAW_PATH}")

if __name__ == "__main__":
    download()