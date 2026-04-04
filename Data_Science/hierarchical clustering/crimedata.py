#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 13 01:14:46 2021

@author: subham
"""

'''2Perform clustering for the crime data and
identify the number of clusters          
formed and draw inferences. Refer to crime_data.csv dataset.
'''

import pandas as pd
import numpy as np
data=pd.read_csv('/Users/subham/Desktop/data/360 assignment /hierarchical clustering/Dataset_Assignment Clustering/crime_data.csv')
data.shape
d=data.describe()
data.dtypes
data.isna().sum() #as we see no recods are missing

#What is the business objective?

#to know in which area are the higher crime rate and 
#type of action required to control the crime

#Are there any constraints?
#minimize crime 

#now we need to normalize our data
def normal(i):
    
    s=(i-i.mean())/(i.max())-(i.min())
    return(s)

data1=normal(data.iloc[:,1:])
data1
des=data1.describe()
#so here i normalize my data set

#now the to how many cluster we can go for  we need to draw
#dendogram

from scipy.cluster.hierarchy import linkage
import scipy.cluster.hierarchy as sch

l=linkage(data1,method='complete',metric='euclidean')
import matplotlib.pyplot as plt

plt.Figure(figsize=(17,12));plt.xlabel('index');plt.ylabel('distance')

sch.dendrogram(l,leaf_rotation=(0),leaf_font_size=(6))
plt.show()

#now to create the model
#so for that i have import aglomerative clustering
from sklearn.cluster import AgglomerativeClustering
model=AgglomerativeClustering(n_clusters=5,linkage='complete',affinity='euclidean').fit(data1)

y=model.labels_
y
#converting it into dataframe
bucket=pd.DataFrame(y)

data['bucketgrp']=pd.DataFrame(y)
#adding column y in my dataframe
data.columns
#ARRANGINGING THE COLUMS
data=data[['bucketgrp','Unnamed: 0', 'Murder', 'Assault', 'UrbanPop', 'Rape']]
data
grp=data.iloc[:,:].groupby('bucketgrp').mean()
grp

grp.sum()# this will give the totoal of each column  but i want it by rows

grp['tot_crime']=grp.iloc[:,:].sum(axis=1)
grp
#this will give the total crime of each group i.e 
'''
so from here i get the glance that my 
grup 1 state are the state which have high crime rate
so we need to take more action in state 2 group and we also get the 
glance that 
Assault       945.563354 is maximum in crime list
'''




