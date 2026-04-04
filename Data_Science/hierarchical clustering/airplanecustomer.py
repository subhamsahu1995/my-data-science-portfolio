#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 12 20:55:05 2021

@author: subham
"""

#Perform clustering for the airlines data to obtain optimum number of clusters.
# Draw the inferences from the clusters obtained. 
#Refer to EastWestAirlines.xlsx dataset.

import pandas as pd 
import numpy as np

data=pd.read_excel('/Users/subham/Desktop/data/360 assignment /hierarchical clustering/Dataset_Assignment Clustering/EastWestAirlines.xlsx','data',index_col=None)

'''What is the business objective?'''
#the business objective is to segmet the customer with similar traveling behaviour

'''Are there any constraints?'''
#to provide offer to customers for better business growth

data.isna().sum() #no missing value
z=data.describe()
data.shape
data.columns
# i m going to drop id as it is not required inoperation
data=data.drop('ID#',axis=1)
data.columns
# now i am going to normalize my data

def fun(i):
    s=(i-i.mean())/(i.max())-(i.min())
    return(s)

normalize_data=fun(data.iloc[:,: ]) 
normalize_data
do=normalize_data.describe()
#so till here i have normalize my data
#now to know how mny cluster i  can creat

from scipy.cluster.hierarchy import linkage

x=linkage(normalize_data,method='complete',metric='euclidean')

import scipy.cluster.hierarchy as sch

import matplotlib.pyplot as plt

plt.figure(figsize=(15,11));plt.title('dindogram');plt.xlabel('index');plt.ylabel('distance')

sch.dendrogram(x,leaf_rotation=0,leaf_font_size=10)
plt.show()
# now its time to create a model
from sklearn.cluster import AgglomerativeClustering
modle1=AgglomerativeClustering(n_clusters=4,linkage='complete',affinity='euclidean').fit(normalize_data)

r=modle1.labels_
#this will rank customer


#now adding it as a column in my data dataframe
data['ranked']=r=modle1.labels_
data.columns

#now lets arrange the column keeping 'ranked' at 1st position

data=data[['ranked','Balance', 'Qual_miles', 'cc1_miles', 'cc2_miles', 'cc3_miles',
       'Bonus_miles', 'Bonus_trans', 'Flight_miles_12mo', 'Flight_trans_12',
       'Days_since_enroll', 'Award?']]


data1=data.groupby('ranked').mean()
data1

# Write about the benefits/impact of the solution - 
#in what way does the business (client) 
#benefit from the solution provided?
'''
now the client can bring dif diff type of offers to 
diff  segment group  which may impat in business growth 
'''


