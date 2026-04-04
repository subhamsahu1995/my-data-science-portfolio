#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Oct 18 23:38:17 2021

@author: subham
"""


import numpy as np
import pandas as pd
import networkx as nx

data=pd.read_csv("/Users/subham/Desktop/data/360 assignment /network analytics/Datasets_Network Analytics/facebook.csv")
data.shape

data.columns=["a","b","c","d","e","f","g","h","i"]
data.index=["a","b","c","d","e","f","g","h","i"]


g=nx.Graph()

G= nx.from_pandas_adjacency(data,create_using=g)
nx.info(G)

gg=nx.to_numpy_matrix(G)
gg

GG=nx.from_numpy_matrix(gg)
nx.draw(GG,with_labels=1)




