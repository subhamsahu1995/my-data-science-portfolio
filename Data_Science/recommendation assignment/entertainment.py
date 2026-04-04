#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  9 23:09:25 2021

@author: subham
"""


# here we are applying content based recommendation

'''

The Entertainment Company, which is an online movie watching 
platform, wants to improve its collection of movies and showcase 
those that are highly rated and recommend those movies to its 
customer by their movie watching footprint. For this, the company
has collected the data and shared it with you to provide some 
analytical insights and also to come up with a recommendation
algorithm so that it can automate its process for effective
recommendations. The ratings are between -9 and +9

'''

import pandas as pd
import numpy as np
data=pd.read_csv('/Users/subham/Desktop/data/360 assignment /recommendation assignment/Datasets_Recommendation Engine/Entertainment.csv',encoding = 'utf8')
data.duplicated().sum()
data.columns

from sklearn.feature_extraction.text import TfidfVectorizer
# used  as: inverse frequency is created to calculate so that  to get weightage of a term column

tfidf=TfidfVectorizer(stop_words='english')
# to stop the unwanted words as each words have some value 
data.Category.isna().sum()

# here we see no missing value so that 

tfidf_matrix1=tfidf.fit_transform(data.Category)




tfidf_matrix1.shape
print(tfidf_matrix1)

len(data.Category.unique()) #unique genre

'''
for each 'Category'  separate separate  column is formed and then tfidf(weitage) is calculated for :
each movie. and column is taken to check importance of term in 
with each movie if the term is not persent it will give the weitage as zero
'''   

from sklearn.metrics.pairwise import linear_kernel
#this package is used for calculating cosine semilarity

 
#now computing cosine similarity on my tfidf metric
#to find weight to calculate similarity 
cosine_mat=linear_kernel(tfidf_matrix1,tfidf_matrix1)
cosine_mat

len(data.Titles.unique()) # here we see alll the movies are unique

data.Titles.duplicated().sum()   # just cross checking
'''
# creating a mapping of movie name to index number 
becuse when the user will enter any movie name he can get 
recommendation where the score was calculated b/w the ids 
that is why i am creating an id as per unique movie name
'''

#it will give unique index no to all unique movie 
movie_inde=pd.Series(data.index,index=data['Titles']).drop_duplicates()



# lets get movie index by giving the name
movieid=movie_inde["Waiting to Exhale (1995)"]
movieid


# now we are defining the function in which it will take the 
#movie name and give recommended
def recom(Titles,topn):
    movieid=movie_inde[Titles]# to get the indexd after entering the name
    cosine_score=list(enumerate(cosine_mat[movieid]))
    #here i am getting cosinescore of the movie related to it fit 
    #by the user
    cosine_score=sorted(cosine_score,key=lambda x:x[1],reverse=True)
    
    # here we sorted because i want top 10 movies relate to it
    top10=cosine_score[0:topn+1]
    #index n-1 that is why  n+1
    movieindex=[i[0] for i in top10]
    movie_scor=[i[1] for i in top10]
    #now i am converting it to dataframme
    movie_simila=pd.DataFrame(columns=["moviename", "score"])
    #here i want my data_dataframe with two column
    #next i have define the column value 
    movie_simila['moviename']=data.loc[movieindex,'Titles']
    movie_simila['score']=movie_scor
    
    movie_simila.reset_index(inplace=True)
    
    print(movie_simila)
    
#now calling finction



   
recom(('Powder (1995)'),topn=10)

'''so my next movies will nixon ,Money Train etc etc'''

    
    
    
    













