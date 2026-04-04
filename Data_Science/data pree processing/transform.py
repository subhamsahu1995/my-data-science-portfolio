#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 18:12:48 2021

@author: subham
"""
'''
Prepare the dataset by performing the preprocessing techniques,
to have the data which improve model performance.
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("/Users/subham/Desktop/data/360 assignment /data pree processing/DataSets/calories_consumed.csv")
df.describe()
df.head()

#Minmaxscalar x_scaled = (x – x_min)/(x_max – x_min)
from sklearn.preprocessing import MinMaxScaler

'''
For each value in a feature, MinMaxScaler subtracts
 the minimum value in the feature and then divides by
 the range. The range is the difference between the 
 original maximum and original minimum.																									
'''

df_scaled = df.copy()
df_scaled
col_names = ['Weight gained (grams)','Calories Consumed']
features = df_scaled[col_names]

scaler = MinMaxScaler()
df_scaled[col_names] = scaler.fit_transform(features.values)
df_scaled


#standardization


from sklearn.preprocessing import StandardScaler
scaler = StandardScaler()

df_scaled[col_names] = scaler.fit_transform(features.values)
df_scaled


#maxAbsSclar

from sklearn.preprocessing import MaxAbsScaler
scaler = MaxAbsScaler()

df_scaled[col_names] = scaler.fit_transform(features.values)
df_scaled

#robustScalar

from sklearn.preprocessing import RobustScaler
scaler = RobustScaler()

df_scaled[col_names] = scaler.fit_transform(features.values)
df_scaled



from sklearn.preprocessing import QuantileTransformer
scaler = QuantileTransformer()

df_scaled[col_names] = scaler.fit_transform(features.values)
df_scaled


# we can say that basicall while we transform our data  it convert it into the range 0 to 1






