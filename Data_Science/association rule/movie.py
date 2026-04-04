#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 30 01:01:43 2021

@author: subham
"""
import pandas as pd

from mlxtend.frequent_patterns import apriori,association_rules
import matplotlib.pyplot as plt
data=pd.read_csv("/Users/subham/Desktop/data/360 assignment /association rule/Datasets_Association Rules/my_movies.csv")

movie_data=data.iloc[:,5:]

# with 10% support & 90 % confidence
frequent_itemsets=apriori(movie_data,min_support=0.1,use_colnames=True)
frequent_itemsets.sort_values('support', ascending = False, inplace = True)
#it says  about the frequency that gladiator  ha almost 70% of the data



#presending in frequencies
plt.bar(x = list(range(0, 11)), height = frequent_itemsets.support[0:11], color ='rgmyk')
plt.xticks(list(range(0, 11)), frequent_itemsets.itemsets[0:11], rotation = "vertical")
plt.xlabel('item-sets')
plt.ylabel('support')
plt.show()


rules=association_rules(frequent_itemsets,metric='lift',min_threshold=0.9)

mm=rules.sort_values('lift',axis=0,ascending=False)
rules.sort_values('lift',ascending=False,inplace=(True))


#as we see here there many repetative rules in my data set so we need to remove those rules 

def dup(i):
    return(sorted(list(i)))

xx=rules.antecedents.apply(dup)+rules.consequents.apply(dup)

xx=xx.apply(sorted)

rules_set=list(xx)


unique_rules_sets = [list(m) for m in set(tuple(i) for i in rules_set)]


index_rule=[]


for i in unique_rules_sets:
    index_rule.append(unique_rules_sets.index(i))
    
sbm= rules.iloc[index_rule, :]
sbm.sort_values('lift',ascending=False,inplace=True)
sbm_data=sbm.head(11)

'''
 as we see the repetative rules are removed 
 so we can say that , if the distributer arrange his collecton  as per the model 
 there are the chances of miximise sale . as the previous data 
 show about the customer choicess 
'''

