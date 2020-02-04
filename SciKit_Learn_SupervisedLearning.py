
# In this script, I will apply supervised learning to my GISTEMP data 

import csv
import pandas as pd
import numpy as np

file_name="/home/rusul/Desktop/Upload/global-temp-annual_csv.csv"

df = pd.read_csv(file_name)

df.head()

Glb=df['Land and Ocean']

NH=df['N Hem']
SH=df['S Hem']

print(Glb.shape)
print(NH.shape)
print(SH.shape)


# I want to see if the global mean temperature data are a good fit for the Northern Hemisphere data and the Southern Hemisphere data

X = Glb[:, np.newaxis]
y = NH

from sklearn.linear_model import LinearRegression
model = LinearRegression(fit_intercept=True)
model.fit(X,y)


print(model.coef_)
print(model.intercept_)

from sklearn.model_selection import train_test_split
Xtrain, Xtest, ytrain, ytest = train_test_split(X, y, random_state=1) 

model.fit(Xtrain, ytrain)                  
y_model = model.predict(Xtest) 

from sklearn.metrics import accuracy_score
accuracy_score(ytest, y_model)

