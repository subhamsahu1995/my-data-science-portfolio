#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 18:29:23 2021

@author: subham
"""
'''The Shawshank Redemption'''
#Extract reviews for any movie from IMDB and perform sentiment analysis.
import requests 
from bs4 import BeautifulSoup as bs

m=[]
url="https://www.imdb.com/title/tt0111161/reviews?ref_=tt_urv"
rev=requests.get(url) 
soup=bs(rev.content,'html.parser')
reviews=soup.find_all('a',attrs={'class',"title"})
for i in range (len(reviews)):
     m.append(reviews[i].text)

m
mov=" ".join(m)
mov
import re
movie=re.sub('([\W]|_)+'," ",mov)
movie



import nltk
nltk.download('punkt')
from wordcloud import WordCloud, STOPWORDS
from nltk  import word_tokenize
tk=word_tokenize(mov)
tk
stopwords_wc = set(STOPWORDS)
customised_words = ["*","A",".","..."] # If you want to remove any particular word form text which does not contribute much in meaning
new_stopwords = stopwords_wc.union(customised_words)

clean =[]
for i in tk:
     
    if i not in new_stopwords:
     clean.append(i)
    
clean   

cl="".join(clean )

cl
cl = [s for s in cl if len(s) != 0]
cl

cl="".join(clean )
cl

from textblob import TextBlob
blob = TextBlob(cl)
blob.ngrams(n=2)

import matplotlib.pyplot as plt
#word cloud
text=str(blob)
text
wordcloud = WordCloud(width = 1800, height = 1800, 
                background_color ='white', 
                max_words=200,
                min_font_size = 10).generate(text)


plt.imshow(wordcloud)



