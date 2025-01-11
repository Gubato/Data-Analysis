# Proyecto 3

# Importar datos a Python

import pandas as pd
import numpy as np

df = pd.read_csv('/Users/luisdgr/Desktop/Proyecto 3 /music_project_en.csv')

# Observación inicial de los datos

    #print(df.info())
    #print(df.columns)

#Renombrar columnas, en minúsculas y sin espacios; además de renombrar con snake_case en "user_id"

new_columns = []

for col in df.columns:
    new_name = col.strip().lower()
    new_columns.append(new_name)

df.columns = new_columns
df.rename(columns={'userid': 'user_id'}, inplace=True)

    #print(df.columns)

#Encontrar número de valores ausentes

    # print(df.isna().sum())

#Rellenar los NaN en las columnas 'artist', 'genre' y 'track'

rep_columns = ['track', 'artist', 'genre']

for rep in rep_columns:

    df[rep] = df[rep].fillna('unknown')

    # print(df.isna().sum())

# Contar duplicados explícitos y eliminarlos

    # print(df.duplicated().sum()) # Suma de valores duplicados = 3826

df.drop_duplicates(inplace=True)
df.reset_index(drop=True, inplace=True)

print(df.head())

    # print(df.duplicated().sum()) # Suma de valores duplicados (con corrección) = 0

# Revisión de duplicados implícitos

    # print(np.sort(df['genre'].unique())) # Mostrar los valores únicos ordenados por alfabeto

# Crear función de reemplazo para la columna 'genre' y reemplazar los errores del género hiphop

def replace_wrong_genres(wrong_genres, correct_genre):

    for wrong_genre in wrong_genres:
        df['genre'] = df['genre'].replace(wrong_genre, correct_genre)

replace_wrong_genres(['hip','hop','hip-hop'], "hiphop") # Llamado a la función recién creada

    # print(np.sort(df['genre'].unique())) # Mostrar los valores únicos ordenados por alfabeto, debería estar hiphop unificado


