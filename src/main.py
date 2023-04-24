
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
#Valores con "sea" u "ocean" en el string a columna renombrada.
#Transformar columna "casenumber.1" en "seaocean".
shark_df.rename(columns={"casenumber.1": "seaocean"}, inplace=True)
#Filtra filas que contienen sea u ocean.
sea_ocean_rows = shark_df["country"].str.contains('sea|ocean', case=False)
#Asignar los valores de "country" a "seaocean".
shark_df.loc[sea_ocean_rows, "seaocean"] = shark_df.loc[sea_ocean_rows, "country"]
#Cambio de typos o mala escritura del pais por str "Invalid".
shark_df.loc[~check_en_countries, "country"] = "Invalid"


#Transformación de datos columnas 6. Columna Area en origen. Cambiar nulos por Unknown. Si hay SeaOcean pasar values a columna SeaOcean. Quitar espacios al principio y final str en value.

#Quitar espacios al final y principio de valores.
shark_df["area"] = shark_df["area"].str.strip()
#Filtra filas que contienen sea u ocean.
sea_ocean_rows = shark_df["area"].str.contains('sea|ocean', case=False)
#Asignar los valores de "area" a "seaocean".
shark_df.loc[sea_ocean_rows, "seaocean"] = shark_df.loc[sea_ocean_rows, "area"]


#Transformación de datos columnas 7. Columna Location en origen. dividir en dos y transformar Unnamed 2 por Region, asignar lo que vaya despues de coma a Region.

#Transformar columna "unnamed:22" en "region".
shark_df.rename(columns={"unnamed:22": "region"}, inplace=True)
#Añadir lo que viene despues de la ultima coma a "region".
shark_df["region"] = shark_df["location"].apply(lambda x: x.split(",")[-1])

#Transformación de datos columnas 8. Columna Activity en origen. Si hay mas de x caracters, cortar string por x patron. Cambiar Nulos por Unknown.

#Reemplaza strings con mas de 20 caracteres por "Invalid".
shark_df["activity"] = shark_df["activity"].apply(lambda x: "Invalid" if len(x) > 20 else x)

#Transformación de datos columnas 9. Columna Name en origen. Si no empieza por Upper y tamaño de string mayor de 30, cambiar valor por "Invalid". Cambiar Nulos por Unknown.

#Quita espacios por delante y por detras en strings.
shark_df["name"] = shark_df["name"].str.strip()

#Reemplaza strings de mas de 30 caracteres y strings que no empiezan por mayuscula por "Invalid".
shark_df["name"] = shark_df["name"].apply(lambda x: "Invalid" if (len(x) > 30 or not x[0].isupper()) else x)


#Transformación de datos columnas 10. Columna Sex  en origen. Quitar espacio al final de str en nombre columna. Quitar nulos. Opcional: Cambiar M por Male y F por Female.

#Cambio de "F" y "M" por "female" y "male".
shark_df["sex"] = shark_df["sex"].replace({"F": "Female", "M": "Male"})

#Transformación de datos columnas 11. Columna Age en origen. Cambiar nulos por Unknown.

#Columna sin cambiar aparte de convertir nulos y nan por "Unknown"

#Transformación de datos columnas 12. Columna Injury en origen. Cambiar nulos por Unknown. Si no injury, reemplazar en columna por No Injury.

#Transformar columna "unnamed:23" en "injuryoutcome".
shark_df.rename(columns={"unnamed:23": "injuryoutcome"}, inplace=True)
#Añade "survived" a la columna injuryoutcome cuando el string no contiene "FATAL".
shark_df.loc[~shark_df["injury"].str.contains("fatal", case=False), "injuryoutcome"] = "survived"
#Añade "no injury" a la columna injuryoutcome cuando el string contiene "no injury".
shark_df.loc[shark_df["injury"].str.contains("no injury", case=False), "injuryoutcome"] = "no injury"
#Añade "fatal" a la columna injuryoutcome cuando el string contiene "FATAL".
shark_df.loc[shark_df["injury"].str.contains("FATAL", case=False), "injuryoutcome"] = "fatal"

