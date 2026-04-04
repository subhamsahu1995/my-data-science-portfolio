#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct  1 14:57:25 2021

@author: subham
"""

import pandas as pd
from mlxtend.frequent_patterns import apriori,association_rules
with open('/Users/subham/Desktop/data/360 assignment /association rule/Datasets_Association Rules/transactions_retail1.csv') as f:
    trans=f.read()
    #here i am separating my data with new lines
trans=trans.split('\n')

#here i am spliting it with ',' and storing it in trans_data
trans_data=[]   
for i in trans:
    s=i.split(',')
    trans_data.append(s)

#here i am separing each elemet 
all_trans_data=[]    
for i in trans_data :
    for k in i:
        all_trans_data.append(k)
        

from collections import Counter
frequency=Counter(all_trans_data)


trans_freq=sorted(frequency.items(),key=lambda x:x[1])

freq= list(sorted([i[1]for i in trans_freq]))
item=list(sorted([i[0]for i in trans_freq]))

#now lets create  bar plot
import matplotlib.pyplot as plt
plt.bar(height = freq[0:11], x = list(range(0, 11)), color = 'rgbkymc')
plt.xticks(list(range(0, 11), ), item[0:11])
plt.xlabel("items")
plt.ylabel("Count")
plt.show()

#now creating dataframe
from mlxtend.preprocessing import TransactionEncoder
tedata=TransactionEncoder()
te=tedata.fit_transform(trans_data)

data=pd.DataFrame(te,columns=(tedata.columns_))   
data.columns
data.shape
y=data.isna().sum()
y
new_data=data.drop(y,axis=1)

new_data.shape
new_data.columns
new_data=new_data.iloc[:,2:]


frequent_items=apriori(new_data,min_support=0.05,use_colnames=(True),max_len=(10))


frequent_items.sort_values('support',ascending=False,inplace=True)

import matplotlib.pyplot as plt
plt.bar(x=list(range(0,10)), height=frequent_items.support[0:10],color ='rgmyk')
plt.xticks(list(range(0,10)),frequent_items.itemsets[0:10],rotation='vertical')

rules=association_rules(frequent_items,metric='lift',min_threshold=0.90)
rules.sort_values('lift',ascending=False,inplace=True)
















