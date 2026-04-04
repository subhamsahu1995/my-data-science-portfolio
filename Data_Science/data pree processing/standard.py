#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Oct 20 17:40:33 2021

@author: subham
"""
'''
Prepare the dataset by performing the preprocessing 
techniques, to have the standard scale to data
'''



import pandas as pd
import matplotlib.pylab as plt

seeds = pd.read_csv("/Users/subham/Desktop/data/360 assignment /data pree processing/DataSets/Seeds_data.csv")
seeds.shape

seeds.head()

seeds.describe()

seeds.info()

seeds = seeds.drop(["Type"], axis=1)
seeds.info()

#dropping type col because it is not much requires

# Normalization function 
def norm_func(i):
    x = (i-i.min())	/ (i.max()-i.min())
    return (x)
# Normalized data frame (considering the numerical part of data)
df_norm = norm_func(seeds.iloc[:, 1:])

df_norm.describe()
