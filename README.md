Proyecto de Machine Learning que usa XGBoost para predecir ventas semanales basadas en patrones historicos de precio y temporalidad con el Dataset de aguacate/palta. El objetivo es analizar la elasticidad precio-demanda observada en datos historicos para estimar el precio que maximiza ingresos en condiciones de mercado similares al periodo 2015-2017
Se incluye un modelo causal que reemplaza el precio por un proxy de oferta disponible para separar el efecto real de la oferta sobre las ventas del efecto aparente del precio

* Scripts en `src/` para descarga y limpieza de datos.
* Analisis Exploratorio: Deteccion de patrones y correccion de Double Counting en regiones geograficas
* Regresion con XGBoost para estimar ventas futuras basadas en precio y estacionalidad
* Inferencia causal: comparacion entre modelo original y modelo sin precio como feature

Stack Tecnologico
* Python 3.10
* Librerias: Pandas, NumPy, XGBoost, Scikit-Learn, Matplotlib/Seaborn
* Herramientas: VS Code, Jupyter Notebooks
* Dataset original https://github.com/erkansirin78/datasets/blob/master/avocado.csv

## Crear entorno
* conda env create -f environment.yml
* conda activate dynamic_pricing

## Resultados clave
- Precio optimo palta convencional (julio 2018): $1.62
- Precio optimo organico (julio 2018): $0.97
- Las simulaciones fuera de este rango no son confiables
- El modelo causal (MAE 12,301) predice mejor que el original (MAE 32,707) sin usar precio como variable
- La caida de ventas en septiembre y octubre se explica por restricciones de oferta externas en esos meses, no por el precio alto

## Estructura
```text
├── data/              # Datos csv
├── notebooks/         # Analisis
├── src/               # Codigos
└── README.md