
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

#Formato consistente en nombre de columnas. Quitar espacios al principio y final (Columna [["Sex ", "Species "]]). Formatear datos int y float a object (Mejor que solo cambiar year por int(0000)). 

#Transformación de datos columnas X. Criterio: Cambiar nulos por str menos en COLUMNA YEAR donde el data type es float para poder operar. Siguiente paso cambiar nulos columna year por int(0000), y el resto de nulos del DF por String "Unknown" o "Invalid", aplicar casos especiales.

#Transformación de datos columnas 1. Columna Case Number en origen. Eliminar por duplicados cuando x columnas coinciden. Cambiar columna entera por indice.

#Transformación de datos columnas 2. Columna Date en origen. Cambiar tipo formato por fecha y las que no valen por "Incomplete date"

#Transformación de datos columnas 3. Columna Year en origen. Comprobar que coincide con año en columna Date. Cambiar formato a Integer 8 o 16. Cambiar Nulos por cuatro 0 seguidos. 

#Transformación de datos columnas 4. Columna Type en origen. Cambiar nombre de columna por TypeofAttack. Cambiar Nulos por str Invalid.

#Transformación de datos columnas 5. Columna Country en origen. Cambiar Nulos por Unknown. Transformar unnamed column por SeaOcean. Dejar solo paises y transformar SeaOcean for Unknown.

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

