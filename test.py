
import os
import pandas as pd
"""
for i in os.listdir("C:\\Users\\ramka\\Desktop\\Creditcard\\data"):
    df = pd.read_csv("C:\\Users\\ramka\\Desktop\\Creditcard\\data\\"+i)
    k = df.dtypes
"""
read_file = open("C:\\Users\\ramka\\Desktop\\Creditcard\\schema_training.json").read()
contents = eval(read_file)
for i in contents['ColName']:
    print(i)