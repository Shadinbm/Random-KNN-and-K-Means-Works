import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
dfp=pd.read_csv("dat.csv",header=0)
def fet(name):
    vowels='aAeEiIoOuU'
    vowelss=sum(1 for c in name if c in vowels)
    return vowelss
dfp['Vowlc']=(dfp['Fname']+dfp['LName']).apply(fet)
dfp['len']=(dfp['Fname']+dfp['LName']).apply(len)
dfp.to_csv('dat.csv')
def clasin(num):
    if num<=10:
        return 'A'
    elif num<=15:
        return 'B'
    elif num<=20:
        return 'c'
    else:
        return 'D'
dfp['Nclasss']=dfp['len'].apply(clasin)  
dfp.to_csv('dat.csv')
x=dfp[['len','Vowlc']]
y=dfp['Nclasss']  
kn=KNeighborsClassifier(n_neighbors=3)
kn.fit(x,y)
name=input("enter your name:")
# def fet(name):
#     vowels='aAeEiIoOuU'
#     vowelss=sum(1 for c in name if c in vowels)
#     return vowelss
nlen=len(name)
vname=fet(name)
pdc=kn.predict([[nlen,vname]])
print(pdc)








  