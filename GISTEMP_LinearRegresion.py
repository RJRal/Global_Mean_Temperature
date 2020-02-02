

# This is a script to apply the simplest form of machine learning: Linear Regression 

# I will use the GISTEMP global mean temperature data 1880-2014

import csv
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plot

file_name="/home/rusul/Desktop/Upload/global-temp-annual_csv.csv"

df = pd.read_csv(file_name) # This gives you a data frame so better use commands that are useful in data frames

df.head() # From this we see that column 'Land and Ocean' is what I want (because these are mean values of temperature over both land and ocean

X = df[['Land and Ocean']]

y = pd.DataFrame(np.array(np.arange(len(X)))) 
#x = df.iloc[1, :-1].values

#y = df.iloc[:, 2].values

xTrain, xTest, yTrain, yTest = train_test_split(X, y, test_size = 1/3, random_state = 0)

linearRegressor = LinearRegression()

linearRegressor.fit(xTrain, yTrain)

yPrediction = linearRegressor.predict(xTest)

print(xTrain.shape)
print(yTrain.shape)
print(xTest.shape)
print(yTest.shape)
print(yPrediction.shape)


plot.scatter(yTrain, xTrain , color = 'teal')
plot.plot(linearRegressor.predict(xTrain),xTrain, color = 'firebrick')
plot.title('Temperature Fluctuations vs Time (Training set)', size=16)
plot.xlabel('Time', size=14)
plot.ylabel('Temperature variations from the mean', size=14)
plot.show()

