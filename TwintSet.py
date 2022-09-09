import twint
import pandas as pd


def scrape_tweets(topic: str, limit: int, since_date:str, until_date:str) -> pd.DataFrame:
    """
    Proposito: Funcion para extaer una cantidad de tweets(limit) publicados en una localidad (city)
               de un tema (topic) en un intervalo de tiempo(since,until)
    """
    c = twint.Config()
    #Filtros de busqueda
    c.Limit = limit
    c.Search = topic                                                                                     
    c.Since = since_date
    c.Until = until_date
    c.Lang = 'es'   
    
    #Guardado de resultados
    c.Hide_output = True
    c.Store_pandas = True
    c.Pandas = True
    
    twint.run.Search(c)
    
    df = twint.storage.panda.Tweets_df
    return df
# end def

def profile_info(username: str) -> pd.DataFrame:
    """
    Proposito: Funcion para confirmar si un usuario de es venezolano
    """
    #Filtros de busqueda del usuario
    c = twint.Config()
    c.Username = username
    
    #Guardado de resultados
    c.Hide_output = True
    c.Store_pandas = True
    c.Pandas = True
    twint.run.Lookup(c)
    
    df = twint.storage.panda.Tweets_df
    return df
# end def



#Palabras claves de busqueda
politica_array = [
    'politica venezolana', 
    'oposicion venezolana',
    'chavistas',
    'chavez',
    'Dictadura de Maduro'
]

migracion = 'migracion venezolana'

#Nombre de archivos para guardar
name_csv = [
    'politica venezolana', 
    'migracion venezolana'
]


columns = ['id','created_at','user_id','username','name','tweet'] 
since_date = '2021-6-1'
until_date = '2022-8-17'
limit = 50000


for i in range(len(politica_array)):
    df_prueba = scrape_tweets(politica_array[i], limit, since_date, until_date)
    df_prueba[columns].to_csv(name_csv[0], mode='a', index=False, header=False) 

for i in range(len(migracion)):
    df_prueba = scrape_tweets(politica_array[i], limit, since_date, until_date)
    df_prueba[columns].to_csv(name_csv[0], mode='a', index=False, header=False) 
    
