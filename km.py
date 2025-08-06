from sklearn.cluster import KMeans
import numpy as np
X = np.array([[2, 10], [2, 5], [8, 4],[5, 8], [7, 5], [6, 4],[1,2],[4,9]])
kmeans = KMeans(n_clusters=3, random_state=0, n_init="auto").fit(X)
print(kmeans.labels_)
dataprediction=kmeans.predict([[5,4]])
print(dataprediction)