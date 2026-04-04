#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 19 20:17:14 2021

@author: subham
"""

'''
Majority of the datasets have missing values, that might
be because the data collected were not at regular intervals
 or the breakdown of instruments and so on. It is nearly 
 impossible to build the proper model or in other words, 
 get accurate results. The common techniques are either 
 removing those records completely or substitute those missing
 values with the logical ones, there are various techniques 
 to treat these types of problems.
 
Prepare the dataset using various techniques to solve the 
problem, explore all the techniques available and use them 
to see which gives the best result.
'''
import pandas as pd
import numpy as np
import sklearn as sk

data=pd.read_csv("/Users/subham/Desktop/data/360 assignment /data pree processing/DataSets/claimants.csv")

data2=pd.read_csv("/Users/subham/Desktop/data/360 assignment /data pree processing/DataSets/claimants.csv")


data.isna().sum()

data.loc[:,['CLMSEX','CLMINSUR','SEATBELT','CLMAGE']].isna().sum()

#the columns in which values are missing are
#'CLMSEX','CLMINSUR','SEATBELT','CLMAGE'
from sklearn.impute import SimpleImputer
si=SimpleImputer(missing_values=np.nan,strategy="median")
data.CLMAGE=pd.DataFrame(si.fit_transform(data[['CLMAGE']]))
data.CLMAGE.isna().sum()
#now clmage is filled with median value that is 30

data[['CLMSEX','CLMINSUR','SEATBELT']]=data[['CLMSEX','CLMINSUR','SEATBELT']].interpolate(method='linear',limit_direction='forward')

data[['CLMSEX','CLMINSUR','SEATBELT']].isna().sum()


#lets see is there any missing value 
data.isna().sum()
#there no missing value left






