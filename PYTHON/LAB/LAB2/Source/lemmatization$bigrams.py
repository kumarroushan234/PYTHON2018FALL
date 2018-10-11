from nltk.corpus import wordnet as wn
from nltk import pos_tag,ne_chunk
from nltk.tokenize import word_tokenize,wordpunct_tokenize,sent_tokenize
import re, collections
from nltk.stem import WordNetLemmatizer
from nltk.tag import pos_tag
from collections import Counter
from nltk import FreqDist
import nltk
from nltk import ngrams
from operator import itemgetter


#-	Take an Inputfile. Use the simple approach below to summarize a text file
with open('input1.txt' , 'r') as f:
    lines = f.readlines()
print("lines",lines)
fr=''
#Multi- line file into single string
for m in lines:
    fr=fr+m
print(fr)
#tokenize word
word = word_tokenize(fr)
sent = sent_tokenize(fr)

#-	Using Lemmatization, apply lemmatization on the remaining words
lemmatizer = WordNetLemmatizer()
lemma2 = []
for word1 in word:
    lemma1 = lemmatizer.lemmatize(word1.lower())
    lemma2.append(lemma1)

print("\n ***********************LEMMATIZATION********************** \n")
print(lemma2)
fr_pos = pos_tag(lemma2)

print("\n ************************BIGRAM************************** \n")

n = 2
gram=[]
bigrams = ngrams(lemma2, n)
for grams in bigrams:
    gram.append(grams)
print(gram)
str1 = " ".join(str(x) for x,y in fr_pos)
str1_word = word_tokenize(str1)
print("\n ***********************BI-GRAMS WITH HIGHEST WORD FREQUENCY*************************** \n")
fdist1 = nltk.FreqDist(gram)
top_fiv = fdist1.most_common()
top_five = fdist1.most_common(5)

top=sorted(top_fiv,key=itemgetter(0))
print(top)
print('\n *******************************TOP 5 BIGRAMS WITH WORD FREQUENCY****************************** \n')
print(top_five)
sent1 = sent_tokenize(fr)
rep_sent1 = []


for sent in sent1:
    for word,words in gram:
        for ((c,m), l) in top_five:
            if (word,words == c,m):
                rep_sent1.append(sent)  # Creating sentences containing the most common words
print ("\n **************************************SENTENCES WITH TOP FIVE BIGRAMS:*************************** \n")
print(max(rep_sent1,key=len))