#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 21:36:18 2021

@author: subham
"""
'''
Convert the continuous data into discrete classes on iris dataset.
Prepare the dataset by performing the preprocessing techniques, to
 have the data which improve model performance.
'''
#====================================================================

'''
Data discretization is the process of converting continuous data
into discrete buckets by grouping it. Discretization is also 
known for easy maintainability of the data
'''

#Discretization transforms are a technique for transforming numerical input or output variables to have discrete ordinal labels.

#demonstration of the discretization transform

from sklearn.preprocessing import KBinsDiscretizer
import matplotlib.pyplot as plt
import pandas as pd

# generate gaussian data sample
data=pd.read_csv('/Users/subham/Desktop/data/360 assignment /data pree processing/DataSets/iris.csv')
data
data.shape
data=data.iloc[:,1:]
data.columns
#droping the colimn as it is not reqired
data=data.drop(["Species"],axis=1)
data


# discretization transform the raw data
kbins = KBinsDiscretizer(n_bins=10, encode='ordinal', strategy='uniform')
data_trans = kbins.fit_transform(data)
#here each interval contain 10% of total observation

# histogram of the transformed data
plt.hist(data_trans, bins=10)






#alternative  method


data2=pd.read_csv('/Users/subham/Desktop/data/360 assignment /data pree processing/DataSets/iris.csv')
data2.columns
data2.drop(['Species','Unnamed: 0'],axis=1,inplace=True)
data2.columns
data2.shape

# we use pandas.cut


data2['bucket']=pd.cut(data['Sepal.Length'],bins=5,labels=["1","2","3","4","5"])
data2

plt.hist(data2.bucket,list=5)

#in this way we can do it to every column


