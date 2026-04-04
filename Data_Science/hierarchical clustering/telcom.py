#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 14 13:43:19 2021

@author: subham
"""
'''
Perform clustering analysis on the telecom data set. 
The data is a mixture of both categorical and numerical data.
 It consists of the number of customers who churn out.
 Derive insights and get possible information on factors that 
 may affect the churn decision. Refer to Telco_customer_churn.xlsx 
 dataset.
'''

import pandas as pd
import numpy as np

data=pd.read_excel('/Users/subham/Desktop/data/360 assignment /hierarchical clustering/Dataset_Assignment Clustering/Telco_customer_churn.xlsx')
data
j=data.describe()
j
data.isna().sum()

#no features are  missing
data.dtypes
data.duplicated().sum()
data.info()
#here i a selecting all those columns whose data type is object i.e string
object_columns = data.select_dtypes(include=['object']).columns

data1=data.drop(object_columns,axis=1)
data1
dd=data1.describe()
data1.drop(['Count'],axis=1,inplace=True)
data1

# now i have to standardize the data
def norm(i):
    x=(i-i.mean())/(i.max()-i.min())
    return(x)


normalize_data=norm(data1.iloc[:,0:])
normalize_data

#now aur data is normalized




from scipy.cluster.hierarchy import linkage
import scipy.cluster.hierarchy as sch
z=linkage(normalize_data,method='complete',metric='euclidean')
z
import matplotlib.pyplot as plt
plt.Figure(figsize=(17,12));plt.title('dendogram');plt.xlabel('index');plt.ylabel('distance')

sch.dendrogram(z,leaf_rotation=(0),leaf_font_size=(9))
plt.show()


# lets create a model
from sklearn.cluster import AgglomerativeClustering
model=AgglomerativeClustering(n_clusters=(5),linkage='complete',affinity='euclidean').fit(normalize_data)
ml=model.labels_

data['grouped']=ml=model.labels_
data.columns
#now arranging the columns
data.shape
data=data.iloc[:,[30,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29]]

data.columns


new=data.groupby('grouped').mean()
new.drop('Count',axis=1)
new

yy=np.where(data.grouped==1)
yy

'''
so the customer who are in group 1 seems to be the profitabele customer so we need to focus on them 
as there service intake bring good profit to the organization

'''
left=data.loc[[  50,   57,  142,  162,  191,  246,  278,  305,  317,  345,  378,
         404,  406,  426,  457,  476,  481,  524,  530,  534,  536,  542,
         545,  548,  556,  584,  595,  614,  637,  648,  656,  682,  686,
         719,  732,  746,  747,  748,  750,  779,  786,  789,  791,  793,
         815,  833,  840,  849,  862,  869,  871,  876,  881,  899,  905,
         911,  912,  922,  929,  932,  945,  960,  971,  972,  981,  983,
         985,  995, 1002, 1004, 1018, 1028, 1035, 1044, 1060, 1084, 1092,
        1106, 1120, 1121, 1162, 1175, 1205, 1217, 1223, 1251, 1295, 1296,
        1300, 1310, 1329, 1369, 1399, 1409, 1450, 1464, 1480, 1506, 1519,
        1522, 1528, 1535, 1558, 1578, 1600, 1603, 1608, 1660, 1698, 1795,
        1832, 1836, 1870, 1894, 1910, 1959, 1968, 1982, 2003, 2048, 2062,
        2136, 2169, 2194, 2205, 2231, 2232, 2271, 2323, 2324, 2327, 2343,
        2378, 2391, 2392, 2402, 2410, 2495, 2534, 2550, 2559, 2566, 2569,
        2571, 2587, 2596, 2604, 2615, 2635, 2662, 2668, 2669, 2673, 2678,
        2685, 2702, 2706, 2749, 2756, 2763, 2793, 2801, 2810, 2843, 2844,
        2846, 2848, 2856, 2859, 2864, 2865, 2867, 2875, 2877, 2881, 2883,
        2884, 2903, 2912, 2913, 2915, 2930, 2935, 2937, 2981, 2988, 3010,
        3018, 3034, 3036, 3056, 3058, 3062, 3083, 3089, 3090, 3098, 3105,
        3112, 3114, 3121, 3122, 3140, 3146, 3161, 3164, 3221, 3232, 3243,
        3277, 3285, 3291, 3315, 3322, 3332, 3343, 3354, 3359, 3362, 3366,
        3392, 3405, 3414, 3445, 3495, 3499, 3505, 3519, 3520, 3531, 3538,
        3543, 3549, 3558, 3560, 3563, 3565, 3603, 3615, 3621, 3625, 3652,
        3658, 3663, 3666, 3670, 3691, 3699, 3704, 3721, 3730, 3734, 3760,
        3765, 3768, 3771, 3785, 3799, 3803, 3805, 3819, 3829, 3839, 3846,
        3862, 3869, 3877, 3884, 3900, 3909, 3918, 3921, 3922, 3923, 3934,
        3950, 3957, 3989, 3997, 4002, 4003, 4004, 4007, 4008, 4016, 4018,
        4021, 4034, 4053, 4056, 4069, 4083, 4101, 4105, 4117, 4121, 4144,
        4148, 4152, 4155, 4163, 4167, 4179, 4201, 4204, 4206, 4209, 4210,
        4215, 4238, 4249, 4250, 4255, 4257, 4258, 4276, 4287, 4293, 4296,
        4305, 4310, 4313, 4317, 4323, 4329, 4339, 4345, 4373, 4381, 4394,
        4414, 4416, 4417, 4426, 4428, 4433, 4448, 4449, 4463, 4479, 4484,
        4489, 4493, 4496, 4498, 4499, 4523, 4536, 4539, 4559, 4573, 4599,
        4601, 4642, 4656, 4667, 4671, 4682, 4694, 4697, 4713, 4717, 4727,
        4729, 4742, 4743, 4745, 4750, 4752, 4757, 4761, 4766, 4767, 4794,
        4797, 4802, 4807, 4820, 4821, 4825, 4828, 4829, 4836, 4848, 4870,
        4896, 4904, 4908, 4912, 4918, 4926, 4934, 4960, 4972, 4978, 4980,
        4989, 4994, 5003, 5027, 5033, 5035, 5046, 5081, 5088, 5089, 5093,
        5107, 5118, 5133, 5144, 5151, 5154, 5155, 5157, 5160, 5164, 5178,
        5180, 5183, 5194, 5202, 5205, 5216, 5217, 5221, 5246, 5251, 5260,
        5271, 5272, 5275, 5280, 5283, 5286, 5291, 5295, 5315, 5318, 5335,
        5346, 5354, 5358, 5360, 5369, 5370, 5373, 5377, 5382, 5400, 5407,
        5408, 5419, 5428, 5448, 5462, 5467, 5476, 5490, 5491, 5502, 5506,
        5520, 5534, 5543, 5564, 5565, 5576, 5577, 5581, 5590, 5591, 5595,
        5604, 5608, 5613, 5634, 5641, 5643, 5645, 5654, 5674, 5677, 5701,
        5711, 5718, 5737, 5742, 5757, 5765, 5769, 5801, 5815, 5817, 5823,
        5825, 5826, 5845, 5860, 5880, 5881, 5884, 5889, 5897, 5916, 5922,
        5930, 5932, 5936, 5956, 5970, 5975, 5988, 5991, 5995, 6003, 6013,
        6029, 6037, 6059, 6060, 6085, 6097, 6107, 6116, 6119, 6140, 6144,
        6152, 6157, 6165, 6188, 6204, 6228, 6231, 6235, 6257, 6262, 6266,
        6271, 6281, 6314, 6323, 6328, 6387, 6421, 6422, 6427, 6428, 6435,
        6455, 6462, 6468, 6478, 6486, 6487, 6491, 6494, 6497, 6500, 6502,
        6514, 6519, 6523, 6531, 6537, 6569, 6583, 6584, 6588, 6590, 6602,
        6603, 6611, 6622, 6638, 6656, 6682, 6700, 6701, 6704, 6710, 6721,
        6734, 6744, 6758, 6786, 6802, 6804, 6818, 6824, 6846, 6852, 6873,
        6908, 6929, 6935, 6936, 6939, 6943, 6961, 6964, 6976, 6977, 6985,
        6998, 7012, 7018, 7029, 7040, 7042],:]

