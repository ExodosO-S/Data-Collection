
import snscrape.modules.twitter as sntwitter
import pandas as pd
import itertools
import twint

def profile_info(username: str) -> pd.DataFrame:
    """
    Proposito: Funcion para extraer la informacion de un perfil
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


def scrape_tweets(topic: str, limit: int, city:str, since_date:str, until_date:str) -> pd.DataFrame:
    """
    Proposito: Funcion para extaer una cantidad de tweets, publicados en una localidad, 
               de un tema, en un intervalo de tiempo
    """
    search = '{} geocode:{} lang:es until:{} since:{}'.format(topic,city,until_date, since_date)
   
    tweets_list = []
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(search).get_items()):
        if i > limit:
            break
        tweets_list.append([tweet.id, tweet.date, tweet.user.username, tweet.content])
        
    df = pd.DataFrame(tweets_list, columns=['id','date','user','content'])
    return df
# end def

def scrape_tweet_p(topic: str, limit: int, since_date:str, until_date:str) -> pd.DataFrame:
    """
    Proposito: Funcion para extaer una cantidad de tweets,
               de un tema, en un intervalo de tiempo
    """
    search = '{} lang:es until:{} since:{}'.format(topic,until_date, since_date)
   
    tweets_list = []
    for i,tweet in enumerate(sntwitter.TwitterSearchScraper(search).get_items()):
        if i > limit:
            break
        tweets_list.append([tweet.id, tweet.date, tweet.user.username, tweet.content])
        
    df = pd.DataFrame(tweets_list, columns=['id','date','user','content'])
    return df
# end def

#Arreglos para busquedas por emojis

emoji_array =[
    #Emojis de Alegria
    ['😊', '😂', '😀', '😁', '🤣', '😃', '😄', '😆', '😉',
    '😇', '😍', '😘', '🥰', '😗', '😙', '😚', '🤩', '😋',
    '😝', '😜', '😛', '🤪', '🤗', '🤭', '🥴', '😌', '🥳'],
    #Emojis de Asco
    ['🤮', '🤢'],
    #Emojis de Ira
    ['👿', '😤', '😡', '😠', '💀', '☠️', '🤬', '🖕'],
    #Emojis de miedo
    ['😱', '😨', '😰', '😖'],
    #Emojis de Sorpresa
    ['😯', '😲', '🤯', '😵'],
    #Emojis de Tristeza
    ['😣', '😥', '😫', '😓', '😕', '☹️', '🙁', 
    '😞', '😟', '😢', '😭','😦','😧','😔']
]

#Arreglo de cuidades para busqueda (Ciudades de Venezuela)

city_array = [
    #Parte superior Maracaibo
    '10.246060156173254,-71.37228551201015,150km',
    #Parte superior Merida, Barinas, parte baja de maracaibo
    '8.672966476826637,-71.25528566679023,150km',
    #Parte superior Barquisimeto, apure, barinas, acarigua
    '8.998644474848565,-67.49796139564408,360km',
    #Parte superior, Caracas, Maracay, valencia
    '10.144518404385412,-64.64681438136844,260km',
    #Estado Bolivar, Parte superior de amazonas, Maturin
    '6.276694359336725,-64.55362541708513,400km',
    #Parte abaja Amazonas
    '3.1236755117895285,-65.86649170454469,160km'
]
#Arreglo de titulos para los CSV
name_emojis = [
    'EmojisAlegria', 
    'EmojisAsco', 'EmojisIra',
    'EmojisMiedo', 'EmojisSorpresa','EmojisTristeza'
]

columns = ['id','date','user','content'] 


#Palabras claves de busqueda
politica_array = [
    'politica venezolana', 
    'oposicion venezolana',
    'chavistas',
    'chavez',
    'Dictadura de Maduro'
]

migracion = [
    'darien venezolanos', 
    'darien venezuela',
]

#Nombre de archivos para guardar
name_p = [
    'politica venezolana.csv', 
    'migracion venezolana.csv'
]

since_date = '2021-8-1'
until_date = '2022-8-17'
limit = 20000

for i in range(len(migracion)):
    for j in range (len(migracion[i])):
        df_prueba = scrape_tweet_p(migracion[i],limit,since_date, until_date)
        df_prueba[columns].to_csv(name_p[1], mode='a', index=False, header=False)

# vzla_loc = ''
# vzla_bio = ''

# p_loc = ''
# p_bio = ''

# for u in range(len(city_array)):
#     for i in range(len(emoji_array)):
#         for j in range(len(emoji_array[i])):
#             df_prueba = scrape_tweets(emoji_array[i][j],limit,city_array[u],since_date, until_date)
#             profile_list = df_prueba.user.values.tolist()
#             for w in profile_list:
#                 df_profile = profile_info(profile_list)
#                 if df_profile[p_loc] == vzla_loc or df_profile[p_bio] == vzla_bio:
#                     df_prueba.to_csv(name_emojis[i], mode='a', index=False, header=False)
#                 else:
#                     continue

