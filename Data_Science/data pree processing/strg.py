#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 21 22:34:37 2021

@author: subham
"""
'''
Create a string “Grow Gratitude”.
Code for the following tasks:
How do you access the letter “G” of “Growth”?
How do you find the length of the string?
Count how many times “G” is in the string.
'''
word1='Grow Gratitude'
print(word1)
#How do you access the letter “G” of “Growth”?
wrd2='Growth'
x=list(wrd2)
print(x[0]) 

#Count how many times “G” is in the string.
w='Grow Gratitude'
x=0
for i in w:
    
    if i=="G":
        x=x+1
        print(x)
        
        
'''
Create a string “Being aware of a single shortcoming within yourself is far more useful than being aware of a thousand in someone else.”
Code for the following:
Count the number of characters in the string.

'''    
x= "Being aware of a single shortcoming within yourself is far more useful than being aware of a thousand in someone else."

y=x.split(' ')
z=list(x)
z
len(x)
len(y)
len(z)

'''
Create a string "Idealistic as it may sound, altruism should be the driving force in business, not just competition and a desire for wealth"
Code for the following tasks:
get one char of the word
get the first three char
get the last three char

'''

strn="Idealistic as it may sound, altruism should be the driving force in business, not just competition and a desire for wealth"
xx=strn.split(" ")
xx
for y in xx:
        k=list(y)
        print(k[0])
 #here we get first letter of the word
 
'''get the first three char'''

thr=xx[:3]
thr

'''get the last three char'''

thr=xx[-3:]
thr

'''
create a string "stay positive and optimistic". Now write a code to split on whitespace.
Write a code to find if:
The string starts with “H”
The string ends with “d”
The string ends with “c”
'''

x= "stay positive and optimistic"
x.split(" ")

x.startswith("H")
x.endswith("d")
x.endswith("c")    
   
# Write a code to print " 🪐 " one hundred and eight times. (only in python)

n=int(input( "enter a no 108"))
x=0
for i in range( n+1):
    x=x+1
    print("jupiter  🪐 ",x)
       
      
#Create a string “Grow Gratitude” and write a code to replace “Grow” with “Growth of”
    

x="Grow Gratitude"
x.replace('Grow','Growth')


#A story was printed in a pdf, which isn’t making any sense. i.e.:
    
'''.elgnujehtotniffo deps mehtfohtoB .eerfnoilehttesotseporeht no 
dewangdnanar eh ,ylkciuQ .elbuortninoilehtdecitondnatsapdeklawesuomeht 
,nooS .repmihwotdetratsdnatuotegotgnilggurts saw noilehT .
eert a tsniagapumihdeityehT .mehthtiwnoilehtkootdnatserofehtotniemacsretnuhwef a ,
yad enO .ogmihteldnaecnedifnocs’esuomeht ta dehgualnoilehT ”.
emevasuoy fi yademosuoyotplehtaergfo eb lliw I ,uoyesimorp I“ .eerfmihtesotnoilehtdetseuqeryletarepsedesuomehtnehwesuomehttaeottuoba saw 
eH .yrgnaetiuqpuekow eh dna ,peels s’noilehtdebrutsidsihT .
nufroftsujydobsihnwoddnapugninnurdetratsesuom a nehwelgnujehtnignipeelsecno saw noil A”

'''

x="""elgnujehtotniffo deps mehtfohtoB .eerfnoilehttesotseporeht no 
dewangdnanar eh ,ylkciuQ .elbuortninoilehtdecitondnatsapdeklawesuomeht 
,nooS .repmihwotdetratsdnatuotegotgnilggurts saw noilehT .
eert a tsniagapumihdeityehT .mehthtiwnoilehtkootdnatserofehtotniemacsretnuhwef a ,
yad enO .ogmihteldnaecnedifnocs’esuomeht ta dehgualnoilehT ”.
emevasuoy fi yademosuoyotplehtaergfo eb lliw I ,uoyesimorp I“ .eerfmihtesotnoilehtdetseuqeryletarepsedesuomehtnehwesuomehttaeottuoba saw 
eH .yrgnaetiuqpuekow eh dna ,peels s’noilehtdebrutsidsihT .
nufroftsujydobsihnwoddnapugninnurdetratsesuom a nehwelgnujehtnignipeelsecno saw noil A"""

y=x[::-1]

print(y)
"""
A lion was once sleeping in the jungle when a mouse started running up and down his body just for fun
. Thisdisturbedthelion’s sleep, and he wokeupquiteangry. He
 was abouttoeatthemousewhenthemousedesperatelyrequestedtheliontosethimfree. “I promiseyou, I will be ofgreathelptoyousomeday if yousaveme
.” Thelionlaughed at themouse’sconfidenceandlethimgo. One day
, a fewhunterscameintotheforestandtookthelionwiththem. Theytiedhimupagainst a tree
. Thelion was strugglingtogetoutandstartedtowhimper. Soon,
 themousewalkedpastandnoticedthelionintrouble. Quickly, he ranandgnawed
 on theropestosetthelionfree. Bothofthem sped offintothejungle
"""


