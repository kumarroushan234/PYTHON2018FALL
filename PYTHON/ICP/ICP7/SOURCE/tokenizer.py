import urllib

import requests
from bs4 import BeautifulSoup
import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('wordnet')
nltk.download('maxent_ne_chunker')
nltk.download('words')
from nltk.tokenize import word_tokenize
from nltk.util import ngrams
from nltk.stem import PorterStemmer, LancasterStemmer, SnowballStemmer, WordNetLemmatizer
from nltk import wordpunct_tokenize,ne_chunk,pos_tag


#opening text file naming input to save the text data
file = open("input.txt","w+", encoding="utf-8")

# Getting the link
getLink=urllib.request.urlopen("https://en.wikipedia.org/wiki/Python_(programming_language)")

# Converting to HTML
soup = BeautifulSoup(getLink,"html.parser")
file.write(soup.get_text())


#reading the file input
inputfile = open("input.txt","r", encoding="utf-8")
fileread = inputfile.read()

#Sentence tokenization and word tokenization
senttokens = nltk.sent_tokenize(fileread)
wordtokens = nltk.word_tokenize(fileread)

#printing each sentence
for s in senttokens:
    print("PRINTING SENTENCES: \n" )
    print(s)


#printing each word
for w in wordtokens:
    print("PRINTING WORDS : \n")
    print(w)


#Porter Stemmer
pStemmer=PorterStemmer()
print("PORTER STEMMING OUTPUT: \n")
for p in wordtokens:
    print(pStemmer.stem(str(p)))

#lancasters Stemmer
lStemmer=LancasterStemmer()
print(" LANCASTER STEMMING OUTPUT: \n")
for t in wordtokens:
    print(lStemmer.stem(str(t)))

#Snowball Stemmer
sStemmer = SnowballStemmer('english')
print("SNOWBALL STEMMING OUTPUT: \n")
for s in wordtokens:
    print(sStemmer.stem(str(s)))

#parts of speech
print("PARTS OF SPEECH: \n")
print(nltk.pos_tag(wordtokens))

#Lemmatizer
print("LEMMATIZER: \n")
lemmatizer = WordNetLemmatizer()
for l in wordtokens:
    print(lemmatizer.lemmatize(str(l)))

#Trigram
print("TRIGRAM: \n")
trigram = ngrams(wordtokens, 3)
for t in trigram:
    print(t)




#Named Entity Recognition
print("NAMED ENTITY RECOGNIZATION: \n")
for s in senttokens:
    ner = ne_chunk(pos_tag(wordpunct_tokenize(s)))
    print(str(ner))