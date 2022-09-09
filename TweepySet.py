from distutils.command.config import config
from os import access
import configparser

import tweepy
import pandas as pd
import twint

# read keys from config.init

config = configparser.ConfigParser()
config.read('config.ini')

api_key = config['twitter']['api_key']
api_key_secret = config['twitter']['api_key_secret']

access_token = config['twitter']['access_token']
access_token_secret  = config['twitter']['access_token_secret']

# authentication to Twitter API
auth = tweepy.OAuthHandler(api_key, api_key_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)


def scrape_tweets_keywords(keyword: str, limit: int, since_date:str, until_date:str):
    """
    Purpose: busqueda por keyword generalmente politica y migracion
    """  
    c = twint.Config()
    
    #Filtros de busqueda
    c.Custom["tweet"] = ["id","created_at","user_id","username","name","tweet"] 
    c.Limit = limit
    c.Search = keyword                                                                                     
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

def scrape_tweets_users(username: str, limit: int, since_date:str, until_date:str) -> pd.DataFrame:
    """
    Purpose: busqueda por usuarios generalmente para politica
    """  
    c = twint.Config()
    
    #Filtros de busqueda
    c.Custom["tweet"] = ["id","created_at","user_id","username","name","tweet"] 
    c.Username = username
    c.Limit = limit                                                                                    
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

#Palabras claves de busqueda
politica_array = [
    'politica venezolana', 
    'oposicion venezolana',
    'chavistas',
    'chavez'
]

migracion = 'migracion venezolana',

#Usuarios para busqueda por perfil
user_array = [
    'politica venezolana', 
    'migracion venezolana', 
    'oposicion venezolana',
    'chavistas',
    'chavez'
]

#Nombre de archivos para guardar
name_csv = [
    'politica venezolana', 
    'migracion venezolana'
]


columns = ['id','created_at','user_id','username','name','tweet'] 
since_date = '2021-6-1'
until_date = '2022-8-17'
limit = 5

# #       BUSQUEDA POR POLITICA USUARIOS Y KEYWORDS

# for i in range(len(politica_array)):
#     df_prueba = scrape_tweets_keywords(politica_array[i], limit,since_date, until_date)
#     df_prueba[columns].to_csv(name_csv[0], mode='a', index=False, header=False) 

# #       BUSQUEDA POR MIGRACION KEYWORDS
# for u in range(len(city_array)):
#     for i in range(len(emoji_array)):
#         for j in range(len(emoji_array[i])):
#                 df_prueba = scrape_tweets(emoji_array[i][j], limit,city_array[u], since_date, until_date)
#                 df_prueba[columns].to_csv(name_cvs[i], mode='a', index=False, header=False) 



#Busqueda por Emojis
 
#Parametros de busqueda
max_count = 100
limit = 10000

#Variables de guardado por emojis
columns = ['Tweet Id','Time', 'User Name', 'User Screen Name', 'Text']
data = []


# for i in range(len(emoji_array)):
#     countRt  = 0
#     countDup = 0 
#     for j in range(len(emoji_array[i])):
        
#         tweets = tweepy.Cursor(api.search_tweets, 
#                                q = emoji_array[i][j],
#                                geocode = "8.280113,-62.717049,100000km ",
#                                lang='es',
#                                count = max_count,
#                                tweet_mode = 'extended').items(limit)
        
        
#         for tweet in tweets :
#             if tweet.full_text.startswith('RT'):
#                 countRt += 1
#             else:
#                 data.append([tweet.id, 
#                             tweet.created_at, 
#                             tweet.user.name, 
#                             tweet.user.screen_name, 
#                             tweet.full_text])
                
#     name_csv = title_cvs[i]
#     df = pd.DataFrame(data, columns= columns).to_csv(name_csv)
#     print(title_cvs[i], len(data), countRt, len(data) - countRt, countDup )
#     data.clear()
  
# #Variables de guardado por palabras claves  


def reply_tweet(name:str,tweet_id:str,limit:int ) -> pd.DataFrame:
    """
    Purpose: obtener las respuestas de un tweet usando el nombre y el id del tweet
  """
    replies = tweepy.Cursor(api.search_tweets, q='to:{}'.format(name),since_id=tweet_id, 
                            tweet_mode='extended').items(limit)
    replied_thread = []
    for reply in replies:
        if(reply._json['in_reply_to_status_id'] == tweet_id):
                replied_thread.append(reply._json['full_text'])  
                        
    df = pd.DataFrame(replied_thread)
    return df
# end def


   
   


