#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 17:18:51 2021

@author: subham
"""
'''
There are three datasets given (Facebook, Instagram, and LinkedIn). Construct and visualize the following networks:
circular network for Facebook
star network for Instagram
star network for LinkedIn

'''


import pandas as pd
import numpy as np
import networkx as nx 
import matplotlib.pyplot as plt

df = pd.read_csv("/Users/subham/Desktop/data/360 assignment /network analytics/Datasets_Network Analytics/instagram.csv")
df.shape

# as we see the data here are  in the form of adjacency matrix
#so there is no need to change my data in graph data
df.columns=["a","b","c","d","e","f","g","h"]
df.index=["a","b","c","d","e","f","g","h"]

g=nx.Graph()
nx.info(g)      



#===================================================
G=nx.from_pandas_adjacency(df,create_using=g)
nx.info(G)

#in case of i want to calculate degree of centrality , betwness,or etc etc  
# we can use this G when the raw data already in adjacency matrix form

b = nx.degree_centrality(G)  # Degree Centrality
print(b) 

#=====================================================

GG=nx.to_numpy_matrix(G)   #this will convert my data from graph into matrix form
GG

gg=nx.from_numpy_matrix(GG) #this will convert metrix data into graph
nx.draw(gg,with_labels=1)










