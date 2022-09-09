from asyncore import read
import re
import pandas as pd
import numpy as np
from cleantext import clean

#                   Funciones de lectura y escritura en archivos csv

def read_to_flat_list(fileName:str, columnName:str)-> list:
    """
    Purpose: Leer un archivp cvs, y devolver como una lista plana los elementos de una columna
    """
    column = [columnName] 
    data = pd.read_csv(fileName)
    data_c = data[column].values.tolist()
    data_list = list(np.concatenate(data_c).flat)
    return data_list
# end def



#                       Funciones de limpieza de texto
def clean_text(text) -> str:
    """
    Purpose:Limpiar el texto. Se pretende eliminar: URLs, caracteres especiales y emojis.
    """
    #remover emojis
    text = clean(text, no_emoji=True)
    #eliminar los ; (punto y coma)
    text = re.sub(";",' ', text)
    #remover espacio en blanco extra
    text = re.sub(' +', ' ',text)
    #eliminar faltos de linea y retorno de carro
    text = re.sub("\r|\n",' ', text)
    #remover las URLs y las menciones (@NombreUsuario)    
    processed_text = re.sub(r"(?:\@|http?\://|https?\://|www)\S+", "", text)
    text = " ".join(processed_text.split())
    
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
column_name = 'tweet'

data_raw = []
data_clean = []

n = 5


data_raw = read_to_flat_list(name_emojis[n],column_name)
for j in range(len(data_raw)):
    data_raw[j] = clean_text(data_raw[j])
    print(j)
    data_clean = list(set(data_raw))
save_dataframe_tag(name_emojis_clean[n],name_emojis_clean[n],data_clean)
     