
# this is a script to read gloabl mean temperatures from a csv file and then construct a nice looking time series 
import csv
import pandas as pd
import numpy as np

file_name="/home/rusul/Desktop/Upload/global-temp-annual_csv.csv"

#with open(file_name, 'r') as csvfile: 
    # creating a csv reader object 
 #   csvreader = csv.reader(csvfile, delimiter=',') 
    
  #  for line in csvreader:
   #     print(line[0])
  
# pandas is better! 

df = pd.read_csv(file_name)

df.head() # what data do we want? 


temperature=df['Land and Ocean']

temp=np.array(t)
temp.shape


