#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  6 16:00:58 2021

@author: subham
"""
import pandas as pd
import numpy as np
'''Most of the datasets have extreme values or 
exceptions in their observations. These values 
affect the predictions (Accuracy) of the model 
in one way or the other, removing these values is
 not a very good option. For these types of scenarios,
 we have various techniques to treat such values. 
'''
'''Prepare the dataset by performing the preprocessing
 techniques, to treat the outliers.'''

data=pd.read_csv('/Users/subham/Desktop/data/360 assignment /data pree processing/DataSets/boston_data.csv')
data.shape
x=data.describe()
x

data.columns

#converting into intizer
data[['crim', 'zn', 'indus', 'chas', 'nox', 'rm', 'age', 'dis', 'rad', 'tax',
       'ptratio', 'black', 'lstat', 'medv' ]] = data[['crim', 'zn', 'indus', 'chas', 'nox', 'rm', 'age', 'dis', 'rad', 'tax',
       'ptratio', 'black', 'lstat', 'medv']].astype('int64')
data.dtypes
x1=data.duplicated()# lets check for the duplicated 
d=x1.sum()
d
#as we know there is noo duplicate in the data
#we neet to move ahed to check outliers
#========================outlier=========================
#1 boxplot
import matplotlib.pyplot as plt
import seaborn as sns

data.columns

data.dtypes
data.shape

def outtreat(data,col_name):
    data.boxplot(column=[col_name])
    plt.show()

#now to check which all column are having outlier

outtreat(data,'crim')
outtreat(data,'zn')
outtreat(data,'indus') #no outlier
outtreat(data,'chas')#categorical variable
outtreat(data,'nox')#nooutlier
outtreat(data,'rm')#noooutlier
outtreat(data,'age')#nooutlier
outtreat(data,'dis')
outtreat(data,'rad')#nooutlier
outtreat(data,'tax')#no outlier
outtreat(data,'ptratio')
outtreat(data,'black')
outtreat(data,'lstat')
outtreat(data,'medv')


plt.boxplot(data[[ 'crim','zn', 'rm','dis','ptratio', 'black', 'lstat', 'medv']])


# as we see there is no out lier in age col  we can also delete it
#as we see there are 7 columns in which outlier is present
#'crim', 'zn', 'rm', 'dis','ptratio', 'black', 'lstat', 'medv'    
#to find which all columns contain outliers


'''
how to make it in loop????
for x in range(0,10):
    y=x+1
    plt.boxplot(data.iloc[:,y])
    print(y)

'''       

       
#now we have to find iqr
iqr=data.crim.quantile(0.75)-data.crim.quantile(0.25)
iqr
upper_limit=data.crim.quantile(0.75)+(iqr*1.5)
upper_limit

lower_limit=data.crim.quantile(0.25)-(iqr*1.5)
lower_limit


#outlier techniques = remove ,replace ,winsorize

# remove
x=np.where(data.crim>upper_limit,True,np.where(data.crim<lower_limit,True,False))
x
data=data.assign(x=np.where(data.crim>upper_limit,True,np.where(data.crim<lower_limit,True,False)))
data
# to count the frequency of outlier
data.x.value_counts()
#so there are the rows containing the outlier
k=np.where(data.x==True)
k

xx=data.loc[[ 10,  14,  17,  34,  49,  50,  60,  62,  89, 114, 116, 138, 141,143, 149, 167, 170, 173, 177, 179,
             180, 184, 207, 209, 225, 246,258, 260, 261, 273, 
             281, 282, 285, 304, 316, 355, 377, 379, 380,400],['crim','x']]

xx
#===============now trimming out====================

data=data.loc[~(x), ]
data

# now lets check what all are the changes is made

data.shape
xl=data.loc[:,:]

import seaborn as sns
sns.boxplot(xl.crim)

#we see still there are outlier present in the the data

#now we use===================== replace =================technique==============
# now we replace it with mixima and minima

#imp note run the data (data frame ) 
#so that it cant be applied on the operated data

data=pd.read_csv('/Users/subham/Desktop/data/360 assignment /data pree processing/DataSets/boston_data.csv')


data['rep']=pd.DataFrame(np.where(data.crim > upper_limit, upper_limit,
                                  np.where(data.crim<lower_limit, lower_limit,
                                           data.crim)))

data
sns.boxplot(data.rep)


#victory🥵
#as we see now there is no outlier i my data

#plt.boxplot(data[[ 'crim','zn', 'rm','dis','ptratio', 'black', 'lstat', 'medv']])
#=============================zn'=======================

#data=pd.read_csv('/Users/subham/Desktop/data/360 assignment /data pree processing/DataSets/boston_data.csv')

data.zn
data
data.shape

# Detection of Outliers
iqr=data.zn.quantile(0.75)-data.zn.quantile(0.25)
iqr
upper=data.zn.quantile(0.75)+(iqr*1.5)
upper
lower=data.zn.quantile(0.25)-(iqr*1.5)
lower
#so lets go wth the replacing technique

data['zn_rep']=pd.DataFrame(np.where(data.zn>upper,upper,np.where(data.zn<lower,lower,data.zn)))
data
data.zn_rep

sns.boxplot(data.zn_rep)


#so here my data has no out lier
#movint to the next columns========rm=================
#tring with winsorization
from feature_engine.outliers import Winsorizer
#Detection of Outliers
data.rm
data.shape
data.rm.shape
iqr=data.rm.quantile(0.75)-data.rm.quantile(0.25)
iqr
upper1=data.rm.quantile(0.75)+(iqr*1.5)
upper1
lower1=data.rm.quantile(0.25)-(iqr*1.5)
lower1

winso=Winsorizer(capping_method='iqr',tail='both',fold=1.5,variables=['rm'])
winso
df_t = winso.fit_transform(data[['rm']])

data=data.assign(df_t = winso.fit_transform(data[['rm']]))
data
sns.boxplot(data.df_t)

# so here my column rm is outlier free 


########MOVING FOR THE NEXT COLUMN 
#================='dis'==========================
data.dis
iqr=data.dis.quantile(0.75)-data.dis.quantile(0.25)
upper11=data.dis.quantile(0.75)+iqr*1.5
lower11=data.dis.quantile(0.35)-iqr*1.5

from feature_engine.outliers import Winsorizer
wino=Winsorizer(capping_method='iqr',tail='both',fold=1.5,variables=['dis'])

newdis=wino.fit_transform(data[['dis']])
data=data.assign(newdis=wino.fit_transform(data[['dis']]))
data
sns.boxplot(data.newdis)

#no outlier here in new dis
#####================='ptratio'==========================

iqr=data.ptratio.quantile(0.75)-data.ptratio.quantile(0.25)
low=data.ptratio.quantile(0.25)-iqr*1.5
high=data.ptratio.quantile(0.75)+iqr*1.5

win=Winsorizer(capping_method='iqr',tail='both',fold=1.5,variables=['ptratio'])
newpet=win.fit_transform(data[['ptratio']])
data=data.assign(newpet=win.fit_transform(data[['ptratio']]))
data.newpet
sns.boxplot(data.newpet)

#ptratio is now outlier free


#####================='black'==========================



iqr=data.black.quantile(0.75)-data.black.quantile(0.25)
low=data.black.quantile(0.25)-iqr*1.5
high=data.black.quantile(0.75)+iqr*1.5

wi=Winsorizer(capping_method='iqr',tail='both',fold=1.5,variables=['black'])
newblack=wi.fit_transform(data[['black']])
data=data.assign(newblack=wi.fit_transform(data[['black']]))
data.newblack
sns.boxplot(data.newblack)

#####================='lstat'==========================


iqr=data.lstat.quantile(0.75)-data.lstat.quantile(0.25)
low=data.lstat.quantile(0.25)-iqr*1.5
high=data.lstat.quantile(0.75)+iqr*1.5

w=Winsorizer(capping_method='iqr',tail='both',fold=1.5,variables=['lstat'])
newlstat=w.fit_transform(data[['lstat']])
data=data.assign(newlstat=w.fit_transform(data[['lstat']]))
data.newlstat
sns.boxplot(data.newlstat)



#####================='medv'==========================

data

iqr=data.medv.quantile(0.75)-data.medv.quantile(0.25)
hi=data.medv.quantile(0.75)+iqr*1.5
lo=data.medv.quantile(0.25)-iqr*1.5

from feature_engine.outliers import Winsorizer
wo=Winsorizer(capping_method='iqr',tail='both',fold=1.5,variables=['medv'])
data['new_medv']=pd.DataFrame(wo.fit_transform(data[['medv']]))
data
sns.boxplot(data.new_medv)

'''so finally our all the columns are outlier free so we can 
drop the columns which contain outlier and keep the new transformed columns
'''

plt.boxplot(data[['zn_rep', 'df_t', 'newdis',
       'newpet', 'newblack', 'newlstat', 'new_medv']])










