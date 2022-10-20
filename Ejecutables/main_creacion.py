from IPython.core.interactiveshell import InteractiveShell # Nos permite mostar más de una salida por celda
InteractiveShell.ast_node_interactivity = "all" # Nos permite mostar más de una salida por celda

import requests
import pandas as pd
import numpy as np
import pandas as pd
import mysql.connector
pd.options.display.max_columns=None

#cargamos el df del que se extraerán los datos para cargarlos en sql

df= pd.read_csv('../Datos/etl_transformacion.csv')


print("csv cargado")


# creamos el imput para solicitarle al usuario los datos para la extraccion del país que deseen

contraseña = input("Ingresa tu contraseña de acceso de MySql ")
print("---------------------------------------------------------------")

nombre_bbdd = input("Indica el nombre de tu base de datos a crear ")
print("---------------------------------------------------------------")




import creacion_bbdd_tablas_clima as crn #importamos nuestra libreria

# iniciamos la clase
ejemplo = crn.Crear_bbdd_tablas(nombre_bbdd, contraseña)

# utilizamos el metodo de "llamada API" para obtener los datos de la API
print(f"Estamos creando tu base de datos {nombre_bbdd}".format(nombre_bbdd = nombre_bbdd))
bbdd_ejemplo= ejemplo.crear_bbdd(nombre_bbdd, contraseña)
print("-----------------------------------------")
print("-----------------------------------------")


# el siguiente paso es crear alguna tabla
query_creacion_tabla = input("Si deseas crear una tabla, ingresa la query necesaria")
print("---------------------------------------------------------------")
ejemplo.crear_insertar_tabla(nombre_bbdd, contraseña, query_creacion_tabla)
print("---------------------------------------------------------------")


print("El proceso ha finalizado")