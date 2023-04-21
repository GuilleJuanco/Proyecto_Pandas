
#Importar librerias.
import pandas as pd
import numpy as np
import chardet

#Decodificacion del archivo csv.
with open("/home/guille/w2-project_pandas/data/attacks.csv", "rb") as f:
    result = chardet.detect(f.read())
    encoding = result['encoding']

#Importar archivo csv.
shark_df = pd.read_csv("/home/guille/w2-project_pandas/data/attacks.csv", encoding=encoding)
shark_df.shape

#Printear DataFrame para localizar anomalias en filas.

print(shark_df) #Las Ultimas filas sugieren que existen muchas filas con todos o casi todos los valores nulos.

#Limpiar filas 1. Criterio: Quitar filas con mas de mitad de datos nulos.

limpiar_1 = shark_df.dropna(thresh=13, inplace=True) #Limpiar filas con menos de 13 valores no nulos
limpiar_1

#Limpiar filas 2. Criterio: Quitar filas duplicadas.

limpiar_2 = shark_df.drop_duplicates(inplace=True)
limpiar_2







