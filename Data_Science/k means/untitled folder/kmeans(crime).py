#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 13:22:58 2021

@author: subham
"""
'''
Perform clustering for the crime data and 
identify the number of clusters      
formed and draw inferences. Refer to crime_data.csv dataset.
'''
import pandas as pd
import numpy as np
data=pd.read_csv("/Users/subham/Desktop/data/360 assignment /k means/Datasets_Kmeans/crime_data (1).csv")
data
data.isna().sum()
data.columns
data=data.drop('Unnamed: 0',axis=1)
data
#no missing value and 
data.duplicated().sum()
#no duplicates rows
 #now normalize our data
def normal(i):
    x=(i-i.mean())/(i.max()-i.min())
    return(x)

normalize=normal(data)
data.Murder.count()

#as we see our data is normalized i.e scale and unit free
#now to know how may cluster can be formed we need to from form 
#scree plot

import matplotlib.pyplot as plt
from sklearn.cluster import KMeans



wss=[]
k=list(range(2,8))
for i in k:
    kmean=KMeans(n_clusters=i)
    kmean.fit(normalize)
    wss.append(kmean.inertia_)

wss

plt.plot(k,wss,'ro-');plt.title('scree_plot');plt.xlabel("no of cluster");plt.ylabel("within sum of square")

#as we the maximun no of data is covered till 3 cluster
# now  we have to create the model
model=KMeans(n_clusters=3).fit(normalize)
model.labels_
x=model.labels_

data['buccket']=x
data.columns

new_data=data[['buccket','Murder', 'Assault', 'UrbanPop', 'Rape']]

grp=new_data.groupby('buccket').mean()
grp['tot_crim']=grp.iloc[:,:].sum(axis=1)


#as we see the maximum no of crimes 
#occurs to the states which come under buccket 2



































