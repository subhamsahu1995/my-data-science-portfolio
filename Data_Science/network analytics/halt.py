#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 14 02:26:04 2021

@author: subham
"""


'''
There are two datasets consisting of information for the connecting
routes and flight halt. Create network analytics models on both the
datasets separately and measure degree centrality, degree of closeness 
centrality, and degree of in-between centrality.
Create a network using edge list matrix (directed only).
Columns to be used in R:

Flight_halt=c("ID","Name","City","Country","IATA_FAA","ICAO","Latitude","Longitude",
              "Altitude","Time","DST","Tz database time")
'''
x=("ID","Name","City","Country","IATA_FAA","ICAO","Latitude","Longitude",
              "Altitude","Time","DST","Tz database time")
j=0
for i in x:
    print((i))
    j=j+1
    print(j)

#just to check how many no of columns do we have 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import networkx as nx


data=pd.read_csv("/Users/subham/Desktop/data/360 assignment /network analytics/Datasets_Network Analytics/flight_hault.csv",sep = ',', header=0)
data.shape
print(data)

#assigning column name to the respective columns
data.columns=["ID","Name","City","Country","IATA_FAA","ICAO","Latitude","Longitude","Altitude","Time","DST","Tz database time"]




g = nx.from_pandas_edgelist(data, source = 'IATA_FAA', target = 'ICAO')
#converting it to graphdata

nx.info(g)



#number of nodes=12650 (airport)
#number of edges=7382 (no of  connection with other)
''' visualization'''



#we cab escpe data visualization part as it takes much time to read

ll=nx. draw(g)


aa=nx.to_numpy_matrix(g)
aa
#just to see matrix 



kk=nx.from_numpy_matrix(aa)
nx.draw(kk)
# to see the graph of the matrix we use nx.from_numpy_matrix()




pos = nx.spring_layout(g, k = 0.15)#what type of layout  we want
nx.draw_networkx(g,pos, node_size = 25, node_color = 'g')


dc=nx.degree_centrality(g)
print(dc)



for i in sorted(dc,key=dc.get,reverse=True):
    print(i,dc[i])
    
#so we can say that AIRPORT "VRMO"HAS has maximum direct connection with other airport
    
 #now see the plot
   
pos = nx.spring_layout(dc, k = 0.15)#what type of layout  we want
nx.draw_networkx(dc,pos, node_size = 25, node_color = 'g')


#degree of closeness

clsc=nx.closeness_centrality(g)
print(clsc)

for i in sorted(clsc,key=clsc.get,reverse=True):
    print(i,clsc[i])

pos = nx.spring_layout(clsc, k = 0.15)#what type of layout  we want
nx.draw_networkx(clsc,pos, node_size = 25, node_color = 'g')



bt=nx.betweenness_centrality(g)
print(bt)

nx.draw(bt)









