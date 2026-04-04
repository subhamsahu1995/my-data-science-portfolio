#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 15 14:50:31 2021

@author: subham
"""
import pandas as pd
import numpy as np
'''
Perform K means clustering on the airlines dataset 
to obtain optimum number of clusters. Draw the inferences 
from the clusters obtained. Refer to EastWestAirlines.xlsx dataset.
'''



data=pd.read_excel('/Users/subham/Desktop/data/360 assignment /k means/Datasets_Kmeans/EastWestAirlines (1).xlsx','data',index_col=None)
data
data.shape
data.columns
data1=data.drop('ID#',axis=1)
data1.shape
data1.isna().sum()
data1.duplicated().sum()
data1=data1.drop_duplicates()
data1
#so here we see there is one duplicate  value so  we need to remove
#it as it may create disturbance in performing analysis

#now we need to normalize our data
def norm(i):
    x=(i-i.mean())/(i.max()-i.min())
    
    return (x)
#here main moto is to make my data scale free andunit free
normalize_data=norm(data1.iloc[:,:])

#so now our next steo is to 
#create scree plot or elbow curve
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
# within-cluster sum-of-squares criterion 


k=list(range(2,10))
k
wss=[]
for i in k:
    kmean=KMeans(n_clusters=i)
    kmean.fit(normalize_data)
    wss.append(kmean.inertia_)
    
wss    


#Plot K values range vs WCSS to get Elbow graph for choosing K (no. of clusters)

plt.plot(k,wss);plt.title('scree plot');plt.xlabel('no of clusters');plt.ylabel('total_within_SS')



model=KMeans(n_clusters=5).fit(normalize_data)
model.labels_
y=model.labels_
y
#now adding it to the dataframe
data1['grouping']=y=model.labels_
data1.columns

data1.info()
#now arranging the columns

data1=data1.iloc[:,[11,0,1,2,3,4,5,6,7,8,9,10]]
data1.columns
#now we have to group our data
new_data=data1.groupby('grouping').mean()
new_data






