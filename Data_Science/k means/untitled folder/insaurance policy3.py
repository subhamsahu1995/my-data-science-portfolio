#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 11:13:54 2021

@author: subham
"""

'''
Analyze the information given in the following ‘Insurance Policy dataset’ to  
create clusters of persons falling in the same type. 
Refer to Insurance Dataset.csv
'''

import numpy as np
import pandas as pd
data=pd.read_csv('/Users/subham/Desktop/data/360 assignment /k means/Datasets_Kmeans/Insurance Dataset.csv')
data
data.isna().sum()
data.duplicated().sum()
data.info()
data.columns
data.dtypes
#now to normalize our data
def fun(i):
    x=(i-i.mean())/(i.max()-i.min())
    return(x)
 
norm_data=fun(data)
norm_data

from sklearn.cluster import KMeans
#now its time to create scree plot
k=list(range(2,8))
wss=[]
for i in k:
    kmean=KMeans(n_clusters=i)
    kmean.fit(norm_data)
    wss.append(kmean.inertia_)

wss

import matplotlib.pyplot as plt
plt.plot(k,wss,'ro-');plt.title('screeplot')

#from the sree plot i find that maximum no of data is covered till cluster 4
#now developing the model
model=KMeans(n_clusters=3).fit(norm_data)
model.labels_
m=model.labels_
data['grp']=m=model.labels_
data.columns
#now arranging the columns
data.columns
data=data[['grp','Premiums Paid', 'Age', 'Days to Renew', 'Claims made', 'Income']]
data2=data.groupby('grp').mean()
data2

#from the above model we can say that the people with average age of 50-55 are 
#having higher premium paids
