import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
dfp=pd.read_csv("dat.csv",header=0)
def prommo(a,b):
    if a<=50000 and b<=2:

      return 'NO'
    elif a>50000 and b>2:
       return 'yes'
    elif a>50000 and b>5:
       return 'yes'
    elif a>50000 and b<5:
       return 'No'
    else:
       return "NO"
dfp['promlist'] = dfp.apply(lambda row: prommo(row['Sal'], row['Exp']), axis=1)
dfp.to_csv('dat.csv')
# print(dfp)
x=dfp[['Sal','Exp']]
y=dfp['promlist']
kn=KNeighborsClassifier(n_neighbors=3)
kn.fit(x,y)
# print(kn.predict([[]]))
a=int(input("enter your sal:"))
b=int(input(("enter your Exp:")))
print(kn.predict([[a,b]]))