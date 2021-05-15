###Logistic Regression
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib
import matplotlib.pyplot as plt

from pymongo import MongoClient
connection=MongoClient('localhost',27017)
db=connection.Logistic
data=db.Trail2
pry=data.find()

for item in pry:
    print(item)
       
dataset2=pd.DataFrame(list(data.find()))
print(dataset2)

titanic_data=dataset2.drop("_id",axis="columns")
print(titanic_data)

##histogram
v1=titanic_data.hist()
print(v1)
#print(titanic_data.dtypes)
##importing seaborn for visualising the data
##countplot for surving Vs Non Survived
print(sns.countplot(x='Survived',data=titanic_data))
#Male VS Female Survival
print(sns.countplot(x='Survived',data=titanic_data,hue='Sex'))
#checking for null values
print(titanic_data.isna().sum())
#Visualising null values
print(sns.heatmap(titanic_data.isna()))
##finding % of null value in age column
print(titanic_data['Age'].isna().sum()/len(titanic_data['Age']) * 100)
##finding % of null value in cabin column
print(titanic_data['Cabin'].isna().sum()/len(titanic_data['Cabin']) * 100)
##finding the distribution for age column
print(sns.displot(x='Age',data=titanic_data))
##filling age column
titanic_data['Age'].fillna(titanic_data['Age'].mean(),inplace=True)
print(titanic_data['Age'].isna().sum())
print(sns.heatmap(titanic_data.isna()))
titanic_data.drop('Cabin',axis=1,inplace=True)
print(titanic_data.head())
##Preparing data to Model
##Converting string to numeric (Sex column to 0 and 1)
gender=pd.get_dummies(titanic_data['Sex'],drop_first=True)
titanic_data['Gender']=gender
##Dropping the string value columns not required
titanic_data.drop(['Name','Sex','Ticket','Embarked'],axis=1,inplace=True)
print(titanic_data.head())
##dependent and independent variable
x0=titanic_data[['PassengerId','Pclass','Age','SibSp','Parch','Fare','Gender']]
y0=titanic_data['Survived']
##Data modelling Splitting into train and test set
from sklearn.model_selection import train_test_split
x0_train,x0_test,y0_train,y0_test=train_test_split(x0,y0,test_size=0.33,random_state=42)
from sklearn.linear_model import LogisticRegression
lr=LogisticRegression()
print(lr.fit(x0_train,y0_train))
predict=lr.predict(x0_test)
print(predict)
##printing confusion matrix
from sklearn.metrics import confusion_matrix
print(confusion_matrix(y0_test, predict))
##Classification report
from sklearn.metrics import classification_report
print(classification_report(y0_test, predict))