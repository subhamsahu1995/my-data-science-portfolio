#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 17 20:10:00 2021

@author: subham
"""

#Analyze the information given in the following 
'''
Perform clustering on mixed data. Convert the categorical
 variables to numeric by using dummies or label encoding
 and perform normalization techniques. The dataset has the
 details of customers related to their auto insurance. 
 Refer to Autoinsurance.csv dataset.

'''


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv('/Users/subham/Desktop/data/360 assignment /k means/Datasets_Kmeans/AutoInsurance (1).csv')
data
data.duplicated().sum()

data.isna().sum()

data.dtypes
#now to select all those columns with data types numeric
data.columns
data=data.drop(['Customer', 'State','Effective To Date','Gender','Marital Status'],axis=1)
data.dtypes

data_obj=data.select_dtypes(include=['object'])
data_obj.dtypes

data1=pd.get_dummies(data_obj)


data2=data.drop(data_obj,axis=1)
data2.dtypes

#so here i have created dummy variavle 

#now normalizee our numeric data
def function(i):
    x=(i-i.mean())/(i.max()-i.min())
    return(x)
  
norm_data=function(data2.loc[:,:])

#now joining the normalized data and 
new_data=pd.concat([norm_data,data1],axis=1)

#now to create scree plot
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans



wss=[]
k=list(range(2,8))
for i in k:
    kmean=KMeans(n_clusters=i)
    kmean.fit(new_data)
    wss.append(kmean.inertia_)
wss

plt.plot(k,wss,'ro-');plt.title('scree_plot');plt.xlabel("no of cluster");plt.ylabel("within sum of square")

#now create a model
model=KMeans(n_clusters=4).fit(new_data)
x=model.labels_

data['bkt']=x=model.labels_

#now to arrange the columns
data.columns
data=data[['bkt','Customer Lifetime Value', 'Response', 'Coverage', 'Education',
       'EmploymentStatus', 'Income', 'Location Code', 'Monthly Premium Auto',
       'Months Since Last Claim', 'Months Since Policy Inception',
       'Number of Open Complaints', 'Number of Policies', 'Policy Type',
       'Policy', 'Renew Offer Type', 'Sales Channel', 'Total Claim Amount',
       'Vehicle Class', 'Vehicle Size']]


data.dtypes
#now grouping the data
grpd=data.groupby(['bkt']).mean()
grpd


#so here we say that the the  all the customers fall under  grp 0  are the most valuable customer


