#Importing packages
import numpy as np
import pandas as pd
import sklearn
from sklearn.cluster import KMeans
import matplotlib
import matplotlib.pyplot as plt

##Connection of mongoDb
from pymongo import MongoClient
connection=MongoClient('localhost',27017)
db=connection.Kmeans
data=db.Trail1
ury=data.find()

for item in ury:
    print(item)
       
dataset1=pd.DataFrame(list(data.find()))
print(dataset1)

df1=dataset1.drop("_id",axis="columns")
print(df1)
    


##histogram
r=df1.hist()
print(r)
##Bar chart
kl=df1.plot.bar()
print(kl)
##K means 
x=df1.iloc[:,[0,1,2,3]].values
wcss=[]
for i in range(1,11):
    kmeans=KMeans(n_clusters=i,init='k-means++',max_iter=300,n_init=10,random_state=(0))
    kmeans.fit(x)
    wcss.append(kmeans.inertia_)
plt.plot(range(1,11),wcss)
plt.title=('Elbow Method')
plt.xlabel=('No of clusters')
plt.ylabel=('wcss')
plt.show()    
##
kmeans=KMeans(n_clusters=3,init='k-means++',max_iter=300,n_init=10,random_state=(0))
y_means=kmeans.fit_predict(x)
kmeans.cluster_centers_
plt.scatter(x[y_means==0,0],x[y_means==0,1],s=100,c='Yellow',label='Iris_sentosa')
plt.scatter(x[y_means==1,0],x[y_means==1,1],s=100,c='magenta',label='Iris_vericolor')
plt.scatter(x[y_means==2,0],x[y_means==2,1],s=100,c='Cyan',label='Iris_virginica')

plt.scatter(kmeans.cluster_centers_[:,0],kmeans.cluster_centers_[:,1],s=100,c='Green',label="Centroids")
plt.legend()
