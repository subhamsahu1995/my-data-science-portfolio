#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Aug 15 21:47:33 2021

@author: subham
"""
#ALL QUESTIONS ARE DONE HERE FROM EVERY MODULE
'''
ASSIGNMENT-1 Data Types

Please implement by using Python.

Construct 2 lists containing all the available data types  (integer, float, string, complex and Boolean) and do the following..


Create another list by concatenating above 2 lists

Find the frequency of each element in the concatenated list.


Print the list in reverse order.

Create 2 Sets containing integers (numbers from 1 to 10 in one set and 5 to 15 in other set)

Find the common elements in above 2 Sets.
Find the elements that are not common.
Remove element 7 from both the Sets.

Create a data dictionary of 5 states having state name as key and number of covid-19 cases as values.
Print only state names from the dictionary.
Update another country and it’s covid-19 cases in the dictionary.
'''

#Construct 2 lists containing all the available data types  (integer, float, string, complex and Boolean) and do the following..

a=[1,1.3,'aa',{'a':"alpha"},(1+9j),True]
b=[2,3.5,'bb',{1:100,2:200},(2+5j),False]

#Create another list by concatenating above 2 lists


print(a)
z=a+b
print(z,end=',')

#Find the frequency of each element in the concatenated list.


for y in z:
    #print(y, end=', ')
    c=0
for j in z:
   # print(j,'j')
    if y==j:
        c=c+1
        print(j,c)
        
 
#Print the list in reverse order.

z.reverse()
print(z)


#Create 2 Sets containing integers (numbers from 1 to 10 in one set and 5 to 15 in other set)
set1=[]
for i in range(1,11):
    set1.append(i)
    print(i+1)
    print(set1)

set2=[]
    
for i in range(5,16):
    set2.append(i)
    print(i+1)
    print(set2)

sets=set1+set2
print(sets)


#Find the common elements in above 2 Sets.

def common_member(set1,set2):
    a_set = set(set1)
    b_set = set(set2)
 
    if (a_set & b_set):
        print(a_set & b_set)
    else:
        print("No common elements")
          
    
    

common_member(set1,set2)



#Find the elements that are not common in 2 list.

fx=set(set1).difference(set2)
print(fx)
fy=set(set2).difference(set1)
print(fy)

gg=set2-set1
print(gg)                      
ff=set1-set2
print(ff)  
      
not_common=gg.union(ff)
print(not_common)
        
not_comnon=list(not_common)
print(not_common)        

#Remove element 7 from both the Sets.




'''
Create a data dictionary of 5 states having state
 name as key and number of covid-19 cases as values.
Print only state names from the dictionary.
Update another country and it’s covid-19 cases in the dictionary.
'''

data={'delhi':646654,'up':465753,'Bihar':9767645,'jharkhand':234322,'kolkata':8688768}



for k,v in data.items():
    print(k)
    

m=input("enter the key")
for k,v in data.items():
    if k==m:
        print(v)
        break
    else:
        print('no record found')
        break
        
  
#Update another country and it’s covid-19 cases in the dictionary.
data['mumbai']=24876816
print(data.keys())



#===================================MODULE 2 =====================================    



'''
MODULE-2 OPERATORES
Please implement by using Python
A. Write an equation which relates   399, 543 and 12345 
B.  “When I divide 5 with 3, I got 1. But when I divide -5 with 3, I got -2”—How would you justify it.
       2.  a=5,b=3,c=10.. What will be the output of the following:
              A. a/=b
              B. c*=5  
       3. A. How to check the presence of an alphabet ‘s’ in word “Data Science” .
            B. How can you obtain 64 by using numbers 4 and 3 .



'''
#A. Write an equation which relates   399, 543 and 12345 

x=399
y=543
z=12345

12345/543
z=22*y+x
z

#B.  “When I divide 5 with 3, I got 1. But when I divide -5 with 3, I got -2”—How would you justify it.


5//3
-5//3    


#2.  a=5,b=3,c=10.. What will be the output of the following:
#A. a/=b
#B. c*=5 
a=a/b
print(f'the value of a/b={a}')
c=c*5
print(f'the value of c*5={c}')


#3. A. How to check the presence of an alphabet ‘s’ in word “Data Science” .
#B. How can you obtain 64 by using numbers 4 and 3 .

data='Data Science '
xx=list(data)
#print(xx)
con=0
m='S'
for x in xx:
    z=x.split(',')
    #print(z)
    for ll in z:
        print(ll)
        if ll in m:
         con=con+1
print('value is present & the total count is ',con)
       
        
        
data='Data Science '
xx=list(data)
#print(xx)
con=0
m='S','D'
for x in xx:
    z=x.split(',')
    #print(z)
    for ll in z:
        #print(ll)
        if ll in m:
         print(ll)   
         con=con+1
         print('value is present & the total count is ',con)
        
    
#B. How can you obtain 64 by using numbers 4 and 3 .  
 
x=64
y=4
z=3
x1=y**z
x1
if x1==x:
    print('matched')
else:
    print('notmatched')
    

#===================================MODULE 3 =====================================    

'''
MODULE 3 Variables
What will be the output of the following (can/cannot):
Age1=5
5age=55

What will be the output of following (can/cannot):
Age_1=100
age@1=100

How can you delete variables in Python ?


'''

#What will be the output of the following (can/cannot):
Age1=5
print(Age1)

5age=55
it cannot


What will be the output of following (can/cannot):
Age_1=100
print(Age_1)

age@123=100
#it cannot
 

#How can you delete variables in Python ?
a=12
b=34
c=34
a={1:100,2:200,3:300}
for k, v in data.items():
    if k==int(input("enter the k")):
        a.remove(k)
        
        
#create read update and delete
       
data=[]
while True:
    x=input("please press 1:crete,2:read,3:update,4:delete,5 to end")
    if x=="1":
        v_code=int(input("enter the verification_code"))
        name=input("enter your name")
        age=int(input("please input your age"))
        location=input("enter your location")
        data.append([v_code,name,age,location])
    elif x=="2":
        print(data)
    elif x=="3":
        v_code=int(input("enter the v_vode you want to update"))
        for i in range (0,len(data)):#loop
            if data[i][0]==v_code:
                new_name=input("enter  new name of the candidate")
                age_n=int(input("enter the age"))
                new_location=input("enter the location")
                data[i][1]=new_name
                data[i][2]=age_n
                data[i][3]=location
    elif x== "4":
        delo=[]
        v_code=int(input("enter the v_code you want to delete"))
        for i in range(0,len(data)):
             if data[i][0]==v_code:
                 delo.append(data[i])
                 print(delo)
                 break
        if len(delo)<1:
            print("given value is not found")
        else:
            data.remove(delo[0])
            
    elif x=="5":
        print("thanks ")
        break
              
#===================================MODULE 4 =====================================    
        
'''
MODULE-4 Conditional Statements
Please write Python Programs for all the problems .
 Take a variable ‘age’ which is of positive value and check the following:
If age is less than 10, print “Children”.
If age is more than 60 , print ‘senior citizens’
 If it is in between 10 and 60, print ‘normal citizen’

Find  the final train ticket price with the following conditions. 
If male and sr.citizen, 70% of fare is applicable
If female and sr.citizen, 50% of fare is applicable.
If female and normal citizen, 70% of fare is applicable
If male and normal citizen, 100% of fare is applicable
[Hint: First check for the gender, then calculate the fare based on age factor.. For both Male and Female ,consider them as sr.citizens if their age >=60]
Check whether the given number is positive and divisible by 5 or not.  
  
'''  
#1st question of module 4      
'''        
Take a variable ‘age’ which is of positive value and check the following:
If age is less than 10, print “Children”.
If age is more than 60 , print ‘senior citizens’
If it is in between 10 and 60, print ‘normal citizen’
'''     
age=int(input("please enter your current age"))

if age<10:
    print('you come under children categories')
elif age>60:
    print('you come under SENIOR CITIZEN')
elif age >10 and age<60:
    print('you come under normal categories')
else:
    print('reject')
    
'''Find  the final train ticket price with the following conditions. 
If male and sr.citizen, 70% of fare is applicable
If female and sr.citizen, 50% of fare is applicable.
If female and normal citizen, 70% of fare is applicable
If male and normal citizen, 100% of fare is applicable
[Hint: First check for the gender, then calculate the fare based on age factor.. For both Male and Female ,consider them as sr.citizens if their age >=60]
Check whether the given number is positive and divisible by 5 or not.  
'''
gender=input("enter your sex")
age=int(input("please enter your current age"))
fare=int(input("set the fare"))
cgfare=0
if gender=='male'and age>=60:
    cgfare=.7*fare
    print(f'you come under senior citizen and have to pay only {cgfare}')
elif gender=='female'and age>=60:
    cgfare=.5*fare
    print(f'you come under senior citizen and have to pay only {cgfare}')
elif (age >10 and age<60) and gender=='female':
    cgfare=.7*fare
    print(f'you come under normal citizen and have to pay only {cgfare}')
elif (age >10 and age<60) and gender=='male':
    cgfare=fare
    print(f'you come under normal citizen and have to pay only {cgfare}')
else:
    print("you are free to travel")    
    
    
#===================================MODULE 5 =====================================    
'''
MODULE 5 LOOPS and Functions
Please implement Python coding for all the problems.

A) list1=[1,5.5,(10+20j),’data science’].. Print default functions and parameters exists in list1.
B) How do we create a sequence of numbers in Python.
C)  Read the input from keyboard and print a sequence of numbers up to that number

Create 2 lists.. one list contains 10 numbers (list1=[0,1,2,3....9]) and other 
list contains words of those 10 numbers (list2=['zero','one','two',.... ,'nine']).
 Create a dictionary such that list2 are keys and list 1 are values..

 Consider a list1 [3,4,5,6,7,8]. Create a new list2 such that Add 10 to the even number and multiply with 5 if it is odd number in the list1..

       4.     Write a simple user defined function that greets a person in such a way that :
             i) It should accept both name of person and message you want to deliver.
              ii) If no message is provided, it should greet a default message ‘How are you’
           Ex: Hello ---xxxx---, How are you  - default message.
            Ex: Hello ---xxxx---, --xx your message xx---
'''


def my_fun(*n):
    list1=[n]
    print(list1)
    
    
    
my_fun({1:100,2:200,3:300,4:400},(1,2,3,4,5),"datascience")


#How do we create a sequence of numbers in Python

for x in range(1,10+1):
    print(x)

# Read the input from keyboard and print a sequence of numbers up to that number
    
n=int((input('enter a no till you want the sequence')))
for i in range(0,n+1):
    print(i)
    
    
    
'''
Create 2 lists.. one list contains 10 numbers (list1=[0,1,2,3....9]) and other 
list contains words of those 10 numbers (list2=['zero','one','two',.... ,'nine']).
 Create a dictionary such that list2 are keys and list 1 are values..

'''   
list1=[1,2,3,4,5,6,7,8,9,10] 
list2=['one','two','three','four','five','six','seven','eight','nine','ten']

dic=dict(zip(list1,list2))   
print(dic)
    
#Consider a list1 [3,4,5,6,7,8]. Create a new list2 such that Add 10 to the even number and multiply with 5 if it is odd number in the list1..

list1=[3,4,5,6,7,8]    

       
for x in list1 :
    if x%2==0:
        print("even no",(x+10))
        
    elif x %2!=0:
        print(x*5)
        
               
        
'''
4.     Write a simple user defined function that greets a person in such a way that :
             i) It should accept both name of person and message you want to deliver.
              ii) If no message is provided, it should greet a default message ‘How are you’
           Ex: Hello ---xxxx---, How are you  - default message.
            Ex: Hello ---xxxx---, --xx your message xx---    
'''        
def name() :
    first=input("enter your first name")
    second=input('enter your second name')
    message=input('enter your message')
    print(f'hi i am {first} {second} my message is {message}')
    
#calling function
name()    
'''    
 ii) If no message is provided, it should greet a default message ‘How are you’
           Ex: Hello ---xxxx---, How are you  - default message.
            Ex: Hello ---xxxx---, --xx your message xx---      
'''
def message() :
    first=input("enter your first name")
    second=input('enter your second name')
    message=input('enter your message')
    default="how are you??"
    if message=="  ":
        
        print(f'hi i am {first} {second} my message is {message}')
    elif message=='':
        print(f'hi i am {first} {second} your message is {default}')


#calling function
message()
      
    
    
#===================================MODULE  =====================================    
    
 '''   
    
MODULE 6 PACKAGES
Implement in Python

For the dataset “Indian_cities”, 
Find out top 10 states in female-male sex ratio
Find out top 10 cities in total number of graduates
Find out top 10 cities and their locations in respect of  total effective_literacy_rate.

For the data set “Indian_cities”
Construct histogram on literates_total and comment about the inferences
Construct scatter  plot between  male graduates and female graduates

For the data set “Indian_cities”
Construct Boxplot on total effective literacy rate and draw inferences
Find out the number of null values in each column of the dataset and delete them.

'''   

#Find out top 10 states in female-male sex ratio

import pandas as pd
import numpy as np

data=pd.read_csv('/Users/subham/Desktop/data/360 assignment /Python Problem Statements/Indian_cities.csv')
data
data.dtypes
grp=data.groupby('state_name').sex_ratio.sum()
srt=grp.sort_values(ascending=False)
srt
dp=srt.head(10)
dp

#Find out top 10 cities in total number of graduates
data=pd.read_csv('/Users/subham/Desktop/data/360 assignment /Python Problem Statements/Indian_cities.csv')
data

data.columns
data.duplicated()

al=data[['name_of_city','total_graduates']].sort_values('total_graduates',ascending=False)
pp=al.head(10)
pp
#Find out top 10 cities and their locations in respect of  total effective_literacy_rate.


data.columns
cl=data[['name_of_city','location','effective_literacy_rate_total']].sort_values('effective_literacy_rate_total',ascending=False)
cl
top=cl.head(10)
top


#Construct histogram on literates_total and comment about the inferences


data=pd.read_csv('/Users/subham/Desktop/data/360 assignment /Python Problem Statements/Indian_cities.csv')
data
data=pd.read_csv('/Users/subham/Desktop/data/360 assignment /Python Problem Statements/Indian_cities.csv')
data

import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
#import scipy.stats as stats
from scipy import stats
data.columns
plt.hist(data.literates_total)

data.literates_total.skew()

'''
In positive skew mean>median>mode
so we can say that it is positively skewed

346152.72819472617 > 141329.0 > 0    111514

right tailed skew
highly skewed

'''
x=data.literates_total.describe()
print(x)

aa=data.literates_total.mean()
aa
bb=data.literates_total.median()
bb
cc=data.literates_total.mode()
cc

stats.mode(data.literates_total)
print(x)

#Construct scatter  plot between  male graduates and female graduates

import matplotlib.pyplot as plot

import numpy as np
import seaborn as sns
 
data.columns
sns.lmplot(x='male_graduates', y='female_graduates', data=data) 
plt.title("Scatter Plot with Linear fit")


#Construct Boxplot on total effective literacy rate and draw inferences

import matplotlib.pyplot as plt
plt.boxplot(data[['effective_literacy_rate_total']])
plt.boxplot(data.effective_literacy_rate_total)
sns.boxplot(data.effective_literacy_rate_total)
# as we see there an outliers
 #now we detect the outliers through IQR
IQR=data.effective_literacy_rate_total.quantile(0.75)-data.effective_literacy_rate_total.quantile(0.25)
IQR


#Find out the number of null values in each column of the dataset and delete them.
data.isnull().sum()

'''
here is no null value
''' 






