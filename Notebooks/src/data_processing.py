import pandas as pd

def clean_credit_card_data(file_path):
    # Leer el archivo Excel
    df_orig = pd.read_excel(file_path)
    
    # Crear una máscara booleana para los valores cero
    df_zero_mask = df_orig == 0
    feature_zero_mask = df_zero_mask.iloc[:, 1:].all(axis=1)
    
    # Filtrar el DataFrame original y crear una copia limpia
    df_clean = df_orig.loc[~feature_zero_mask, :].copy()
    
    # Reemplazar los valores específicos en las columnas 'EDUCATION' y 'MARRIAGE'
    df_clean['EDUCATION'].replace(to_replace=[0, 5, 6], value=4, inplace=True)
    df_clean['MARRIAGE'].replace(to_replace=0, value=3, inplace=True)
    mean_value = df_clean['PAY_1'].loc[df_clean['PAY_1'] != 'Not available'].astype(int).mean()
    df_clean['PAY_1'] = df_clean['PAY_1'].replace('Not available', int(mean_value)).astype(int)
    
    # Devolver el DataFrame limpio
    return df_clean
