#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 18 17:33:26 2021

@author: subham
"""

'''
Perform clustering analysis on the telecom dataset.
The data is a mixture of both categorical and numerical 
data. It consists of the number of customers who churn. 
Derive insights and get possible information on factors 
that may affect the churn decision. 
Refer to Telco_customer_churn.xlsx dataset.
'''

import numpy as np
import pandas as pd

data=pd.read_excel('/Users/subham/Desktop/data/360 assignment /k means/Datasets_Kmeans/Telco_customer_churn (1).xlsx')
data
data.isna().sum()
data.duplicated().sum()
data.info()
data.columns
data.dtypes
data.info()
#here i a selecting all those columns whose data type is object i.e string
object_columns = data.select_dtypes(include=['object']).columns

data1=data.drop(object_columns,axis=1)
data1
dd=data1.describe()
data1.drop(['Count'],axis=1,inplace=True)
data1

#now we have to normalize our data
def funct(i):
    x=(i-i.mean())/(i.max()-i.min())
    return(x)

normal=funct(data1)
normal

#now aour data is normalized now to create scree plot
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

k=list(range(2,9))
wss=[]
for i in k:
    kmean=KMeans(n_clusters=i)
    kmean.fit(normal)
    wss.append(kmean.inertia_)

wss

plt.plot(k,wss,'ro-');plt.title('scree plot')

#as we see our maximum data coverd under 5 cluster
#now creating model
model=KMeans(n_clusters=4).fit(normal)
y=model.labels_
y

data['grpd']=y=model.labels_
data.columns
data=data.iloc[:,[30,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]]

newdata=data.groupby('grpd').mean()
newdata
























