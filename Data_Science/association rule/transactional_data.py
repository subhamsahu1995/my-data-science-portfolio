#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct  2 20:24:25 2021

@author: subham
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

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
data.replace(to_replace='NA',value=0)
col=data.columns
data.shape
y=data.isna().sum()
y
new_data=data.drop(y)

new_data.shape

new_data.columns
new_data.drop('NA',axis=1,inplace=(True))
new_data.columns
new_data=new_data.iloc[:,2:]

new_data.columns



#with 1% support and 90% lift ratio or we can confidence
frequent_items=apriori(new_data,min_support=0.01,use_colnames=(True),max_len=(10))

frequent_items.sort_values('support',ascending=False,inplace=True)

frequent_items.shape

import matplotlib.pyplot as plt
plt.bar(x=list(range(0,9)), height=frequent_items.support[0:9],color ='rgmyk')
plt.xticks(list(range(0,9)),frequent_items.itemsets[0:9],rotation='vertical')


rules=association_rules(frequent_items,metric='lift',min_threshold=0.90)
rules.sort_values('lift',ascending=False,inplace=True)

# as we see here many rules are repitative  so we need to 

def fin(i):
    return(sorted(list(i)))
           
ma_x=rules.antecedents.apply(fin) + rules.consequents.apply(fin)
ma_x=ma_x.apply(sorted)
uniq_rule=list(ma_x)    
      
uniq_rule_set=[list(m) for m in set(tuple(i)for i in uniq_rule)]

index_rule=[]

for i in uniq_rule_set:
    index_rule.append(uniq_rule.index(i))
    
rules_new=rules.iloc[index_rule,:]
rules_new.sort_values('lift',ascending=False)








