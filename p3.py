import pandas as pd
import numpy as np
from sklearn.neighbors import KNeighborsClassifier
dfp=pd.read_csv("dat.csv",header=0)
x=dfp[['Sal','Exp']]
y=dfp['Class']
k=KNeighborsClassifier(n_neighbors=3)
k.fit(x,y)
q=[[88000,5]]
d,i=k.kneighbors(q)
similar_employees = dfp.iloc[i[0]]
print(similar_employees)