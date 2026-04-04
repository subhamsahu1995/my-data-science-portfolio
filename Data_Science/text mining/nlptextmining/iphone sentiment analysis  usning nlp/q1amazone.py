#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

Created on Wed Nov 24 15:19:10 2021

@author: subham

"""

'''

Extract reviews of any product from e-commerce website Amazon.
Perform sentiment analysis on this extracted data and build a unigram and bigram word cloud.

'''


    
import requests
from bs4 import BeautifulSoup as bs
i_phone =[]
for i in range (1,11):
    ip=[]
    url="https://www.amazon.in/Apple-iPhone-Pro-Max-1TB/product-reviews/B09G9FDDJN/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber="+str(i)
    pages=requests.get(url)
    soup=bs(pages.content,'html.parser')
    lis=soup.find_all("span",attrs={"class","a-size-base review-text review-text-content"})
    for i in range(len(lis)):
        ip.append(lis[i].text)
    i_phone =i_phone+ip
    
        
with open("i_phone13.text","w",encoding="utf8") as out:
        out.write(str(i_phone))

    
#till here i  have extracted the data and stored in i_phone13.text file


with open('/Users/subham/Desktop/data/360 assignment /text mining/i_phone13.text','r',encoding='utf-8') as sw:
    iphone=sw.read()
    

iphone

#now the next step is  data preprocessing 
#Joinining all the reviews into single paragraph 


import re
phone2=re.sub('([\W]|_)+'," ",iphone)
phone2
#removng all the special character


from nltk.stem.wordnet import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()


lem=lemmatizer.lemmatize(phone2)
lem


import nltk
nltk.download('punkt')
from nltk import word_tokenize


tk=word_tokenize(lem)
tk

#stopwords

nltk.download('stopwords')
from nltk.corpus import stopwords 
sw=stopwords.words('english')
clean_word=[]
for i in tk:
    if i not in sw:
        clean_word.append(i)
        
print(clean_word)        
        
#extra stop words 
  
with open("/Users/subham/Desktop/data/class_360/text mining /txtmining/Datasets NLP/stopwords_en.txt","r") as sw1:
    stowords = sw1.read()
    
stowords 
   
stowords = stowords.split("\n")

stowords.extend(["The","mobile","time","android","phone","device","screen","battery","product","apple","good","day","price","launched","I","easy","browser","...","Apple","Pro ","Max","iphone","pro","iPhone","prO","amazon"])


data3=[]
for i in clean_word:
    if i not in stowords:
        data3.append(i)
        
'''cleanded data  '''      
data3   



# WordCloud can be performed on the string inputs.
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt

cloud1=" ".join(data3)

wc=WordCloud(background_color='White',
                      width=1800,
                      height=1400
                     ).generate(cloud1)


plt.imshow(wc)
   
'''word cloud with positive words'''

with open("/Users/subham/Desktop/data/class_360/text mining /txtmining/Datasets NLP/positive-words.txt")as p:
    positive=p.read().split()
    
    
    
data4=[]
for i in data3:
    if i in positive:
        data4.append(i)

print(data4)

cloud=" ".join(data4)

wc=WordCloud(background_color='White',
                      width=1800,
                      height=1400
                     ).generate(cloud)
plt.imshow(wc)


'''word cloud with negative words'''


with open("/Users/subham/Desktop/data/class_360/text mining /txtmining/Datasets NLP/negative-words.txt") as n:
    neg=n.read().split("\n")
    
neg

data5=[]

for i in data3 :
    if i in neg:
        data5.append(i)
        
data5    


#negative word cloud
cloud=" ".join(data5)

wc=WordCloud(background_color='White',
                      width=1800,
                      height=1400
                     ).generate(cloud)
plt.imshow(wc)


#to know the frequency of the word we use bag of word

import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
bag_of_words_model = CountVectorizer()
print(bag_of_words_model.fit_transform(data3).todense()) # bag of words


bag_of_word_df = pd.DataFrame(bag_of_words_model.fit_transform(data3).todense())
bag_of_word_df.columns = sorted(bag_of_words_model.vocabulary_)
bag_of_word_df.head()
   
  
'''creating  bigram cloud'''

 

cloud1 #my clean data though it depends upon  us to 
# whether we need more things do cleare or update


from textblob import TextBlob
blob = TextBlob(cloud1)

cloud2=blob.ngrams(n=2)
cloud2

# We need to convert each WordList n-gram into a single string (e.g., "This is")
# before we can join them all together with " ".join()


cloud2_as_strings = [" ".join(ngram_wordlist) for ngram_wordlist in cloud2]
print("\ncloud2 converted to a list of strings:")
print(cloud2_as_strings)

# Now, you can join this list of strings into a single large string
cl2 = " ".join(cloud2_as_strings)

print(cl2)






wc=WordCloud(background_color='White',
                      width=1800,
                      height=1400
                     ).generate(cl2)
plt.imshow(wc)






nltk.download('punkt')

from wordcloud import WordCloud, STOPWORDS

WNL = nltk.WordNetLemmatizer()

# Lowercase and tokenize
text = cloud1.lower()

# Remove single quote early since it causes problems with the tokenizer.
text = text.replace("'", "")

tokens = nltk.word_tokenize(text)
text1 = nltk.Text(tokens)

# Remove extra chars and remove stop words.
text_content = [''.join(re.split("[ .,;:!?‘’``''@#$%^_&*()<>{}~\n\t\\\-]", word)) for word in text1]

# Create a set of stopwords
stopwords_wc = set(STOPWORDS)
customised_words = ['price','ppx','dt','asin','great','yo','ref','psc','notch'] # If you want to remove any particular word form text which does not contribute much in meaning

new_stopwords = stopwords_wc.union(customised_words)

# Remove stop words
text_content = [word for word in text_content if word not in new_stopwords]

# Take only non-empty entries
text_content = [s for s in text_content if len(s) != 0]

# Best to get the lemmas of each word to reduce the number of similar words
text_content = [WNL.lemmatize(t) for t in text_content]

nltk_tokens = nltk.word_tokenize(text)  
bigrams_list = list(nltk.bigrams(text_content))
print(bigrams_list)

dictionary2 = [' '.join(tup) for tup in bigrams_list]
print (dictionary2)

# Using count vectoriser to view the frequency of bigrams

from sklearn.feature_extraction.text import CountVectorizer
vectorizer = CountVectorizer(ngram_range=(2, 2))
bag_of_words = vectorizer.fit_transform(dictionary2)
vectorizer.vocabulary_



sum_words = bag_of_words.sum(axis=0)
words_freq = [(word, sum_words[0, idx]) for word, idx in vectorizer.vocabulary_.items()]
words_freq =sorted(words_freq, key = lambda x: x[1], reverse=True)
print(words_freq[:100])



# Generating wordcloud
words_dict = dict(words_freq)
WC_height = 1000
WC_width = 1500
WC_max_words = 200
wordCloud = WordCloud(max_words=WC_max_words, height=WC_height, width=WC_width, stopwords=new_stopwords)
wordCloud.generate_from_frequencies(words_dict)


plt.figure(4)
plt.title('Most frequently occurring bigrams connected by same colour and font size')
plt.imshow(wordCloud, interpolation='bilinear')
plt.axis("off")
plt.show()


