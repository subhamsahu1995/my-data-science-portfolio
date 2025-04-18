#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug  7 19:30:26 2021

@author: subham

"""
#interview questions

#ascending and descending order of a list

l1=[2,3,53,11]
l1.sort()
ascending=l1 
print(ascending)
l1.sort(reverse=True)
descending=l1
print(descending)

#output
#[2, 3, 11, 53]
#[53, 11, 3, 2]
#reverse string in same position
name="Subham Sahu"
rev=name[-1::-1]
wrd=rev.split()
first_name=wrd[1]
last_name=wrd[0]

reversed_name_within_same_position=first_name+" "+last_name
print(reversed_name_within_same_position)

#output
# mahbuS uhaS


#Question A7: WAP to input 4 integers a, b, c, d and check that the equation a3 + b3 +c3 = d3 is satisfied or not.
a= int(input("enter a no"))
b= int(input("enter a no"))
c= int(input("enter a no"))
d=int(input("enter a no"))
a3=a**3
b3=b**3
c3=c**3
dc=d**3
d3=a3+b3+c3
if dc==d3:
    print("equation satisfied")
else:
    print("equation doesn't satisfy")
print(a,b,c,a3,b3,c3,dc,d3)    
    
#Question B8: WAP to input the salary of a person and calculate the hra and da according to the following conditions:
		#Salary 				HRA		DA
 		#5000-10000			10%		5%	
		#10001-15000			15%		8%
 


sal=int(input("enter a sal"))
if sal >=5000 and sal<=10000:
    hra= .1*sal
    da= .05*sal
elif sal>=10001 and sal <=15000:
    hra=(15/100)*sal
    da=.06*sal
print( sal,hra,da)    


z=[1,3,4,5,7]
print(z[-1])
print(z[1:4])

y=0
for x in z:
      if x==1:
         y=100
      if x==3:
         y=200
      if x==8:
          y=500
      print(x,y)    
#Question B10: An electricity board charges according to the following rates:
		#For the first 100 units -   40 paisa per unit.
		#For the next 200 units -   50 paisa per unit.
		#beyond 300 units -  60 paisa per unit.
      
unit=int(input("enter a unit"))
slab=" "
if unit>=100:
    rate=.4*unit
    salb="comes under first slab"
elif unit <=300:
    rate=40+(unit-100)*0.5
    slab="slab>100and slab <300"
else:
    slab="greater than 300 unit"
    rate=90+(unit-300)*0.6
print(slab,50+rate)
    

#Question B12: WAP to input the selling price and cost price from the user and determine whether the seller has made profit
#or incurred loss. Also display the value of profit or loss.

sp=int(input("enter a selling price"))
cp=int(input("enter a cost price"))
profit=0
loss=0
if sp>cp:
    profit=sp-cp
    print("there ia proit")
else:
    loss=cp-sp
    print("here it is loss")
print("profit value",profit,"loss value",loss)    


#Question B76: WAP to print the following series:
#(1)	2, 4, 8, 16, 32, 64, 128, 256
#(2)	1, 4, 7, 10, …………… 40
#(3)	1, -4, 7, -10……………-40

n= int(input("enter a no"))
z=0
for x in range (1,(n+1)):
    z=2**x
    print(z,x)
         
#Question B76: WAP to print the following series:
#(1)	2, 4, 8, 16, 32, 64, 128, 256
                                                                                                                                                              
x=0
y=0
while x<=10:
    x=x+1
    y=2**x
    print(x,y)

    
    
#(2)	1, 4, 7, 10, …………… 40

    
for x in range(-1,-40 ,-3):
    print(x)



#(4)	1, 5, 11, 19, 29 ……

j=0
for x in range(1,10):
    j=x**2+(x-1)
    print(x,j)

    
z=0
x=0

while x <=10:
    z=x**2+(x-1)
    print(x,z)
    x=x+1
    
#estion B40: WAP to input 2 numbers and find out the sum of all the even nu mbers which are not divisible by 5 but divisible by 3
#and lies between the given two numbers.
a= int(input("enter: a no"))
b=int(input("enter a no"))
x=0
ss=0
for x in range(a,b):
    if x%2==0 and x%3==0 and x%5!=0:
        ss=ss+x
        print(x,ss)

a= int(input("enter: a no"))
b=int(input("enter a no"))
ss=0
while a<=b:
    if a%2==0 and a%3==0 and a%5!=0:
        ss=ss+a
        print(a,ss)
    a=a+1


#Question B37: WAP to print the sum and average of first n odd numbers.
n=int(input("enter a no"))
so=0
while n <=10:
    if n%2!=0:
        so=so+n
        print(so,n)
        oa=so/n
    n=n+1
print(so,oa)    
#Question B38: WAP to print the sum and average of first n even numbers.
n=int(input("enter a no"))
x=0
se=0
avg=0
for x in range(1,n):
    if x%2==0:
        se=se+x
        print(se,x)
        avg=se/x
print(se,avg)
        
#Question B39: WAP to print the table of a given number.
x=0
n= int(input("enter a no "))
while x <=10:
    x=x+1
    s=n*x
    print(x,s)

  
#===================================================================================================================================================================         
#list
#declare empty list
x=[]
z=0
while z<=10:
    j=int(input("enter a no"))
    x.append(j)
    print(x,z)
    z=z+1
   
##Question D2: WAP to search how many times a number is present in an array.
y=[]
x=0

for x in range(1,10):
    d=int(input("enter a no"))
    y.append(d)
    print(y,x)

for ss in y:
    print("the values ofss",ss)
    c=0
    for w in y:
        if ss==w:
            c=c+1
    print("count of freq:",c)            

#Question D4: WAP to input the sales made by a salesman in every month of a given year and find out the total, average, maximum and minimum sales.

sales=[]
month= 1
while month <=12:
    amount=int(input("enter a amout"))
    sales.append(amount)
    month=month+1
    print(month,sales)
tot=sum(sales)
avg=(tot/month)
max=max(sales)
min=min(sales)
print("tot",tot,avg,max,min,end=(" "))

#Question D5: WAP to calculate the average of 10 values stored in an array and display all those values which are more than the calculated average.
values=[]
y=0
avg=0
for x in range(1,5):
    y=int(input("enter a no"))
    values.append(y)
    print(values,x)
    
    for y in values:
      if y>avg:

        sum=sum(values)
        avg=sum/x
        print("avg",avg)
       
#program based on string


############################################################==================================================================================================

x=input("enter a string")
a=x.replace("a","c")
print(a)

	
#Question C1:  WAP to count the number of spaces, tabs and new line characters in a given string
x=input("enter a string")
s=x.count(" ")
t=x.count("\t")
n=x.count("\n")
print(s,t,n)


#Question C2: WAP to input a character and a string. Each occurrence of a character in the string should be converted to opposite case i.e. upper to lower case or vice versa.
l=x.swapcase()
print(l)

#Question C3: WAP to count the number of words and number of characters in a given line of text except the spaces.

x= input("enter a statement")
y=x.replace(" ","")
z=x.count(" ")
w=len(x)
print(x,y,z,w)
dd=list(x)
print(dd)

#Question C4: WAP to input a multi word string and produce a string in which first letter of each word is capitalized.
x= input("enter a no")
y=x.split(" ")
for d in y:
    c=d.capitalize()
    print(c)
    print(d)
print(y)

#Question C8: WAP to search a given string into another string and displays the position if found otherwise displays 0.
x=input("enter a string")
y=input("enter a string")
m=x.split(y)
print(m)
print(len(m[0]))

#Question C9: WAP to find a substring of given string.
x=input("enter a string")
y=input("enter a string")
if(x.find(y)==-1):
    print("the string is not present")
else:
    print("the value is present")
    

#Question C11: WAP to count all the occurrences of a character in a given string.

s= input("enter a string")
l=list(s)
t=set(s)


for x in t:  
    alpha=0
    for m in l:
        if m==x:
            alpha=alpha+1
    print(x,alpha)


    
s= input("enter a string")
l=list(s)

for x in set(l):   
    alpha=0
    for m in(l):
        if m==x:
            alpha=alpha+1
            print(x,alpha)
           


x=int(input("enter a no"))
y=0
z=0
while y<=x:
    y=y+1
    z=2**y
    print(y,z)    




def isunique(d):
    l=list(d)
    k=set(d)
    if len(l)>len(k):
        return"duplicate"
    else:
        return "unique"


def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)

#a=[12,32,[333,45],434,34,(323,434)]
#print(type(a))

#for i in a:
   

##if type(i) in (list,tuple):      

 ##    flatter(i[0])
   

#else:
      

#      out.append(i) 
#print(    

#wap to search key by value
# wap to get count of int, string, list value in dict
data={1:233,3:"thrice",4:"four",6:[12,34,56,67,75,45],2:200}
n=input("enter a key")
#print(type(data))
data["sam"]="subhamsahu"
data[22]="for few people"
print(data[n])


#write digit to word
w1 ={0:'zero',1:'one',2:'two',3:'three',4:'four',
     5:'five',6:'six',7:'seven',8:'eight',
     9:'nine',10:'ten',11:'eleven',12:'twelve',
     13:'thirteen',14:'fourteen',15:'fifteen',
     16:'sixteen',17:'seventeen',18:'eighteen',
     19:'ninteen'}
w2 ={2:'twenty',3:'fourty',4:'fourty',5:'fifty',
     6:'sixty',7:'seventy',8:'eighty',9:'ninty'}
w3={1:"one hundred",2:"two hundred",3:"three hundred",4:"four hundred",5:"five hundred",6:"six hundred"}
       
n= int(input("enter a no"))
if n<20:
     print(w1[n])
elif n<100:
     n1=n//10
     n2=n%10
     print(w2[n1],w1[n2])
elif n<1000:
     n3=n//100
     n4=n%100
     n1=n//10
     n2=n%10
     print(w3[n3],w2[n4])
    
#========================== ===============FUNCTION===========================================                     
     
#NO ARGUMENT NO RETURN

def my_fun1():
    x= int(input("enter a no"))
    y= input("enter your name")
    z=input("enter yor class")
    print(x,y,z)


for x in range(1,10):
     my_fun1()
     print(x)
         
          

my_fun1()
my_fun1()
my_fun1()
#NO ARGUMENT WITH RETURN

def fun():
     x= int(input("enter a no"))
     y= int(input("enter a no"))
     return(x,y)
a,b=fun()
print(a+b)


def fun():
     x= int(input("enter a no"))
     y= int(input("enter a no"))
     c=x+y
     return(c)
o=fun()
print(o)




#ARGUMENT WITH NORETURN
def fun(x,y):
     c=x+y
     print(c)

     
fun(4,6)



#ARGUMENT WITH RETURN    
def fun(a,b):
     a=int(input("enter a no"))
     b=int(input("enter a no"))
     return(a,b)




d,r=fun(3,5)
print(d+r)
print(d*r)

s=fun()
print(2*s)

#wap the factorial of a gievn no from the user

def fact(n):
     f=1
     for x in range(1,n+1):
          f=f*x
     return(f)
t=int(input("enter a no"))
fa= fact(t)
print(fa)
    
          
def my_num(n):
     f=1
     for x in range(1,n+1):
          f=f*x
     return(f)







     
d=my_num(6)
print(d)




def my_fun(l):
     y=1
     for x in range(1,l+1):
          y=y*x
     return(y)
          
     

ee=my_fun(8)
print(ee)


for x in range (1,11):
     if x%3==0:
          break
     print("break",x)
for x in range(1,20):
     if x%3==0:
       continue
     print("continue",x)


n=int(input("enter a no of candies"))
y=10
z=0
for x in range (1,n+1):
     if x>y:
          print("out of stock")
          break
     print("candies")
     z=z+1
     print(z)
print("bye and have your food sahu lovely bhaskar")



for x in range(1,13):
     if x%2==0:
         #print(x)
        # print("the value was even")
         continue
     print(x)

#=============================================,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,=============================================

     #nested loop




for x in range(1,4):
	for c in range(1,x+1):
		print("*",end=" ")
	print()	          



#reverse the piramid of star
n=int(input("enter a no"))	
for x in range(1,n):
     for y in range(1,n-x):
          print("*",end=" ")
     print()     

#--------------------------------------------------------------------------------------------------------------------------------------
     #TWO DIMENSION LIST


x=[]
#n=int(input("enter a no"))
for y in range(3):
     z=[]
     name=input("enter your name")
     age=input("enter your age")
     z.append(name)
     z.append(age)
     x.append(z)
     print(x,end=" ")
     
for s in x:
     print(s)


#while true

#it will keep on iterating untill or unless the condition become true.
x=5
while True:
     y=int(input("entaer a no"))
     if x==y:
          print("you are fit for this job")
          break
    
     else:
          print("enter your experience")
           

y=10
while True:
    
    x=int(input("enter a no"))
    if x>y:
         print("your order can't be processed,please enter a no again")
        
    else:
         for i in range(1,x+1):
              print("take")
         break
     
     





         
y=10
while True:
          x=int(input("enter a no"))
          if x>y:
           print("not sufficient amout as per your requirement,enter less requirement")
         
          else:
           for i in range(1,x+1): 
               print("candyxyz")
           break
          #print("candyxyz")
           
     


y=10
n=int(input("enter a no"))     
for x in range(1,n+1):
          if x>y:
               print("not sufficient amout as per your requirement,add less requirement")
               break
          print("candies")

print("bye")


pt_data=[]
while True:
     #pt_data=[]
     pt=input("1:add,press2:desplay,press3:update,press4:delete,press5:exit")
     if pt=='1':
          ptid=input("patient id")
          ptname=input("enter pt_name")
          ptage=input("enter pt_age")
          pt_data.append([ptid,ptname,ptage])
          print("new record  is  added")
          
     elif pt=='2':
          for r in pt_data:
              print(r)
         # print(pt_data)     
               
     elif pt=='3':
          ptid2=input("enter pt_id which you want to update")#if can name the variable with different name
          for i in range(0,len(pt_data)):
               if pt_data[i][0]== ptid2:#as of the commented variable
                    new_ptname=input("enter new pt_name")
                    newpt_age=input("enter pt_age")
                    pt_data[i][1]= new_ptname
                    pt_data[i][2]= newpt_age
                    print("record changed")

     elif pt=='4':
          wrow=[]
          ptid=input("enter patient id which you want to delete ")
          for i in range(0,len(pt_data)):
               if pt_data[i][0]== ptid:
                    wrow.append(pt_data[i])
                    break
               
          if len(wrow)<1:#if ptid!=ptid
             print("given value is not found")
          else:
             pt_data.remove(wrow[0])
          
        
     elif pt == '5':
          break
     else :
          print("wrong choice")
'''              
 function
 factoriar
 fibnocii series
 dynamic argument
 optional argument
'''
def age(* ag):
     a=int(input("enter a no"))
     for i in ag:
          n=a*i
          print(n)


age(12,34,54,23,22,23,43)



#optional argument
def mu_fun(a,b,c=2,d=3):
     e=a+b*c
     return(e)



jj=mu_fun(33,43)
print(jj)



#factorial
def fact(n):
     y=1
     for i in range(1,n+1):
          y=i*y
          print(y)

        

#febo 1,1,2,3,5,8....
def fib(x):
    if x==1:
        return 1
    elif x==2:
        return 1
    elif x>2:
        return fib(x-1)+ fib(x-2)
    

n=int(input("enter a no"))

for n in range (1,n+1):
     print(n,fib(n))


        

#read this file

o=open(r'C:\Users\SONY\Desktop\samm.txt','r')
#print(o.read())
#print(z)
x=o.readlines()
print(x)
y=x[1]
print(y,"y")
for i in x:
     print(i)


w=open(r'C:\Users\SONY\Desktop\samm.txt','w')
w.write('hello world\n')
w.write('please maintain\n')
w.write('social distancing')

w.close()

append=open(r'C:\Users\SONY\Desktop\samm.txt','a')
append.write("so this is the append file\n")
append.close()
#read and append

rd=open(r'C:\Users\SONY\Desktop\datatt.txt','r')
f=rd.readlines()
print(f)

for c in f:
     print(c)
ap=open(r'C:\Users\SONY\Desktop\datatt.txt','a')
ap.write('subham s@007\n')
ap.write('saurabh sh344\n')
ap.close()





#find a perticular word  , word count ,row count,character count
#find=[is]
rd=open(r'C:\Users\SONY\Desktop\datatt.txt','r')
f=rd.readlines()
wc=0
for k in f:
     ss=k.split(" ")
     print(ss)
     wc=wc+len(ss)
     s=k.replace(" ","")
     
print(wc)
print("rc",len(f))





