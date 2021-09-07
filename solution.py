# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#Code is meant for the ACM research coding challenge for 2021. It analyzes two paragraphs:
#One from farenheit 451 and another from the biography of benjamin franklin and draws
#sentiment scores from texblob

import matplotlib.pyplot as plt
import numpy as np
import math
import nltk
from nltk import word_tokenize, pos_tag
from nltk.corpus import stopwords, wordnet
from nltk.stem import WordNetLemmatizer
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import pandas as pd
import re
from textblob import TextBlob

pd.set_option('max_colwidth', 10)


#The function below splits the texts from either paragraph into sections that 
#can be used to attach sentiments to individually

def split_text(text, n=10):
    
    length = len(text)
    size = math.floor(length / n)
    start = np.arange(0, length, size)
    
    split_list = []
    for piece in range(n):
        split_list.append(text[start[piece]:start[piece]+size])
    return split_list

#Cleans the text of all special characters (and, for my sanity, the mix-matched way the)
# text uses quotations marks)

def clean_text(dirty_text):
    cleaned_text = re.sub('[`]', "'", dirty_text)
    cleaned_text = re.sub('[^A-Za-z]+', ' ', cleaned_text)
    return cleaned_text

#tokenizes the text, removes stopwords, and tags the words to their POS
    
pos_dict = {'J':wordnet.ADJ, 'V':wordnet.VERB, 'N':wordnet.NOUN, 'R':wordnet.ADV}
def token_stop_pos(fixed_text):
    tags = pos_tag(word_tokenize(fixed_text))
    newlist = []
    for word, tag in tags:
        if word.lower() not in set(stopwords.words('english')):
            newlist.append(tuple([word, pos_dict.get(tag[0])]))
    return newlist
    
   

#The function below, Lemma, creates a list for the lemmas gained from the stem words
# we were able to find from the text. 

wordnet_lemmatizer = WordNetLemmatizer()

def lemmatize(pos_data):
    lemma_rew = " "
    for word, pos in pos_data:
        if not pos:
            lemma = word
            lemma_rew = lemma_rew + " " + lemma
        else:
            lemma = wordnet_lemmatizer.lemmatize(word, pos=pos)
            lemma_rew = lemma_rew + " " + lemma
    return lemma_rew

#The below functions are intended to return the sentiments found from the use of 
# TextBlob. They were not used because of their ineffectiveness

'''   
def getSubjectivity(review):
    return TextBlob(review).sentiment.subjectivity

def getPolarity(review):
    return TextBlob(review).sentiment.polarity

def analysis(score):
    if score < 0:
        return "Negative"
    elif score == 0:
        return "Neutral"
    else:
        return "Positive"
'''

#The vader functions below perform the same tasks as the TextBlob functions above
# except they are to be used instead because of their effectiveness when it comes to literature

analyzer = SentimentIntensityAnalyzer()
def vadersentimentanalysis(review):
    vs = analyzer.polarity_scores(review)
    return vs['compound']

def vader_analysis(compound):
    if compound >= 0.5:
        return 'Positive'
    elif compound <= -0.5 :
        return 'Negative'
    else:
        return 'Neutral'

#The below is simply just the read in, pre-processing, and returning of sentiments 
# as intended as the purpose of the program

raw_text = ""

with open(r'C:\Users\donov\Documents\homework\input.txt', 'rt') as file_in:
    for line in file_in:
        raw_text = raw_text + line

paragraph_1_raw = raw_text[:1481]
paragraph_2_raw = raw_text[1484:]

data = [{'The text': raw_text[:1481]}, {'The text': raw_text[1484:]}]
df = pd.DataFrame(data, index=['Paragraph_1','Paragraph_2'], columns = ['The text'])

df['Cleaned text'] = df['The text'].apply(clean_text)
df['POS tagged'] = df['Cleaned text'].apply(token_stop_pos)
df['Lemma'] = df['POS tagged'].apply(lemmatize)

final_data = pd.DataFrame(df[['The text', 'Lemma']])


final_data['Vader Sentiment'] = final_data['The text'].apply(vadersentimentanalysis)
final_data['Vader Analysis'] = final_data['Vader Sentiment'].apply(vader_analysis)

'''
final_data['Subjectivity'] = final_data['Cleaned text'].apply(getSubjectivity) 
final_data['Polarity'] = final_data['Cleaned text'].apply(getPolarity) 
final_data['Analysis'] = final_data['Polarity'].apply(analysis)
'''

print(final_data.head())


list_pieces = []
for t in df['The text']:
    split = split_text(t, 10)
    list_pieces.append(split)

polarity_transcript = []
for lp in list_pieces:
    polarity_piece = []
    for p in lp:
        polarity_piece.append(vadersentimentanalysis(p))
    polarity_transcript.append(polarity_piece)
    
print(polarity_transcript[1])
    
plt.plot(polarity_transcript[1])
plt.title("Paragraph_2 polarity over time")
plt.show()
