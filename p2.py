import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
dfp=pd.read_csv("dat.csv",header=0)
def classi(Exp):
    if Exp <= 5:
        return "Sales"
    elif 6 <= Exp <= 10:
        return "HR"
    else:
        return "I.T"
dfp['Dep']=dfp["Exp"].apply(classi)
x=dfp[['Sal','Exp']]
y=dfp['Dep']
f=KNeighborsClassifier(n_neighbors=3)
f.fit(x,y)
print("Model trained:", f)
# print(f.predict([[8000,4]]))
# dfp.to_csv("dat.csv")

    