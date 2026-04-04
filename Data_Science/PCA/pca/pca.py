#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 21 20:37:27 2021

@author: subham
"""
'''
Perform hierarchical and K-means clustering on the 
dataset. After that, perform PCA on the dataset and 
extract the first 3 principal components and make a 
new dataset with these 3 principal components as the 
columns. Now, on this new dataset, perform hierarchical 
and K-means clustering. Compare the results of 
clustering on the original dataset and clustering on
 the principal components dataset (use the scree plot 
technique to obtain the optimum number of clusters 
in K-means clustering and check if you’re getting 
similar results with and without PCA).
'''

import pandas as pd
import numpy as np
data=pd.read_csv("/Users/subham/Desktop/data/360 assignment /PCA/wine.csv")

data
data.shape
data.columns


data.Type.value_counts()
import matplotlib.pyplot as plt
import scipy.cluster.hierarchy as sch
from sklearn.preprocessing import scale 
normal_data=scale(data)

#so herei normalize our data
def normal(i):
    x=(i-i.mean())/(i.max()-i.min())
    return(x)

data1=normal(data.iloc[:,1:])
data1
#now its time to draw dendrogram
from scipy.cluster.hierarchy import linkage
z=linkage(data1,method='complete',metric='euclidean')
z


plt.Figure(figsize=(19,12));plt.xlabel('clusters');plt.ylabel('distance');plt.title('dendrogram')
sch.dendrogram(z,leaf_rotation=0,leaf_font_size=5)



#now create a model
from sklearn.cluster import AgglomerativeClustering


model=AgglomerativeClustering(n_clusters=(3),linkage='complete',affinity='euclidean').fit(data1)
model.labels_
y=model.labels_
#now creating new column#
data['grp']=y=model.labels_
data.columns


#now arranging the column

new_data=data.groupby('grp').mean()
new_data=new_data.drop('Type',axis=1)

data.grp.value_counts()
#now  performing k mean clustering
'''
as my data is completed now lets perform 
kmeans clustering 
lets create scree plote
'''
data2=data
data2=data2.drop(['Type'],axis=1)
def norma(i):
    x=(i-i.mean())/(i.max()-i.min())
    return(x)
normalizedata=norma(data2.iloc[:,:])

from sklearn.cluster import KMeans

wss=[]
k=list(range(1,10))
k
for i in k:
    kmean=KMeans(n_clusters=i)
    kmean.fit(normalizedata)
    wss.append(kmean.inertia_)
    
wss


plt.plot(k,wss,'ro-');plt.title('scree plot')
#as we see my maximum no of data is covered till 4


#now creating the model

mdl=KMeans(n_clusters=3).fit(normalizedata)

zz=mdl.labels_
zz
#now add new col to the data_frame

data2['kmn']=zz=mdl.labels_
#now grouping our data  as per the k mean clustering


newdata2=data2.groupby('kmn').mean()
newdata2

data2.kmn.value_counts()


'''
as we see both the cluster give almost same 
relust i.e k means and hierarical clustering


now performing pca

'''

pdata=pd.read_csv('/Users/subham/Desktop/data/360 assignment /PCA/wine.csv')
pdata
pdata.shape
pdata.isna().sum()
data.duplicated().sum()
wine2=pdata.iloc[:,1:]
wine2
#now normalze out data
from sklearn.preprocessing import scale
noma=scale(wine2)
noma
#now our data is scale freee
from sklearn.decomposition import PCA
#PCA Implementation

pca=PCA(n_components=13)
pca


wine_pca=pca.fit_transform(noma) #pca_value
wine_pca
#here we get pca values


# now to get variance of each col of pcs  contain

vari=pca.explained_variance_ratio_
vari

# Cummulative variance of each PCA
import numpy as np
totvar=np.cumsum(np.round(vari,decimals=4)*100)
totvar



# PCA Components matrix or covariance Matrix
pca.components_
pca.components_[0]

#now variance plot for pca component
plt.plot(totvar,color='red')

pca_data=pd.DataFrame(wine_pca)

pca_data.columns
#now i join the nominal col of the orignal data frame  with the 3 col of my data


pdata.columns


new_dataframe=pd.concat([pdata['Type'],pca_data.iloc[:,0:3]],axis=1)
new_dataframe


#now creating scatter plot to see is there any relationship exist b/w two component




plt.scatter(x=new_dataframe[0],y=new_dataframe[1])
# we see throught the scatter plot that that there\
#is no relationship b/w the two variable


new_dataframe.columns='Type', 'col0','col1','col2'

new_dataframe.columns
#now creating clustering  with this data frame using k means and hierarchichical clustering


new_dataframe.columns



'''
 Now, on this new dataset, perform hierarchical 
and K-means clustering. Compare the results of 
clustering on the original dataset and clustering on
 the principal components dataset (use the scree plot 
technique to obtain the optimum number of clusters 
in K-means clustering and check if you’re getting 
similar results with and without PCA).
'''
new_dataframe
new_dataframe1=new_dataframe

new_dataframe1=new_dataframe1.drop(['Type'],axis=1)

new_dataframe1.shape

import scipy.cluster.hierarchy as sch
from scipy.cluster.hierarchy import linkage

l=linkage(wine_pca,method='complete',metric='euclidean')


plt.Figure(figsize=(20,14));plt.title('dendrogram')
sch.dendrogram(l,leaf_font_size=(18),leaf_rotation=(0))

from sklearn.cluster import AgglomerativeClustering



modelf=AgglomerativeClustering(n_clusters=3,linkage='complete',affinity='euclidean').fit(wine_pca)
md=modelf.labels_

new_dataframe['grouped']=md=modelf.labels_

deso=new_dataframe.groupby(['grouped']).mean()
deso

new_dataframe.grouped.value_counts()

#now performing k means clustering in pca data

n_dataf=new_dataframe.drop(['Type','grouped'],axis=1)

n_dataf

#as we know our data is already normalize we need to create 

wss1=[]
k=list(range(1,10))
k
for i in k:
    kmean=KMeans(n_clusters=i)
    kmean.fit(wine_pca)
    wss1.append(kmean.inertia_)

wss1
plt.plot(k,wss1);plt.title('screeplot')
#taking 3 as cluster
modk=KMeans(n_clusters=3).fit(wine_pca)

km=modk.labels_

new_dataframe['kclus']=km=modk.labels_
grpk=new_dataframe.groupby('kclus').mean()
grpk

new_dataframe.kclus.value_counts()

value1=new_dataframe.iloc[:,4].value_counts()
value1

value2=new_dataframe.iloc[:,5].value_counts()                                                           
value2




















