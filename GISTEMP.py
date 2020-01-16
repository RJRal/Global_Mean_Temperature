
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

temp=np.array(temperature)
temp.shape


# Now let us plot the data 

fig= plt.figure(figsize=(6,3))

plt.plot(np.arange(0,len(temp))+1880,temp)
plt.xlabel('year', size=14)
plt.ylabel('anomalies from the mean', size=14)
plt.title('The rise in global mean temperatures since 1880, a clear trend!',size=14)
plt.show()
