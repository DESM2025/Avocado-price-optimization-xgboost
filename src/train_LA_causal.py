import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.metrics import mean_squared_error, mean_absolute_error
import joblib
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'avocado_processed_city.csv')
MODEL_DIR = os.path.join(BASE_DIR, 'models')
REGION = 'LosAngeles'

def train_model():
    
    df = pd.read_csv(DATA_PATH)
    df = df[df['region'] == REGION].copy()
    df['Date'] = pd.to_datetime(df['Date'])
    
    #feature 
    df['total'] = df.groupby('Date')['Volumen'].transform('sum') #suma de ventas totales por fecha
    df['escasez'] = df['month'].isin([9, 10]).astype(int) #meses donde mas subio el precio y probablemente hubo escasez
    FEATURES = ['month', 'week', 'type_organic', 'total', 'escasez']
    TARGET = 'Volumen'
    
    cutoff = '2018-01-01'
    train = df[df['Date'] < cutoff]
    test = df[df['Date'] >= cutoff]
    
    X_train = train[FEATURES]
    y_train = train[TARGET]
    X_test = test[FEATURES]
    y_test = test[TARGET]
    
    # train
    model = xgb.XGBRegressor(
        objective='reg:squarederror',
        n_estimators=1000,
        learning_rate=0.05,
        max_depth=6,
        early_stopping_rounds=50,
        n_jobs=-1,
        random_state=42
    )
    model.fit(X_train, y_train, eval_set=[(X_test, y_test)], verbose=50)
    
    # evaluacion
    preds = model.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, preds))
    mae = mean_absolute_error(y_test, preds)
    print(f"RMSE:{rmse:,.0f} | MAE: {mae:,.0f}")
    print(f"Error % aprox:{(mae / y_test.mean()) * 100:.2f}%")
    
    # validacion causalidad
    test_scarcity = test[test['escasez'] == 1]
    if len(test_scarcity) > 0:
        correlacion = test_scarcity['AVGPrice'].corr(test_scarcity['Volumen'])
        print(f"\ncorrelacion precio-demanda en meses de escasez: {correlacion:.2f}")
        print("(deberia ser negativa si el modelo captura elasticidad real)")
    
    os.makedirs(MODEL_DIR, exist_ok=True)
    model_path = os.path.join(MODEL_DIR, f'xgb_avocado_{REGION}_causal.pkl')
    joblib.dump(model, model_path)
    print(f"modelo guardado en {model_path}")

if __name__ == "__main__":
    train_model()