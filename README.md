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


## Análisis de los Resultados

### Distribución del incumplimiento de pago próximo mes

La siguiente gráfica muestra la distribución de las cuentas según el incumplimiento de pago próximo mes:

![Incumplimiento de pago próximo mes](../data/img/incumplimiento.png)

Podemos observar que la mayoría de las cuentas no entran en incumplimiento el próximo mes, mientras que una proporción más pequeña sí entra en incumplimiento.

### Relación entre el incumplimiento de pago y el género

La siguiente gráfica muestra la relación entre el incumplimiento de pago y el género:

![Incumplimiento de pago según género](../data/img/incumplimiento_por_genero.png)

Se puede apreciar que tanto hombres como mujeres presentan incumplimientos de pago, pero la proporción es ligeramente mayor en los hombres.

### Relación entre el incumplimiento de pago y el límite de crédito

La siguiente gráfica muestra la distribución del límite de crédito según el incumplimiento de pago:

![Distribución del límite de crédito según el incumplimiento de pago](../data/img/dist_in_p_g.png)

Podemos notar que las cuentas con mayor límite de crédito tienden a tener un menor riesgo de incumplimiento de pago.

### Relación entre el incumplimiento de pago y la edad

La siguiente gráfica muestra la distribución de la edad según el incumplimiento de pago:

![Distribución de la edad según el incumplimiento de pago](../data/img/dis_in_of_pay.png)

No se observa una diferencia significativa en la distribución de la edad entre las cuentas que entran o no en incumplimiento de pago.

### Incumplimiento de pago según nivel educativo

La siguiente gráfica muestra el incumplimiento de pago según el nivel educativo:

![Incumplimiento de pago según nivel educativo](../data/img/dis_in_of_edu.png)

Podemos notar que las cuentas con educación universitaria presentan la menor proporción de incumplimiento de pago.

### Correlación entre las variables numéricas

La siguiente matriz de correlación muestra la relación entre las variables numéricas:

![Matriz de correlación](../data/img/heatmap.png)

Podemos observar que algunas variables, como `PAY_1`, `PAY_2`, `PAY_3`, están altamente correlacionadas entre sí, lo que indica una fuerte relación en el historial de pagos.

## Análisis de los Modelos Predictivos

En este proyecto, se desarrollaron tres modelos predictivos para determinar la probabilidad de que una cuenta entre en incumplimiento el próximo mes utilizando datos financieros históricos y la información del cliente. A continuación, se presenta un análisis de los resultados obtenidos para cada modelo:

## Resultados de los Modelos

### Regresión Logística
**Accuracy**: 80.8%

**Confusion Matrix**:

```
[[6758  177]
 [1533  438]]
```

**Classification Report**:

```
              precision    recall  f1-score   support

           0       0.82      0.97      0.89      6935
           1       0.71      0.22      0.34      1971

    accuracy                           0.81      8906
   macro avg       0.76      0.60      0.61      8906
weighted avg       0.79      0.81      0.77      8906

```


### Random Forest
**Accuracy**: 81.2%

**Confusion Matrix**:

```
[[6543  392]
 [1284  687]]
```

**Classification Report**:

```
              precision    recall  f1-score   support

           0       0.84      0.94      0.89      6935
           1       0.64      0.35      0.45      1971

    accuracy                           0.81      8906
   macro avg       0.74      0.65      0.67      8906
weighted avg       0.79      0.81      0.79      8906

```


### XGBoost
**Accuracy**: 81.1%

**Confusion Matrix**:

```
[[6539  396]
 [1287  684]]
```

**Classification Report**:

```
              precision    recall  f1-score   support

           0       0.84      0.94      0.89      6935
           1       0.63      0.35      0.45      1971

    accuracy                           0.81      8906
   macro avg       0.73      0.64      0.67      8906
weighted avg       0.79      0.81      0.79      8906

```


A continuación, se muestra el gráfico de las curvas ROC para cada uno de los modelos:

![Curvas ROC](../data/img/roc_curve.png)


En términos de precisión y capacidad de predicción de las cuentas en incumplimiento, los modelos de Random Forest y XGBoost superan ligeramente al modelo de Regresión Logística. Sin embargo, es importante tener en cuenta que estos resultados pueden variar dependiendo de la configuración específica del modelo y los datos utilizado .

Para obtener más detalles sobre la implementación y el análisis de los modelos, consulte los respectivos notebooks y el código fuente en la carpeta `notebooks` y `src` del repositorio.

## Conclusiones y análisis

Se presentan las principales conclusiones del análisis de este proyecto:

- Los tres modelos presentaron resultados similares en términos de precisión y capacidad de predicción, con una precisión promedio de alrededor del 80%.
- El modelo de Regresión Logística logró una precisión del 80.80%, mientras que Random Forest y XGBoost alcanzaron una precisión del 81.20% y 81.10%, respectivamente.
- Los modelos presentaron un mejor desempeño en la clasificación de cuentas que no entran en incumplimiento (clase 0), obteniendo altos valores de precisión y recall para esta clase.
- Sin embargo, los modelos tuvieron dificultades para clasificar correctamente las cuentas que efectivamente entraron en incumplimiento (clase 1), ya que presentaron valores más bajos de recall y precisión para esta clase.
- Es importante tener en cuenta que estos resultados son específicos para los datos utilizados en este proyecto y pueden variar con diferentes conjuntos de datos o configuraciones de los modelos.

En general, los modelos desarrollados pueden ser una herramienta útil para predecir la probabilidad de incumplimiento de una cuenta en el próximo mes.

## Conclusiones adicionales respecto al análisis exploratorio

- La distribución del incumplimiento de pago próximo mes muestra que existe un desbalance de clases, con una proporción mayor de cuentas que no entran en incumplimiento.
- El género no parece ser un factor determinante para predecir el incumplimiento de pago.
- El límite de crédito parece tener cierta influencia en el riesgo de incumplimiento, donde cuentas con límites más altos tienden a tener un menor riesgo.
- No se observa una relación clara entre la edad y el incumplimiento de pago.
- El nivel educativo muestra diferencias en el incumplimiento de pago, donde las cuentas con educación universitaria tienen una proporción menor de incumplimiento.
- Existe una correlación significativa entre las variables de historial de pagos, lo que indica que el comportamiento de pago anterior puede ser un indicador importante para predecir el incumplimiento futuro.

Estos análisis complementan los resultados de los modelos predictivos y proporcionan una visión más completa de los factores relacionados con el incumplimiento de pago en las cuentas.
