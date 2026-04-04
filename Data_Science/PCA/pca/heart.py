#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 22 22:36:42 2021

@author: subham
"""
'''
A pharmaceuticals manufacturing company is conducting a
 study on a new medicine to treat heart diseases. 
 The company has gathered data from its secondary 
 sources and would like you to provide high level 
 analytical insights on the data. Its aim is to 
 segregate patients depending on their age group and 
 other factors given in the data. Perform PCA and
 clustering algorithms on the dataset and check if the 
 clusters formed before and after PCA are the same and 
 provide a brief report on your model. You can also 
 explore more ways to improve your model. 

Note: This is just a snapshot of the data. 
The datasets can be downloaded from AiSpry LMS in the Hands-On
 Material section. 
''' 
 
import pandas as pd
import numpy as np 
 
data =pd.read_csv('/Users/subham/Desktop/data/360 assignment /PCA/heart disease.csv')
data 
 
data.shape
data.dtypes
data.duplicated().sum()
#as we see here is one duplicated value so lets remove it

data=data.drop_duplicates()

from sklearn.preprocessing import scale

#now lets normalize our data

def nom(i):
    x=(i-i.mean())/(i.max()-i.min())
    return(x)

normal=nom(data.iloc[:,:])
normal
#now to perform clustering
#1hierarichal 
#2kmeans
data2=data
data2=data2.iloc[:,[0,2,3,4,5,6,7,8,9,10,11,12,13]]
 
#now create dendrogram 
import scipy.cluster.hierarchy as sch 
from scipy.cluster .hierarchy import linkage 
import matplotlib.pyplot as plt 
x=linkage(normal,method='complete',metric='euclidean')
x 
plt.figure(figsize=(30,15));plt.title('dendrogram')
sch.dendrogram(x,leaf_rotation=(0),leaf_font_size=8) 
#taking 4 as a no of cluster
from sklearn.cluster import AgglomerativeClustering
model=AgglomerativeClustering(n_clusters=(3),linkage='complete',affinity='euclidean').fit(normal)
y=model.labels_ 
#now creating group 
data['gro']=y=model.labels_ 

data.columns
data=data[['gro','age', 'sex', 'cp', 'trestbps', 'chol', 'fbs', 'restecg', 'thalach','exang', 'oldpeak', 'slope', 'ca', 'thal', 'target']]
newdata=data.groupby('gro').mean() 


#now performing kmean clustering
data.columns

kdata=data.drop(['gro','sex'],axis=1)
kdata.dtypes
kdata.oldpeak=kdata.oldpeak.astype('int64')
nomk=nom(kdata)
nomk
#now creating screeplot
from sklearn.cluster import KMeans

wss=[]
k=list(range(1,10))
k
for i in k:
    kmean=KMeans(n_clusters=i)
    kmean.fit(nomk)
    wss.append(kmean.inertia_)
    
wss
 
plt.plot(k,wss,'ro-');plt.title('screeolot')

#as we see the maximum no data is covered till cluster 4
modelk=KMeans(n_clusters=3).fit(nomk)
xx=modelk.labels_
#convering into data frame
kdata['kmn']=xx=modelk.labels_
newgrp=kdata.groupby('kmn').mean()
newgrp

#performing pca in the dataset
pdata=pd.read_csv('/Users/subham/Desktop/data/360 assignment /PCA/heart disease.csv')
pdata.shape

from sklearn.decomposition import PCA
pnorm=scale(pdata.iloc[:,[0,2,3,4,5,6,7,8,9,10,11,12,13]])

pca=PCA(n_components=(13))
pca

pca_value=pca.fit_transform(pnorm)
pca_value

pca.components_
#now getting the variance of each column
var=pca.explained_variance_ratio_
var
#now getting commulative variance

totvar=np.cumsum(np.round(var,decimals=4)*100)
totvar

#now plotting variance for getting pca components
plt.plot(totvar,color='red')


#as we see till 3 component it cover most range of data

pcadata=pd.DataFrame(pca_value)

new_dataframe=pcadata.iloc[:,:3]

new_dataframe.columns='col0','col1','col2'

new_dataframe.columns

#now lets see is there in correlatin there b/w the columns
plt.scatter(x=new_dataframe['col0'],y=new_dataframe['col1'])
#========================================================================
'''now performing clustering using pca dataset'''

new_dataframe.shape

ndnorm=scale(new_dataframe)
from scipy.cluster.hierarchy import linkage
import scipy.cluster.hierarchy as sch
#making dendrogram
ll=linkage(ndnorm,method='complete',metric='euclidean')
ll
sch.dendrogram(ll,leaf_rotation=(0),leaf_font_size=9)

#from the dendrograph i can select 3 cluster
#now creating the model
from sklearn.cluster import AgglomerativeClustering
hmodel=AgglomerativeClustering(n_clusters=(3),linkage='complete',affinity='euclidean').fit(ndnorm)
h=hmodel.labels_
ndf=new_dataframe
ndf['grop']=h=hmodel.labels_
ndf
findata=pd.concat([data['age'],ndf],axis=1)

nfd=findata.groupby('grop').mean()





