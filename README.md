Proyecto de Machine Learning que usa XGBoost para predecir ventas semanales basadas en patrones historicos de precio y temporalidad con el Dataset de aguacate/palta.el objetivo es analizar la elasticidad precio-demanda observada en datos historicos para estimar el precio que maximiza ingresos en condiciones de mercado similares al periodo 2015-2017


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

## Resultados clave
- Precio optimo palta convencional (julio 2018): $1.62
- Precio optimo organico (julio 2018): $0.97
- Las simulaciones fuera de este rango no son confiables

## Estructura
```text
├── data/              # Datos csv
├── notebooks/         # Analisis
├── src/               # Codigos
└── README.md