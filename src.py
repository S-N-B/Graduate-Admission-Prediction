#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  2 15:22:14 2019

@author: shyam
"""

import numpy as np
import pandas as pd

#Importing Dataset
dataset=pd.read_csv("Admission_Predict.csv")
X = dataset.iloc[:,1:8].values #values removes headings of columns
y = dataset.iloc[:,-1].values
model = []
accuracy = []

from sklearn.preprocessing import StandardScaler
sc_X = StandardScaler()
X = sc_X.fit_transform(X)

from sklearn.model_selection import train_test_split, cross_val_score
XTrain, XTest, yTrain, yTest = train_test_split(X, y, test_size=0.1, random_state=10)

#MultiVariable Linear Regression
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(XTrain,yTrain)
s=regressor.score(XTest,yTest)
print(s)
model.append('LinearRegression')
accuracy.append(s)
yPred = regressor.predict(XTest)
print(yPred,yTest)

#Support Vector Regression
from sklearn.svm import SVR
regressor = SVR(kernel='linear',epsilon=0.01)
regressor.fit(XTrain,yTrain)
s=regressor.score(XTest,yTest)
print(s)
model.append('Support Vector Regression')
accuracy.append(s)
yPred = regressor.predict(XTest)
print(yPred,yTest)

#Decision Tree Regression
from sklearn.tree import DecisionTreeRegressor as DT
regressor = DT(max_depth=10)
regressor.fit(XTrain,yTrain)
s=regressor.score(XTest,yTest)
print(s)
model.append('Decision Tree Regression')
accuracy.append(s)
yPred = regressor.predict(XTest)
print(yPred,yTest)

#Random Forest Regression
from sklearn.ensemble import RandomForestRegressor as RF
regressor = RF(n_estimators=100,max_depth=10,criterion='mse')
regressor.fit(XTrain,yTrain)
s=regressor.score(XTest,yTest)
print(s)
model.append('Random Forest Regression')
accuracy.append(s)
yPred = regressor.predict(XTest)
print(yPred,yTest)

#Compare the models
import matplotlib.pyplot as plt
index = np.arange(len(model))
plt.bar(index,accuracy,alpha=0.3,color='blue')
plt.ylabel('Accuracy')
plt.xlabel('Different Machine Learning Models')
plt.xticks(index,model)
plt.show()

for i in range(len(model)):
    print(model[i]," : ",accuracy[i])
