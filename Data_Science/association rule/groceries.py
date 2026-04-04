#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 28 13:25:20 2021

@author: subham
"""
'''
The Departmental Store, has gathered 
the data of the products it sells on a Daily basis.
Using Association Rules concepts,
 provide the insights on the rules and the plots.
'''
groceries=[]
import pandas as pd
from mlxtend.frequent_patterns import apriori,association_rules
with open("/Users/subham/Desktop/data/360 assignment /association rule/Datasets_Association Rules/groceries.csv") as f:
    groceries=f.read()

groceries=groceries.split('\n')

groceries_list=[]
for i in groceries:
    s=i.split(',')
    groceries_list.append(s)
    
all_groceriesitem=[]
for i in  groceries_list:
    print(i)
    for k in i:
        all_groceriesitem.append(k)
        

#now i have to find the frequency
from collections import Counter
from collections import Counter # ,OrderedDict

freqency=Counter(all_groceriesitem)

#now sort it as per the frequencies
freqency=sorted(freqency.items(),key=lambda x:x[1])


#now separate two diff col , with value and frequency
#as we are looking for the higher frequency  that is why we need to sort



freq=list(reversed([i[1]for i in freqency]))                    


items=list(reversed([i[0]for i in freqency]))

#now lets see the bar plot of freq and items
import matplotlib.pyplot as plt
plt.Figure(figsize=(27,10));plt.title('frequency_barpplot')
plt.bar(height=freq[0:11],x=list(range(0,11)),color='rgbkym')
plt.xticks(list(range(0,11) ),items[0:11])
plt.show()



#now creating dataframe to access row and columns
import pandas as pd
groceries_data=pd.DataFrame(pd.Series(groceries_list))

groceries_data=groceries_data.iloc[:9835,:]


groceries_data.columns=['transactional']
groceries_data.shape
#creating dummy variable for evry idem
data=groceries_data['transactional'].str.join(sep='*').str.get_dummies(sep='*')

#now our data set is ready no to rum algorithm

from mlxtend.frequent_patterns import apriori,association_rules

fitems=apriori(data,min_support=0.007,max_len=(10),use_colnames=True)
fitems

#here i am taking min_support as 0.007 i.e in the data the frequency of that item
#
fitems.sort_values('support', ascending = False, inplace = True)
'''	support	itemsets
102	0.255490036600244	frozenset({'whole milk'})
64	0.19347295648637658	frozenset({'other vegetables'})
79	0.18391622610817404	frozenset({'rolls/buns'})
88	0.17435949572997153	frozenset({'soda'})
'''    
#so here we can say that the % of whole milk in the dataset is auround 25% with is maximun transaction


plt.bar(x = list(range(0, 11)), height = fitems.support[0:11], color ='rgmyk')
plt.xticks(list(range(0, 11)), fitems.itemsets[0:11], rotation = "vertical")
plt.xlabel('item-sets')
plt.ylabel('support')
plt.show()




rules=association_rules(fitems,metric='lift',min_threshold=0.9)

top10_rules=rules.sort_values('lift',ascending=False).head(10)

#here we see vice versa.....wchich is almost same rule so we need to remove these rules


'''
example
	antecedents	consequents
1381	frozenset({'whole milk', 'other vegetables'})	frozenset({'root vegetables', 'tropical fruit'})
1376	frozenset({'root vegetables', 'tropical fruit'})	frozenset({'whole milk', 'other vegetables'})
'''
def dup(i):
    return(sorted(list(i)))

xx=rules.antecedents.apply(dup)+rules.consequents.apply(dup)

xx=xx.apply(sorted)

rules_set=list(xx)


unique_rules_sets = [list(m) for m in set(tuple(i) for i in rules_set)]


index_rule=[]


for i in unique_rules_sets:
    index_rule.append(i)
    
sbm= rules.iloc[index_rule, :]



#aa=rules_no.sort_values('lift',ascending=False)   

sbm.sort_values('lift', ascending = True).head(10)

'''==============================================================='''
#support=.01% and confidence=0.8%
f2=apriori(data,min_support=0.01,max_len=(10),use_colnames=(True))




#vizualization

plt.bar(x=list(range(0,11)),height=f2.support[0:11],color='rgmyk')
plt.xticks(list(range(0, 11)), f2.itemsets[0:11], rotation = "vertical")
plt.xlabel('items')
plt.ylabel('support')




#as we see the no of rows reduce to 333 
rule2=association_rules(f2,metric='lift',min_threshold=0.8)

top10_rules2=rule2.sort_values('lift',ascending=False).head(10)

#now its on client to choose which one to go for.





