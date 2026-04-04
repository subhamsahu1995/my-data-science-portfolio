# -*- coding: utf-8 -*-
"""
subham Editor

This is a temporary script file.
"""
import pandas as pd
import numpy as np
from scipy import stats

#Q1) Calculate Skewness, Kurtosis using R/Python code & draw inferences on the following data.

data=pd.read_csv('/Users/subham/Desktop/data/360 assignment /eda assignment/Q1_a.csv')
data
data.drop(['Index'],axis=1,inplace=True)
data
data.describe()
data.dtypes
data.columns
data.shape
#they both work same
data.speed.skew()

stats.skew(data.speed)
# skewness is between -0.5 and 0.5, 
#the data speed  are fairly symmetrical
#mean=median=mode
stats.kurtosis(data.speed)
#it says slithtly left but 
#we consider it as normally distributed

'''
to get SKEW OF ALL THE  COLUMN
stats.skew(data)
stats.kurtosis(data)
'''
stats.kurtosis(data.dist)

stats.skew(data.dist)

#between 0.5 and 1, the data are moderately skewed

import matplotlib.pyplot as plt
plt.hist(data.speed),plt.title('histogram')
plt.hist(data.dist),plt.title('histogram')


data.mean()
data.median()
data.mode()

#to check outlier  we use matplotlib
import seaborn as sns
sns.boxplot(data.speed),plt.title(' speed box-plot')
sns.boxplot(data.dist),plt.title('dist box-plot')
#so  here we get to know that in distance column there is some outlier



import scipy.stats as stats
import pylab
#to see that may data is normally distributed or not we 
########use probplot

stats.probplot(data.dist,dist='norm',plot=pylab)
#we can say that data is normally distributed as most of 
#the poins are close to the line

stats.probplot(data.speed,dist='norm',plot=pylab)
#we can say that data is normally distributed as most of 
#the poins are close to the line
#=====================question 1(b)===================================

data2=pd.read_csv('/Users/subham/Desktop/data/360 assignment /eda assignment/Q2_b.csv')
data2
data2.dtypes
data2.columns
data2.drop(['Unnamed: 0'],axis=1,inplace=True)
data2.SP=data2.SP.astype('int64')
data2.WT=data2.WT.astype('int64')
data2.describe()

#skewness
data2.skew()
data2.kurtosis()

data2.SP.skew()

# positive skew mean>median>mode
#   DATA SP IS HIGHLY SKEWED

stats.kurtosis(data2.SP)   #alternative way to find

#THE DISTRIBUTION IS at PEEKED

plt.hist(data2.SP),plt.title('histogram')
plt.hist(data2.WT).plt.title('histogram')

stats.skew(data2.WT)
#moderately skewed as the skew values ranges from -0.5 to -1

stats.kurtosis(data2.WT)


data2.mean()
data2.median()
data2.mode()

stats.mode(data2.SP)
# TO CHECK WHETHER THERE IS AN OUTLIER OR NOT

import seaborn as sns
sns.boxplot(data2.WT),plt.title(' wt box-plot')
plt.boxplot(data2.SP),plt.title('sp box-plot')
# AS WE SEEE BOTH THE DATA CONTAIN OUTLIER




#TO CHECK WHETHER IT IS NORMALLY DISTRIBUTED OR NOT
 #WE USE PROBPLOT
import scipy. stats as stats
import pylab
stats.probplot(data2.SP,dist='norm',plot=pylab)
#THIS IS NOT NORMALLY DISTRIBUTED

stats.probplot(data2.WT,dist='norm',plot=pylab)
#THIS IS NORMALLY DISTRIBUTED(BUT THERE ARE OUTLIERS




import pandas as pd
my_data = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 8, 6, 4, 2])
my_data.skew()









