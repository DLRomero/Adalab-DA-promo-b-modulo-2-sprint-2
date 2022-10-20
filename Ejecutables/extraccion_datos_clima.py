from IPython.core.interactiveshell import InteractiveShell # Nos permite mostar más de una salida por celda
InteractiveShell.ast_node_interactivity = "all" # Nos permite mostar más de una salida por celda
import requests
import pandas as pd
import numpy as np
df_paises= pd.read_csv('../Datos/attacks_limpieza_IV.csv', index_col= 0)
df_paises = df_paises[df_paises.country.isin(['usa', 'australia', 'new zealand', 'south africa', 'papua new guinea'])]


class Desempaquetado:
    def __init__(self, pais, latitud, longitud):
        self.pais= pais
        self.latitud=latitud
        self.longitud=longitud

    def llamada_api(self):

        df_todo = pd.DataFrame()
        url =  f'http://www.7timer.info/bin/api.pl?lon={self.longitud}5&lat=-{self.latitud}6&product=meteo&output=json'
        response=requests.get(url=url)
        df = pd.json_normalize(response.json()['dataseries'])
        df['country'] = f"{self.pais}"
        df_todo = pd.concat([df, df_todo], axis = 0)

        return df_todo


    def limpiando(self, df):
        # df['wind_profile']= df['wind_profile'].apply(ast.literal_eval)

        # df['rh_profile']= df['rh_profile'].apply(ast.literal_eval)
        x = df['rh_profile'].apply(pd.Series)
        x[0].apply(pd.Series)['layer'][0]

        for i in range(len(x.columns)):

            # aplicamos el apply,extraemos el valore de la key "layer" y lo almacenamos en una variable que convertimos a string
            nombre = "rh_" + str(x[i].apply(pd.Series)['layer'][0])

            # hacemos lo mismo con una variable que se llame valores para "guardar" los valores de la celda
            valores = list(x[i].apply(pd.Series)["rh"] )

            # usamos el método insert de los dataframes para ir añadiendo esta información a el dataframe con la información del clima.
            df.insert(i, nombre, valores)

            y = df['wind_profile'].apply(pd.Series)
            y[0].apply(pd.Series)['layer'][0]
            y


        for i in range(len(y.columns)):

            # aplicamos el apply,extraemos el valore de la key "layer" y lo almacenamos en una variable que convertimos a string
            nombre = "wi_speed" + str(y[i].apply(pd.Series)['layer'][0])
            valores = list(y[i].apply(pd.Series)["speed"])
            df.insert(i, nombre, valores)

            nombre2 = "wi_direction" + str(y[i].apply(pd.Series)['layer'][0])
            valores2 = list(y[i].apply(pd.Series)["direction"])
            df.insert(i, nombre2, valores2)
            
        df_mean = df.groupby("country").mean()
        df_mean=df_mean.rename(columns={'wind10m.direction': 'wind10m_direction',
               'wind10m.speed': 'wind10m_speed'})
        
        df = pd.merge(left = df_paises, right= df_mean, how= "left", left_on= "country", right_on= "country")
        df.to_pickle('../Datos/datos_clima.pkl')
        df.to_csv('../Datos/datos_clima.csv')
       
     
        return df