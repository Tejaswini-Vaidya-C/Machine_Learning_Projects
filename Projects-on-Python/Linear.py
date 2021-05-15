import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt
from pymongo import MongoClient

connection=MongoClient('localhost',27017)
db=connection.Pressure
data=db.Trail
temperature=data.find()

for item in temperature:
    print(item)
       
dataset=pd.DataFrame(list(data.find()))
print(dataset)    

df2=dataset.drop("_id",axis="columns")
print(df2)
# ##df2=pd.read_csv("F://DatasetR//pressure.csv")
# ##df2
#Bar graph of the data
m1=df2.plot.bar()
print(m1)
#Finding the dependent and independent variable
X=df2.iloc[:,:-1]
Y=df2.iloc[:,-1]
# ##
#Train test split
from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=1/3,random_state=0)
#Training the model
from sklearn.linear_model import LinearRegression
Linear_regressor=LinearRegression()
Linear_regressor.fit(X_train,Y_train)
#Predict
Y_pred=Linear_regressor.predict(X_test)
#Visualize training data
plt.scatter(X_train,Y_train,color="blue")
plt.plot(X_train,Linear_regressor.predict(X_train),color='yellow')
plt.show()
#Visualize testing data
plt.scatter(X_train,Y_train,color="magenta")
plt.plot(X_train,Linear_regressor.predict(X_train),color='green')
plt.show()

