#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 20 18:08:32 2021

@author: subham
"""
import pandas as pd
import numpy as np
from scipy import stats 
'''
Calculate Mean, Median, Mode, Variance, Standard Deviation, 
Range & comment about the values / draw inferences,
for the given dataset
For Points, Score, Weigh>
'''



data=pd.read_excel('/Users/subham/Desktop/data/360 assignment /data pree processing/Assignment_module02.xlsx')
data
data.columns
data.Points.mean()
mean=data[['Points', 'Score', 'Weigh']].mean()
median=data[['Points', 'Score', 'Weigh']].median()

data[['Points', 'Score', 'Weigh']].mode()

data[['Points', 'Score', 'Weigh']].mode()

stats.mode(data[['Points', 'Score', 'Weigh']])

data[['Points', 'Score', 'Weigh']].var()
data[['Points', 'Score', 'Weigh']].std()

x=data[['Points', 'Score', 'Weigh']].min()
y=data[['Points', 'Score', 'Weigh']].max()
raneg=(y-x)
raneg

data.skew()

data.kurtosis()
'''
the skewness is between -0.5 and 0.5, 
the data are fairly symmetrical

and the data are normally distributed
'''




