#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 15:11:17 2021

@author: subham
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("/Users/subham/Desktop/data/360 assignment /data pree processing/DataSets/Z_dataset.csv")
df.describe()
df.head()
df.shape
df.columns
#lets check the featues with zero variance
x=df.describe() 
df.var()
#as we see here are no zero variance

from sklearn.feature_selection import VarianceThreshold

#Featureselector that removes all low-variance features.
 
col_names = ['Id','square.length','square.breadth','rec.Length','rec.breadth']
features = df[col_names] 

df[col_names]
#selecting  the input features

vt = VarianceThreshold()

df[col_names] = vt.fit_transform(features.values)


''' or we can do like this'''

df[col_names] = vt.fit_transform(df[col_names].values)


df[col_names]

df.shape







