import requests
import pandas as pd
import numpy as np
import pandas as pd
import mysql.connector
df= pd.read_csv('../Datos/etl_transformacion.csv')

class Crear_bbdd_tablas:
    
    
    def __init__(self, nombre_bbdd, contraseña):
        self.nombre_bdd= nombre_bbdd
        self.contraseña= contraseña
        
    
    def crear_bbdd(self,nombre_bbdd,contraseña):

        mydb = mysql.connector.connect(
        host='127.0.0.1',
        user="root",
        password=f"{contraseña}"
        )
        print("Conexión realizada con éxito")
        
        mycursor = mydb.cursor()

        try:
            mycursor.execute(f"CREATE DATABASE IF NOT EXISTS {nombre_bbdd};")
            print(mycursor)
        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)



    def crear_insertar_tabla(self,nombre_bbdd, contraseña, query):
    
        # nos conectamsos con el servidor usando el conector de sql
        cnx = mysql.connector.connect(user='root', password=f"{contraseña}",
                                        host='127.0.0.1', database=f"{nombre_bbdd}")
        # iniciamos el cursor
        mycursor = cnx.cursor()
        
        # intentamos hacer la query
        try: 
            mycursor.execute(query)
            cnx.commit() 
        # en caso de que podamos ejecutar la query devuelvenos un error para saber en que nos estamos equivocando
        except mysql.connector.Error as err:
            print(err)
            print("Error Code:", err.errno)
            print("SQLSTATE", err.sqlstate)
            print("Message", err.msg)
        