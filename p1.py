import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
dfp=pd.read_csv("dat.csv",header=0)
def classi(Sal):
    if Sal < 60000:
        return "Low"
    elif 60000 <= Sal <= 90000:
        return "Medium"
    else:
        return "High"
dfp['Class']=dfp["Sal"].apply(classi)
x=dfp[['Sal']]
y=dfp['Class']
f=KNeighborsClassifier(n_neighbors=3)
f.fit(x,y)
print("Model trained:", f)
print(dfp)
dfp.to_csv("dat.csv")