
# Here I want to try statistical hypothesis testing for my GISTEMP data


import csv
import pandas as pd
import numpy as np
from scipy import stats

file_name="GISTEMP.csv"

df = pd.read_csv(file_name)

df.head() # From this we see that column 'Land and Ocean' is what I want (because these are mean values of temperature over both land and ocean

Global_Temp=np.array(df['Land and Ocean'])
North_Hemisphere=np.array(df['N Hem'])
South_Hemisphere=np.array(df['S Hem'])

Gloabl_mean=np.mean(Global_Temp)
Northern_mean=np.mean(North_Hemisphere)
Southern_mean=np.mean(South_Hemisphere)
Global_std=np.std(Global_Temp)
Northern_std=np.std(North_Hemisphere)
Southern_std=np.std(South_Hemisphere)

# One sample t-test

from scipy.stats import ttest_1samp

tset, pval = ttest_1samp(North_Hemisphere, Gloabl_mean)

print(tset)
print(pval)

if pval < 0.05:    # alpha value is 0.05 
   print(" reject H0") # Rejecting the Null hypothesis H0
else:
  print("accepti H0")


# Two sampled T-test

from scipy.stats import ttest_ind

stat, pval = ttest_ind(North_Hemisphere, South_Hemisphere)
print(stat)
print(pval)

if pval < 0.05:    # alpha value is 0.05 
   print(" reject H0") # Rejecting the Null hypothesis H0
else:
  print("accepti H0")

#Paired sampled t-test


ttest,pval = stats.ttest_rel(North_Hemisphere, South_Hemisphere)

if pval < 0.05:    # alpha value is 0.05 
   print(" reject H0") # Rejecting the Null hypothesis H0
else:
  print("accepti H0")

# Two-sample Z test

from statsmodels.stats.proportion import proportions_ztest

#ztest ,pval1 = stests.ztest(North_Hemisphere, South_Hemisphere, value=tm,alternative='two-sided')

if pval < 0.05:    # alpha value is 0.05 
   print(" reject H0") # Rejecting the Null hypothesis H0
else:
  print("accepti H0")

# ANOVA (F-TEST)

F, p = stats.f_oneway(North_Hemisphere, South_Hemisphere, Global_Temp)

print("p-value for significance is: ", p)

if pval < 0.05:    # alpha value is 0.05 
   print(" reject H0") # Rejecting the Null hypothesis H0
else:
  print("accepti H0")

import statsmodels.api as sm
from statsmodels.formula.api import ols

import statsmodels.api as sm
ns=np.column_stack((North_Hemisphere, South_Hemisphere))
ns.shape
ns
sh

model = sm.OLS(Global_Temp,North_Hemisphere).fit()

model.params

# ols('Yield ~ C(Fert)*C(Water)', df_anova2).fit()
# sm.stats.anova_lm(model, typ= 2)

# Chi-Square Test
from scipy.stats import chi2


