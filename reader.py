import pandas as pd
import re

global df
df = pd.read_excel('bls.xlsx')

def isfloat(num):
    try:
        float(num)
        return True
    except ValueError:
        return False
total_par=len(df.index)
print(len(df.index))
for i in df.index:
    print((df['NAMA'][i]).upper())
    print(str(df['NO K.P'][i]).replace('-',''))
    print(str(i) + '/' + str(total_par))