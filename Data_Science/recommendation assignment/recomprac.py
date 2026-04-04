#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  5 21:18:36 2021

@author: subham
"""
#so business problem is to recommend movies based on siilarity

import pandas as pd
import numpy as np
anime1 = pd.read_csv("/Users/subham/Desktop/data/class_360/Recommender Dataset/anime.csv", encoding = 'utf8')
anime1.shape
anime1.isna().sum()
data=anime1.genre.isna()
data


#x=anime1.loc[:,['genre', 'type', 'episodes']]
# so as we know there are missing values in genre sp
anime1["genre"] = anime1["genre"].fillna(" ")

anime1.genre.isna().sum()
#now nothing is missing
from sklearn.feature_extraction.text import TfidfVectorizer

#to transfer from text to feature vector

tfidf=TfidfVectorizer(stop_words=('english'))
print(tfidf)
#here i am stopping  uninformative words so that is weight can't be calculated


#to convert it into matrix by fit_transform


tfidf_matrix = tfidf.fit_transform(anime1.genre) 
#Transform a count matrix to a normalized tf or tf-idf
# representation

tfidf_matrix.shape
# it has creteated weighted column for every element
# as we see here the no of columns increased to 46

# now we have to imort package for calaulate similarity
# are are usig cosine sililarity
from sklearn.metrics.pairwise import  linear_kernel

cosine_matrix=linear_kernel(tfidf_matrix,tfidf_matrix)

'''
#now dropping repeated movies name
anime1.name.duplicated().sum()
anime1.name=anime1.drop_duplicates()
'''

movie_index=pd.Series(anime1.index,index=anime1["name"]).drop_duplicates()


movie_id = movie_index["Assassins (1995)"]


movie_id




# here it has indexing all the movie and then  removing duplicated movie


# now i have to define a function in which user has to pass the movie name and will 
# recommend atleast 10 movies semilar to it

def recom(name,topn):
    movie_id=movie_index[name]
    #here we are getting index of the movie
    cosine_score=list(enumerate(cosine_matrix[movie_id]))
    cosine_score=sorted(cosine_score,key=lambda x:x[1],reverse=True)
    cosine_score_n=cosine_score[0:topn+1]
    #getting movie index and movie score
    movieidx=[i[0]for i in cosine_score_n]
    moviescore=[i[1]for i in cosine_score_n]
    #now converting into dataframe
    movie_similar=pd.DataFrame(columns=['name','score'])
    movie_similar['name']=anime1.loc[movieidx,'name']
    movie_similar['score']=moviescore
    movie_similar.reset_index(inplace=True)
    print(movie_similar)
 
    
 
    
#now calling function
recom('Nell (1994)',10)
    
    
    
    
    
    
    
    
    































