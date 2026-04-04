#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  8 18:21:36 2021

@author: subham
"""
import pandas  as pd
import numpy as np
data= pd.read_csv('/Users/subham/Desktop/data/360 assignment /data pree processing/DataSets/animal_category.csv')
data
data.drop(['Index'],axis=1,inplace=True)
data
#in x data frame getting dummy of every variable

#this will create dummy variable for each columns and separe columns  of each group in a columns

#this will show the output of columns 
x=pd.get_dummies(data)
x



#OneHotEncoder

#this will also work same as get_dummies the only diff is 
#OneHotEncoder won't give column name
from sklearn.preprocessing import OneHotEncoder
ohe=OneHotEncoder()
data.columns
xx=pd.DataFrame(ohe.fit_transform(data.iloc[:,0:]).toarray())
xx




#labelencoder

#here we order our data as per the group ex
#in animal( 1(cat),2(dod))
from sklearn.preprocessing import LabelEncoder
m=LabelEncoder()
dfd=data.iloc[:,1:]

data=m.fit_transform(data.Animals)# this will work on only first columns
data
dfd['Animals']=m.fit_transform(dfd['Animals'])
dfd
dfd['Gender']=m.fit_transform(dfd['Gender'])
dfd['Homly']=m.fit_transform(dfd['Homly'])
dfd['Types']=m.fit_transform(dfd['Types'])

dfd
'''so here we can rank column by column so in one time 
we can rank only only columns, which may  be time consuming'''

#dfd[['Animals','Gender']]=m.fit_transform(dfd[['Animals','Gender']])
''' the above code will not work as it accept only ine dimension array'''




