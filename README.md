# Predicción de Incumplimiento de Pagos

Este proyecto tiene como objetivo desarrollar uno o varios modelos predictivos para determinar la probabilidad de que una cuenta entre en incumplimiento de pagos el próximo mes. Utilizaremos datos financieros históricos y la información del cliente para entrenar y evaluar el modelo.

## Descripción General del Proyecto

El objetivo principal de este proyecto es predecir si una cuenta de crédito entrará en incumplimiento de pago en el próximo mes. Para lograrlo, utilizaremos un conjunto de datos que contiene información sobre clientes y transacciones de tarjetas de crédito. Nuestro objetivo final es desarrollar un modelo predictivo preciso que pueda ser utilizado por las instituciones financieras para evaluar el riesgo crediticio y tomar decisiones informadas.

## Datos Utilizados

Utilizaremos el conjunto de datos "Default of Credit Card Clients" de UCI Machine Learning Repository. Este conjunto de datos contiene información sobre características demográficas de los clientes, como género, edad, nivel educativo, estado civil, así como datos financieros como límite de crédito, historial de pagos, montos de facturación y montos de pago. Estos datos nos proporcionarán información relevante para predecir el incumplimiento de pagos.

## Técnicas y Modelos Empleados

En este proyecto, emplearemos las siguientes técnicas y modelos:

- **Análisis Exploratorio de Datos**: Antes de construir el modelo predictivo, realizaremos un análisis en profundidad de los datos para comprender mejor las características, relaciones y distribuciones. Utilizaremos gráficos y estadísticas descriptivas para visualizar y resumir los datos.

- **Preprocesamiento de Datos**: Prepararemos los datos para el modelado, lo cual incluirá la limpieza de datos, la transformación de variables categóricas, el manejo de valores faltantes y la normalización de variables numéricas.

- **Modelado Predictivo**: Utilizaremos varios modelos de aprendizaje automático, como Regresión Logística, Random Forest, XGBoost u otros, para construir el modelo predictivo. Evaluararemos los modelos utilizando métricas de rendimiento como la precisión, el recall y el área bajo la curva ROC. Además, ajustaremos los hiperparámetros de los modelos para mejorar su rendimiento.

## Estructura del Proyecto

El proyecto se organiza de la siguiente manera:

![Estructura del proyecto](../data/img/Estructura.png)

- **data**: Carpeta que contiene los datos utilizados en el proyecto, incluyendo el archivo CSV con los datos de los clientes y las transacciones de tarjetas de crédito.

- **notebooks**: Carpeta que contiene los cuadernos Jupyter utilizados en el proyecto, incluyendo cuadernos para el preprocesamiento de datos, análisis exploratorio y modelado predictivo.

- **exploratory_analysis_report.pdf**: Informe generado durante el análisis exploratorio de los datos, que puede incluir gráficos y resultados relevantes del análisis.

- **trained_model.pkl**: Modelo entrenado guardado en formato pickle, que se puede cargar y utilizar para realizar predicciones.

- **README.md**: Este archivo que proporciona una descripción general del proyecto, su objetivo, los datos utilizados, las técnicas y modelos empleados, así como cualquier otra información relevante.

- **requirements.txt**: Archivo que lista las dependencias del proyecto, que se pueden instalar utilizando el comando `pip install -r requirements.txt`.


## Resultados de los Modelos

### Regresión Logística
- **Accuracy**: 0.8079946103750281
- **Confusion Matrix**:
[[6758 177]
[1533 438]]
- **Classification Report**:
          precision    recall  f1-score   support

       0       0.82      0.97      0.89      6935
       1       0.71      0.22      0.34      1971

accuracy                           0.81      8906
macro avg 0.76 0.60 0.61 8906
weighted avg 0.79 0.81 0.77 8906

### Random Forest
- **Accuracy**: 0.8120368291039749
- **Confusion Matrix**:


