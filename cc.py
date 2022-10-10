import re
import pandas as pd
import numpy as np


data = []
# df_m = pd.read_csv('miedos.csv', sep = ';')
# text_list = list(np.concatenate(df_m[["comment"]].values.tolist()).flat)
# print(text_list)


df = pd.read_csv('done.csv', sep=';')
data_t = df[["Tweet","Label"]].values.tolist()

# for i in range(len(text_list)):
#             data.append([text_list[i],'surprise'])

# for i in range(len(data_t)):
#             data.append(data_t[i])
            
            
df = pd.DataFrame(data_t, columns=["Tweet",'Label'])
df.to_csv('doneFR.csv', sep =';', index=False, encoding="utf-8")



