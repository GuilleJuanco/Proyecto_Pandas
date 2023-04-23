
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

#Formato consistente en nombre de columnas. Quitar espacios al principio y final (Columna [["Sex ", "Species "]]). Formatear datos float a object. 

#Cambio de nombre de columnas en origen por todo minúscula sin espacios.
shark_df.columns = shark_df.columns.str.lower().str.replace(' ', '')

shark_df.columns

# Cambio el tipo de dato de las columnas year y originalorder a string.
shark_df[['year', 'originalorder']] = shark_df[['year', 'originalorder']].astype(str)

shark_df[["year", "originalorder"]].sample(10)

#Cambiar todos los nulos por "Unknown" en el DataFrame.
shark_df.fillna(value="Unknown", inplace=True)

#Check for nulls and nan in the dataframe.
check_nulls = shark_df.isnull().sum()

check_nans = shark_df.isna().sum()

#Transformación de datos columnas 1. Columna Case Number en origen. Cambiar columna entera a indice.

# Cambia valores en columna casenumber por indice. 
shark_df["casenumber"] = range(1, len(shark_df) + 1)

# Establece columna casenumber como indice.
shark_df.set_index("casenumber", inplace=True)

#Transformación de datos columnas 2. Columna Date en origen. Cambiar tipo formato por fecha y las que no valen por "Incomplete date".

#Cambiar dtype: Object a dtype: datetime64[ns] y aislar los valores que tengan un formato diferente.
shark_df["date"] = pd.to_datetime(shark_df["date"], errors="coerce")

conteo_nat = shark_df["date"].isna().sum() #844 valores que voy a convertir en "Invalid"

#Cambiar Valores NaT por la string Invalid.
shark_df["date"] = shark_df["date"].fillna("Invalid")

conteo_invalid = shark_df["date"].value_counts()["Invalid"]

#Quitar ceros de datetime.
shark_df.loc[shark_df["date"] != "Invalid", "date"] = shark_df.loc[shark_df["date"] != "Invalid", "date"].apply(lambda x: x.strftime("%Y-%m-%d"))

#Transformación de datos columnas 3. Columna Year en origen. Eliminar lo que vaya despues del punto.

#Eliminar lo que va despues del punto.
shark_df["year"] = shark_df["year"].str.split(".").str[0]

#Reemplazar 0 por Unkown.
shark_df["year"] = shark_df["year"].replace("0", "Unknown")

count_Unknown_year = shark_df["year"].value_counts()["Unknown"] #Cuenta los valores Unknown en columna.

#Transformación de datos columnas 4. Columna Type en origen. Cambiar nombre de columna por "attacktype". 

#Cambiar nombre de columna
shark_df.rename(columns={"type": "attacktype"}, inplace=True)
shark_df.columns

#Transformación de datos columnas 5. Columna Country en origen. Cambiar Nulos por Unknown. Transformar unnamed column por SeaOcean. Dejar solo paises y transformar SeaOcean for Unknown.

#Make a list with all countries in the world.
#Import csv
countries_df = pd.read_csv("countries.csv")
#Create a list
countries_raw = countries_df['Country'].tolist()
#Quitar ultimo espacio
countries = [e.strip().upper() for e in countries_raw]
#Añadir posible nomenclatura de paises a lista
countries.append("USA")
#Checkea si valor en columna esta en lista countries
check_en_countries = shark_df['country'].str.strip().str.upper().str.contains('|'.join(countries))
#Conteo de paises validos en columna
conteo_countries = check_en_countries.sum()
#Cambio de typos o mala escritura del pais por str "Invalid".
shark_df.loc[~check_en_countries, "country"] = "Invalid"
#OJO "INVALID" PODRIA SER OCEAN/SEA

#Transformación de datos columnas 6. Columna Area en origen. Cambiar nulos por Unknown. Si hay SeaOcean pasar values a columna SeaOcean. Quitar espacios al principio y final str en value.



#Transformación de datos columnas 7. Columna Location en origen. dividir en dos y transformar Unnamed 2 por Region, asignar lo que vaya despues de coma a Region, quitar espacios.

#Transformación de datos columnas 8. Columna Activity en origen. Si hay mas de x caracters, cortar string por x patron. Cambiar Nulos por Unknown.

#Transformación de datos columnas 9. Columna Name en origen. Si no empieza por Upper eliminar elementos de la string. Cambiar Nulos por Unknown.

#Transformación de datos columnas 10. Columna Sex  en origen. Quitar espacio al final de str en nombre columna. Quitar nulos. Opcional: Cambiar M por Male y F por Female.

#Transformación de datos columnas 11. Columna Age en origen. Cambiar nulos por Unknown. Checkear typos. 

#Transformación de datos columnas 12. Columna Injury en origen. Cambiar nulos por Unknown. Si no injury, reemplazar en columna por No Injury.

#Transformación de datos columnas 13. Columna Fatal en origen. Check todos son N o Y. Cambiar nulos por Unknown.

#Transformación de datos columnas 14. Columna Time en origen. Quitar nulos y sacar values a lista para tomar decision sobre agrupar horas y periodos.

#Transformación de datos columnas 15. Columna Species  en origen. Cambiar vacios y nulos. Sacar tipos a la lista, transformar resto por Unknown. Quitar espacio al final en nombre de columna. Opcional: Tamaño de tiburon a nueva columna "Size".

#Transformación de datos columnas 16. Columna Investigador or Source. Dividir columna en Investigador y Source si es posible, si no limpiar caracteres que no aportan claridad.

#Transformación de datos columnas 17. Columna pdf en origen. Limpiar nulos.

#Transformación de datos columnas 18. Columnas href y href formula. IGUALES. Dejar href y reusar href formula para otro uso. Comprobar los nulos de estas columnas especialmente.

#Transformación de datos columnas 20. Columnas Case Number.1 y Case Number.2 en origen. Iguales y redundantes respecto a columnas anteriores (Fecha). No aportan nada nuevo pueden ser reutilizadas ambas.

#Transformación de datos columnas 22. Columnas original order en origen. Dtype Float64 cambiar a str. Eliminar lo que vaya despues del punto. Ofrece index original, relativo orden cronológico de casos (No exacto). Eliminar nulos.

#Transformación de datos columnas 23. Averiguar que es el Bool?. Una de las columnas se puede reusar.