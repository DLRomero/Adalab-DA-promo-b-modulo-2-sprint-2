# importamos todas las librerias que son necesarias para que nuestro código funcione. Estas librerías son las que hemos usado en las clases invertidas de ETL-II y ETL-III. 

import requests
import pandas as pd
import numpy as np


#cargamos el df al que uniremos al final los datos de clima

df_paises= pd.read_csv('../Datos/attacks_limpieza_IV.csv', index_col= 0)
df_paises = df_paises[df_paises.country.isin(['usa', 'australia', 'new zealand', 'south africa', 'papua new guinea'])]

print("csv cargado")


# creamos el imput para solicitarle al usuario los datos para la extraccion del país que deseen

pais = input("¿De país quieres la información climática? ")
print("---------------------------------------------------------------")

latitud = float(input("Indica la latitud del país del que quieres información "))
print("---------------------------------------------------------------")

longitud = float(input("Indica la longitud del país del que quieres información "))
print("---------------------------------------------------------------")


import extraccion_datos_clima as ed #importamos nuestra libreria

# iniciamos la clase
desemp = ed.Desempaquetado(pais, latitud, longitud)


# utilizamos el metodo de "llamada API" para obtener los datos de la API
print(f"Estamos haciendo la llamada a la API para el país {pais}".format(pais = pais))
df_limpiando=desemp.llamada_api()
print("-----------------------------------------")
print(df_limpiando)
print("-----------------------------------------")


# el siguiente paso es limpiar los datos de los dataframes
print("-----------------------------------------")
print(f"Estamos sacando la media de {pais} y los estamos uniendo a tu dataframe")
df_final=desemp.limpiando(df_limpiando)
print(df_final)
print("-----------------------------------------")


print("El proceso ya ha termiando, tienes todos tus datos almacenados en tu ordenador")