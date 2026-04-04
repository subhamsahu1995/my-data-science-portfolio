#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  4 13:42:05 2021

@author: subham
"""

#here we are dealing with gaiming data and we have 
#to deal it with  content based filtering

import pandas as pd
import numpy as np


gamedata=pd.read_csv("/Users/subham/Desktop/data/360 assignment /recommendation assignment/Datasets_Recommendation Engine/game.csv",encoding = 'utf8')
gamedata.shape

gamedata.columns
gamedata.dtypes
gamedata.rating.isna().sum()

gamedata.columns=['userid', 'game', 'rating']
#here i have just changed the name for convinence               

#sorting it by useID
srted_id=gamedata.sort_values('userid',axis=0)
'''taki pata chale  kitna user id kitna diff diff game ko rating dia h'''

srted_id.game.duplicated().sum()
#1562
#we find that there are many repetative games

srted_id.userid.duplicated().sum()
#1739
#here we see that in user there are 1789  repetative user id who 
#reviewed the diff diff movie


#no of unique games
len(srted_id['userid'].unique())
#3261
len(srted_id['game'].unique())

uniqueid=len(srted_id['userid'].unique())
'''
#3261
len(srted_id.game.unique())
#3438
a=3438+1562    #(unique + duplicate just to check=total)
print(a)
'''
'''
#converting long data to wide data using pivot
What’s the difference?   Unlike “Big” Data, “Wide” Data applies
to the typical organization that is more often concerned with 
#tying together data from disparate sources, often a wide range
of sources and thus the name, for meaningful analysis. 
Unlike the “big” in big data, wide data can be large or small.
'''

#using pivot converting long data to wide data using pivot
game2=srted_id.pivot_table(index='userid',columns='game',values='rating').reset_index(drop=True)
'''
as we know we have taken 'userid' as an index  in pivot, reset_index : it will 
create a new column with name 'userid' which can be considerd as an index.
so  as of now we drop that  column using drop=True just to hide it.
reset_index  used becase in the above step we will actually convert the index with with userid.
''' 
# just for understanding if we don't use drop=True in  reset_index()


'''game22=srted_id.pivot_table(index='userid',columns='game',values='rating').reset_index()'''




#here replacing my game2 index by unique index
game2.index=srted_id['userid'].unique()
# we do't find index 4 because there is no userid with 4


#now i am filling the nan value with "blank" so that it cannot be included in 
game2.fillna(0,inplace=True)

#alternative way we can replace

'''new=game2.replace(to_replace= 'Nan',value=' ') we can also fill it with blank'''

from sklearn.metrics import pairwise_distances
from scipy.spatial.distance import cosine, correlation


# Calculating Cosine Similarity between Users on array data
user_sim=1-pairwise_distances(game2.values,metric='cosine')
user_sim

#it will give me calculated cosine score 

#now creating it to dataframe

user_sim2=pd.DataFrame(user_sim)
user_sim2


# Set the index and column names to userid in dataframe
user_sim2.index=gamedata['userid'].unique()
user_sim2.columns=gamedata['userid'].unique()
user_sim2

#to find  the similarity  b/w userid and game 




# Slicing first 10 rows and first 10 columns
sample=user_sim2.iloc[:10,:10]

#as we know the corelation is high within the same users

# Nullifying diagonal values
np.fill_diagonal(user_sim,0)


sample2=user_sim2.iloc[0:10,0:10]


# Most Similar Users


user_sim2.idxmax(axis=1)[0:5]  # (idxmax) Returns index of the maximum element
#it will give the highly corelation between the users
# here i am asking for top 5 corelated (simillar)user

# extract the game which userId 6 &  have watched (we can take any index)
yy=gamedata[(gamedata['userid']==6) | (gamedata['userid']==6964)]   # | means &
# it will give which all games liked by userid 6 and userid 168


user_1=gamedata[(gamedata['userid']==6)]
user_2=gamedata[(gamedata['userid']==6964)]

user_1['game']

user_2['game']


mrg=pd.merge(user_1,user_2,on='game',how='outer')
mrg

# so here i come to the conclusion that 
'''
the next game for userid 6 will be Dyad
and the next game for userid 6964	
Tony Hawk's Pro Skater 2
'''













# so here we get the conclusion  that 
#for userid 6 the next recommended movies will be:
#   Dyad ,James Bond 007 etc.
#for user i    
