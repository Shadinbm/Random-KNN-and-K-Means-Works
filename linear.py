from sklearn import linear_model
X=[[2600],[3000],[3200],[3600],[4000]]
y=[550000,565000,610000,680000,725000]
m1=linear_model.LinearRegression()
m1.fit(X,y)
print(m1.predict([[3300]]))