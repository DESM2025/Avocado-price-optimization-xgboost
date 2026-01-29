Proyecto de Machine Learning que usa XGBoost para predecir la demanda y optimizar precios en el Dataset de agucate/palta, el objetivo es encontrar la elasticidad precio de la demanda para maximizar los ingresos.

* Scripts en `src/` para descarga y limpieza de datos.
* Analisis Exploratorio: Deteccion de patrones y correccion de Double Counting en regiones geograficas
* Regresion con XGBoost para estimar ventas futuras basadas en precio y estacionalidad(en desarrollo)

Stack Tecnologico
* Python 3.12
* Librerias: Pandas, NumPy, XGBoost, Scikit-Learn, Matplotlib/Seaborn
* Herramientas: VS Code, Jupyter Notebooks
* Dataset original https://github.com/erkansirin78/datasets/blob/master/avocado.csv

## Crear entorno
* conda env create -f environment.yml
* conda activate dynamic_pricing

## Estructura
```text
├── data/              # Datos csv
├── notebooks/         # Analisis
├── src/               # Codigos
└── README.md
