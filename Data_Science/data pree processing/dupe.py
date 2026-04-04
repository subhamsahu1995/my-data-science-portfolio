#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep  9 08:36:07 2021

@author: subham
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 23:39:18 2021

@author: subham
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv('/Users/subham/Desktop/data/360 assignment /data pree processing/DataSets/OnlineRetail.csv')
data
data.shape


#as we see there are some missing values in the column customerid  so we need to fill the values to convert it into  int64

'''Q1. For the given dataset perform the type 
casting (convert the datatypes, ex. float to int)'''

data.dtypes

# we need to fill the missing values in case of changing its type

data.CustomerID=data.CustomerID.interpolate(method ='linear', limit_direction ='forward')

data.dtypes
data.isna().sum()

''' the other way to fill the customerid'''

#to fill it with previous value
data[['CustomerID']]=data[['CustomerID']].fillna(method='pad')
data.CustomerID.isna().sum()

#Filled null values with the previous ones



#now to change the datatype

data[['UnitPrice','CustomerID']]=data[['UnitPrice','CustomerID']].astype('int64')
data 
data.dtypes



'''Q2. Check for the duplicate values, and handle the 
duplicate values (ex. drop)
'''

du=data.duplicated()
du
du=data.duplicated().sum() #o check  the total no of duplicates
du
#5238 dup values

du.value_counts()
zz=du.where(du==True)
zz#to see which all rows contain duplicate values
data=data.drop_duplicates()
data
#now all the duplicates values inputs are removed
data.isna().sum()
data.shape
# we see now there are (536671, 8)rows and column
'''
Q3. Do the data analysis (EDA)?
Such as histogram, boxplot, scatterplot etc
'''
import scipy as stats
from scipy import stats
from scipy import stats
lm=data.describe()
lm
ll=data[['Quantity','UnitPrice']] .mean()
ll
med=data[['Quantity','UnitPrice']].median()
med
md=data[['Quantity','UnitPrice']].mode()
md

md=data[['Quantity','UnitPrice']].skew()
md

stats.mean(data.Quantity)
stats.median(data.Quantity)
stats.skew(data[['Quantity','UnitPrice']])
stats.kurtosis(data[['Quantity','UnitPrice']])
import seaborn as sns


#boxplot
sns.boxplot(data.Quantity)

sns.boxplot(data.UnitPrice)


#histogram
plt.hist(data.Quantity)
plt.hist(data.UnitPrice)


#scatar plot
data.plot.scatter(x='Quantity',y='UnitPrice')


sns.lmplot(x='Quantity', y='UnitPrice', data=data) 
plt.title("Scatter Plot with Linear fit")
