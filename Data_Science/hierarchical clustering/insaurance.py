#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 21:25:35 2021

@author: subham
"""

'''
Perform clustering on mixed data.
 Convert the categorical variables to numeric 
 by using dummies or label encoding and perform
 normalization techniques. The data set consists of 
 details of customers related to their auto insurance. 
 Refer to Autoinsurance.csv dataset.
 
'''
import numpy as np
import pandas as pd
data=pd.read_csv('/Users/subham/Desktop/data/360 assignment /hierarchical clustering/Dataset_Assignment Clustering/AutoInsurance.csv')
data
data.isna().sum()
data.duplicated().sum()
data.info()
data.columns
data1=data.drop(['Customer','Education','State','Gender','Marital Status'],axis=1)
data1

numeric=data1.select_dtypes(include=['object']).columns
# now normalize the data so let drop all the nominal data 
number=data1.drop(numeric,axis=1)
def normal(x):
    y=(x-x.mean())/(x.max()-x.min())
    return(y)
number=normal(number.iloc[:,:])


#now create  dummy variable for the caterorical columns

dummee=pd.get_dummies(data1)
dummee

newdata=pd.concat([number,dummee],axis=1)
newdata
# so now my data is normalized so lets check for cluster
from scipy.cluster.hierarchy import linkage
import scipy.cluster.hierarchy as sch
z=linkage(newdata,method='complete',metric='euclidean')
z
import matplotlib.pyplot as plt
plt.Figure(figsize=(20,15));plt.title('dendrogram');plt.xlabel('index');plt.ylabel('distance')

sch.dendrogram(z,leaf_rotation=(0),leaf_font_size=(9))
plt.show()
from sklearn.cluster import AgglomerativeClustering
model=AgglomerativeClustering(n_clusters=(5),linkage='complete',affinity='euclidean').fit(newdata)
model.labels_
r=model.labels_
data1['ranked']=pd.DataFrame(r)
data1.columns

#now arranging the columns

data1=data[['ranked','Customer Lifetime Value', 'Response', 'Coverage', 'Effective To Date',
       'EmploymentStatus', 'Income', 'Location Code', 'Monthly Premium Auto',
       'Months Since Last Claim', 'Months Since Policy Inception',
       'Number of Open Complaints', 'Number of Policies', 'Policy Type',
       'Policy', 'Renew Offer Type', 'Sales Channel', 'Total Claim Amount',
       'Vehicle Class', 'Vehicle Size']]

insight=data1.groupby('ranked').mean()
insight






