
import re
import pandas as pd
import numpy as np
from cleantext import clean

#                   Funciones de lectura y escritura en archivos csv

def read_to_flat_list(fileName:str, columnName, separator:str)-> list:
    """
    Purpose: Leer un archivp cvs, y devolver como una lista plana los elementos de una columna
    """
    column = columnName
    data = pd.read_csv(fileName,sep = separator)
    data_c = data[column].values.tolist()
    data_list = list(np.concatenate(data_c).flat)
    return data_list
# end def



#                       Funciones de limpieza de texto
def clean_text(text) -> str:
    """
    Purpose:Limpiar el texto. Se eliminan:  URLs, (@) menciones, (;) puntos y coma y emojis.
    """
    text = clean(text, no_emoji=True)
    text = clean(text, no_urls=False, replace_with_url="<URL>")
    text = re.sub(";",' ', text)
    text = re.sub(' +', ' ',text)
    text = re.sub("\r|\n",' ', text)
    text = re.sub(r'@\w+', '', text)
    return text
# end def

#                       Funciones de etiquetado

def save_dataframe_tag(fileName: str, tag:str, text_list:list):
    """
    Purpose: devolver un dataframe con la opinion y el sentimiento que represeta
    """
    data = []
    if (tag == ''):
        for i in range(len(text_list)):
            data.append([text_list[i]])
        df = pd.DataFrame(data, columns=["comment"])
        df.to_csv(fileName, sep =';', index=False )
    else:
        for i in range(len(text_list)):
            data.append([text_list[i],tag])
        df = pd.DataFrame(data, columns=["comment",tag])
        df.to_csv(fileName , sep =';', index=False  )
# end def

#nombres de archivos csv
name_emojis = [
    'EmojisAlegria', 
    'EmojisAsco', 'EmojisIra',
    'EmojisMiedo', 'EmojisSorpresa','EmojisTristeza'
]
name_emojis_clean = [
    'Alegria', 
    'Asco', 'Ira',
    'Miedo', 'Sorpresa','Tristeza'
]

name_p = [
    'politica venezolana.csv', 
    'migracion venezolana.csv'
]

name_clean = [
    'PVenezolana_clean.csv', 
    'MVenezolana_clean.csv'
]

#                                                    Main
column_name = ['comment','sentiment']

n = 5
sep = ';'

save_list = []

nameA = "onEmoji.csv"
nameB = "EmojiB_set.csv"
nameC = "Emojic_set.csv"

data = []

num = 2263
select = []
i = 0 

k = 0
df = pd.read_csv(name_emojis_clean[n], sep = ';')
data_c = df[column_name].values.tolist()
while k <= num:
    select.append(data_c[k])
    k+=1

    
df_f= pd.DataFrame(select, columns=column_name)
df_f.to_csv(nameA, sep =';', mode='a', index=False, header=False)
