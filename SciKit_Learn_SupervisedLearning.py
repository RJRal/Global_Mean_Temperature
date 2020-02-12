
# In this script, I will apply supervised learning to my GISTEMP data 

import csv
import pandas as pd
import numpy as np

file_name="/home/rusul/Desktop/Upload/global-temp-annual_csv.csv"

temp = pd.read_csv(file_name)
# temp contains global mean temperatures, northern hemisphere mean 
# temperatures, and southern hemisphere mean temperatures for the period 
# 1880 - 2014 

temp.head()

Glb=temp['Land and Ocean']
NH=temp['N Hem']
SH=temp['S Hem']

# Always check shapes and types! 

print(Glb.shape)
print(NH.shape)
print(SH.shape)

type(Glb)
type(NH)
type(SH) 


# I want to see if the global mean temperature data are a good fit for the Northern Hemisphere data and the Southern Hemisphere data
# This is the simplest machine learning task to perform 

X = Glb[:, np.newaxis]
y = NH

from sklearn.linear_model import LinearRegression
model = LinearRegression(fit_intercept=True)
model.fit(X,y)


print(model.coef_)
print(model.intercept_)

# Using train_test_split 

from sklearn.model_selection import train_test_split
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, random_state=1) 

model.fit(Xtrain, ytrain)                  
ymodel = model.predict(Xtest) 

import matplotlib.pyplot as plt
plt.scatter(ymodel,ytest.values)
plt.show()

# almost slop of 45°!
