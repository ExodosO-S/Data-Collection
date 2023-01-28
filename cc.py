import re
import pandas as pd
import numpy as np


data = []
# df_m = pd.read_csv('miedos.csv', sep = ';')
# text_list = list(np.concatenate(df_m[["comment"]].values.tolist()).flat)
# print(text_list)

df = pd.read_csv('doneT.csv', sep=';')
print(df)

df2 = df[df.label != 'fear']

print (df2)
