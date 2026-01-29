import pandas as pd
import os
import io
import requests

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_DIR = os.path.join(BASE_DIR, 'data')
FILE_PATH = os.path.join(DATA_DIR, 'avocado_raw.csv')
PROCESSED_PATH = os.path.join(DATA_DIR, 'avocado_processed.csv') 

def get_avocado_data():

    df = pd.read_csv(FILE_PATH)
        
    if len(df) > 0:
        print(f"se cargo {len(df)} filas crudas.")
    else:
        print("no se cargaron datos")
        return

    #estandarizar fecha para xgboost
    df['Date'] = pd.to_datetime(df['Date']) 
        
    # renombrar columnas para comodidad
    df = df.rename(columns={
        'AveragePrice': 'AVGPrice',
        'Total Volume': 'Volumen',
        '4046': 'Palta_pequeña',
        '4225': 'Palta_mediana',
        '4770': 'Palta_grande',
        'Small Bags': 'S_Bags',
        'Large Bags': 'L_Bags',
        'XLarge Bags': 'XL_Bags'
    })

    # filtrar la columna inutil unnamed
    if 'Unnamed: 0' in df.columns: df = df.drop(columns=['Unnamed: 0'])

    # ordenar por fecha 
    df = df.sort_values(by=['Date', 'region'])
 
    #eliminar reguiones que no sean ciudades
    eliminar = ['TotalUS','California','GreatLakes','Midsouth','Northeast','NorthernNewEngland','Plains','SouthCarolina','SouthCentral','Southeast','West','WestTexNewMexico']
    df = df[~df['region'].isin(eliminar)]

    if not os.path.exists(DATA_DIR): os.makedirs(DATA_DIR)
    # guardar en un csv sin perder el original
    df.to_csv(PROCESSED_PATH, index=False)
    print(f"datos guardados en: {PROCESSED_PATH}")
    print(df.head(3)) 

if __name__ == "__main__":
    get_avocado_data()