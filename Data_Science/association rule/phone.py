# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

'''
A Mobile Phone manufacturing company wants to launch its three 
brand new phone into the market, but before going with its 
traditional marketing approach this time it want to analyze the
 data of its previous model sales in different regions and you
 have been hired as an Data Scientist to help them out, use the 
 Association rules concept and provide your insights to the
 company’s marketing team to improve its sales.

'''
import pandas as pd
from mlxtend.frequent_patterns import apriori,association_rules
data=pd.read_csv("/Users/subham/Desktop/data/360 assignment /association rule/Datasets_Association Rules/myphonedata.csv")
data.shape
phonedata=data.iloc[:,4:]

# rules with 1%support  and confidence 95%


frequency=apriori(phonedata,min_support=0.01,use_colnames=(True))

frequency.sort_values('support',ascending=False,inplace=True)
import matplotlib.pyplot as plt
plt.figure(figsize=(15,8));plt.title('bar-plot')
plt.bar(x = list(range(0,8)), height = frequency.support[0:8], color ='rgmyk')
plt.xticks(list(range(0,8)),frequency.itemsets[0:8],rotation='vertical')


#as we see  white phones are having higher frequency 
#in the data set  which is almost 64%
rule=association_rules(frequency,metric='lift',min_threshold=0.95)
rule.sort_values('lift',ascending=False,inplace=True)

 #as we there are some rules which is common  or we can say vice versa
 #so we need to remove those rules
def fun(i):
     return(sorted(list(i)))
'''
	antecedents	consequents
3	frozenset({'white'})	frozenset({'orange'})
'''

ma_x=rule.antecedents.apply(fun)+rule.consequents.apply(fun)
ma_x=ma_x.apply(sorted) 
rul=list(ma_x)


uniq= [list(m)for m in set (tuple(i) for i in rul)]
 
ind=[]
for i in uniq:
    ind.append(rul.index(i))

    
new_rule=rule.iloc[ind,:]
 
new_rule.sort_values('lift',ascending=False,inplace=True)


#now creating rule2 with support 1% and confidence 80%

f2=apriori(phonedata,min_support=0.1,max_len=(10),use_colnames=True)
f2.sort_values('support',ascending=False,inplace=True)

#as we see rows reduce to 6 from 8

rule2=association_rules(f2,metric='lift',min_threshold=0.8)
rule2.sort_values('lift',ascending=(False),inplace=True)










