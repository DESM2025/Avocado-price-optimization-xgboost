import pandas as pd
import numpy as np
import xgboost as xgb
from sklearn.metrics import mean_squared_error, mean_absolute_error
import joblib
import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, 'data', 'avocado_processed_state.csv')
MODEL_DIR = os.path.join(BASE_DIR, 'models')
REGION = 'California'

def train_model():

    df= pd.read_csv(DATA_PATH)
    df = df[df['region'] == REGION].copy() #filtrar solo california

    #definir x features e y target
    FEATURES = ['AVGPrice', 'month', 'year', 'week', 'type_organic']
    TARGET = 'Volumen' # predecir volumen de ventas

    #train/test
    cutoff = '2018-01-01'
    train = df[df['Date'] < cutoff]
    test = df[df['Date'] >= cutoff] #tomar todo 2018 en test

    X_train = train[FEATURES]
    y_train = train[TARGET]
    X_test = test[FEATURES]
    y_test = test[TARGET]

    #train
    model = xgb.XGBRegressor(
        objective='reg:squarederror', #loss functiobn squarederrorMSE/squaredlogerror/absoluteerror
        n_estimators=1000, # arboles
        learning_rate=0.05,
        max_depth=6, #profundidad del arbol
        early_stopping_rounds=50,
        n_jobs=-1, #uso nucleos del cpu
        random_state=42 #semilla
    )

    #         (features,target,set evaluacion,verbose=50 cada 50 iteraciones)
    model.fit(X_train, y_train,eval_set=[(X_test, y_test)],verbose=50)
    
    #evaluacion
    preds = model.predict(X_test) #en los datos de test
    rmse = np.sqrt(mean_squared_error(y_test, preds)) #error cuadratico
    mae = mean_absolute_error(y_test, preds) #error absoluto medio
    print(f"RMSE:{rmse:,.0f} | MAE: {mae:,.0f}")
    print(f"Error % aprox:{(mae / y_test.mean()) * 100:.2f}%")

    os.makedirs(MODEL_DIR, exist_ok=True)
    model_path = os.path.join(MODEL_DIR, f'xgb_avocado_{REGION}.pkl')
    joblib.dump(model, model_path)
    print(f"modelo guardado en {model_path}")

if __name__ == "__main__":
    train_model()