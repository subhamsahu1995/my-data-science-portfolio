#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 22:19:08 2021

@author: subham
"""
'''
Create network analytics models on both the datasets separately
and measure degree centrality, degree of closeness centrality, 
and degree of in-between centrality.

connecting routes=c("flights", " ID", "main Airport”, “main Airport ID",
                    
"Destination ","Destination  ID","haults","machinary")

'''
import pandas as pd
import networkx as nx
import numpy as np
import matplotlib.pyplot as plt
data=pd.read_csv("/Users/subham/Desktop/data/360 assignment /network analytics/Datasets_Network Analytics/connecting_routes.csv")
data.columns
#keeping only required columns
data=data.loc[:,['2B', '410', 'AER', '2965', 'KZN', '2990','CR2']]
data.shape
#assigning names to the columns
data.columns=["flights", " ID", "main Airport", "main Airport id","Destination ","Destination  ID","haults"]
data.columns

#now converting this data to graph data
g=nx.from_pandas_edgelist(data,source='main Airport',target="Destination ")
nx.info(g)

nodes=nx.nodes(g)
len(nodes)
edges=nx.edges(g)
len(edges)

#to see the matrix
m=nx.to_numpy_matrix(g)
m

#now to draw graph 
pos=nx.spring_layout(g,k=0.15)
nx.draw_networkx(g,pos,node_color="g")

 
dc=nx.degree_centrality(g)
dc
#now sorting it to see which route has the maximum no of direct connectiom
for i in sorted(dc,key=dc.get,reverse=True):
    print(i,dc[i])
    
cc=nx.closeness_centrality(g) 
cc   
 
#BZO 0.0002920560747663551
# to see which is having the max no of closeness connection  with others  
for i in sorted(cc,key=cc.get,reverse=True):
    print(i,dc[i])


bc=nx.betweenness_centrality(g)
bc

# to see which station has the maximum no of intersection  with others flight

for i in sorted(bc,key=bc.get,reverse=True):
    print(i,bc[i])