#Transformación de datos columnas 13. Columna Fatal en origen. Check todos son N o Y. Cambiar nulos por Unknown.

#Cambio de nombre columna.
shark_df = shark_df.rename(columns={"fatal(y/n)": "fatal"}) 
#Cambio de "Y" y "N" por "Fatal" y "Survived".
shark_df["fatal"] = shark_df["fatal"].replace({"Y": "fatal", "N": "survived"})

#Transformación de datos columnas 14. Columna Time en origen. Quitar nulos y sacar values a lista para tomar decision sobre agrupar horas y periodos.

#Cambio de nombre columna hrefformula por timeofday.
shark_df = shark_df.rename(columns={"hrefformula": "timeofday"})

#Añade el momento del dia a la columna timeofday.
for i, row in shark_df.iterrows():
    try:
        hour = int(row["time"][:2])
        if 0 <= hour < 6:
            shark_df.loc[i, "timeofday"] = "night"
        elif 6 <= hour < 12:
            shark_df.loc[i, "timeofday"] = "morning"
        elif 12 <= hour < 18:
            shark_df.loc[i, "timeofday"] = "afternoon"
        elif 18 <= hour < 24:
            shark_df.loc[i, "timeofday"] = "evening"
        else:#Si el int tiene typo y no entra dentro del rango.
            shark_df.loc[i, "timeofday"] = "Invalid" 
    except:
        #Si la string no se puede convertir a int.
        shark_df.loc[i, "timeofday"] = "Invalid"

#Transformación de datos columnas 15. Columna Species  en origen. Cambiar vacios y nulos. Sacar tipos a la lista, transformar resto por Unknown. Quitar espacio al final en nombre de columna. Opcional: Tamaño de tiburon a nueva columna "Size".

#Importa csv
species_df = pd.read_csv("species.csv")
#Crea lista con especies
species_raw = species_df["Species"].tolist()
#Mantener nombres que aparecen en lista en columna, de otra forma los valores son "Unknown".
shark_df["species"] = shark_df["species"].apply(lambda x: x if any(name in x for name in species_raw) else "Unknown")
#Renombra columna para usar como size
shark_df = shark_df.rename(columns={"casenumber.2": "sizeshark"})
#Deja la parte previa a la coma en species y lo que va despues lo añade a sizeshark.
shark_df["sizeshark"] = shark_df["species"].str.split(",", 1).str[1]
shark_df["species"] = shark_df["species"].str.split(",", 1).str[0]

#Transformación de datos columnas 16. Columna Investigador or Source. Quitar nulos.

#Columna sin cambiar aparte de convertir nulos y nan por "Unknown"

#Transformación de datos columnas 17. Columna pdf en origen. Quitar nulos.

#Columna sin cambiar aparte de convertir nulos y nan por "Unknown"

#Transformación de datos columnas 18. Columnas href y href formula. IGUALES. Dejar href y reusar href formula para otro uso. Comprobar los nulos de estas columnas especialmente.

#Columna sin cambiar aparte de convertir nulos y nan por "Unknown"

#Transformación de datos columnas 20. Columnas Case Number.1 y Case Number.2 en origen. Iguales y redundantes respecto a columnas anteriores (Fecha). 

#casenumber.1 ----- oceansea
#casenumber.2 ----- sizeshark
#Cambiar NaN por "Unknown".
shark_df.fillna(value="Unknown", inplace=True)


#Transformación de datos columnas 22. Columnas original order en origen. Dtype Float64 cambiar a str. Eliminar nulos.

#Columna sin cambiar aparte de convertir nulos y nan por "Unknown"

#Transformación de datos columnas 23. Averiguar que es el Bool?. Una de las columnas se puede reusar.
#unnamed:22 ----- region
#unnamed:23 ----- injuryoutcome