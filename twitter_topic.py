#-*- coding: utf-8 -*-

"""
This function returns top 10 most twitter topics and visualizes the data set.
"""
import logging
import random
import pandas as pd
from collections import defaultdict
import sys
import os
import logging
import codecs
import operator
import numpy as np
from suffix_rules import balRules
from noun_rules import get_truncated
from gensim import corpora, models, similarities
from tethne.model.corpus import mallet
import pyLDAvis.gensim
import gensim


reload(sys)
sys.setdefaultencoding("utf-8")



dic = {} #dictionary that contains only the filtered words
dixt= {} #dictionary that conatains the final appropriate words
discard_list = []

#Receives list of tweets and returns list of list of each words in tweets
def get_new_data(tweet_list):
    #get stop words
	stop_words=get_common_words()
	new_list=[]
    #gets each tweet from tweet list

	tweet_list= [filter(None,[(get_truncated(word)).lstrip().rstrip() for word in balRules(remove_digits(tweet).split(" ")) if word not in stop_words and len(word)>0]) for tweet in tweet_list]
	print "Stemming completed"
	return tweet_list

#removes digits and punctuation marks from a unicode string
def remove_digits(news):
	file_list=[]
	with open("np_digits.txt","r") as f:
		file_list=[value.replace("\n","") for value in list(f)]
	chars_to_remove = file_list
	subj = news
	dd=dict((ord(unicode(char)), None) for char in chars_to_remove)
	subj=subj.translate(dd)
	return subj

def get_common_words():
	file_list=[]
	f=codecs.open("common_words_list.txt",'r',encoding='utf-8')
	for file in f:
		file_list.append(file[:-1])
	return file_list




def count(lists):
    """
    This functions counts the frequency of each word in the dataset
    """
    for news in lists:
    	for true_news in news:

            dic[true_news] = dic.get(true_news,0) + 1


def single_words(news_list):
    """
    This function contains a list of words that has a length of 1 or less 
    and will be added to the discarded list
    """
    for text in news_list:
        for true_text in text:
            if len(true_text) <= 1:
                discard_list.append(true_text)

def discard():
    """
    This fucntion contains a list of words that will be discarded.
    """

    for key,value in dic.items():
        if value == 1 or value == 80:
        	discard_list.append(key)    
    return discard_list
    
    



if __name__=="__main__":

  
    
    first_list = []
    final_list = []

    location = 'pes2.csv'
    df = pd.read_csv(location,encoding='utf-8')
    for first in df.nepali:
    	first_list.append(first)    

    news_list=get_new_data(first_list)
    

    single_words(news_list)
    count(news_list)
    discard_list = discard()


    for text in news_list:
        
        for true_text in text:
            line_list=[]
            if true_text  not in discard_list:
                line_list.append(true_text)
        final_list.append(line_list)
    

    dictionary = corpora.Dictionary(final_list)
    dictionary.save('/tmp/tweets.dict') #storing the dictionary for future refernece
    corpus = [dictionary.doc2bow(tweet) for tweet in final_list] #doc2bow simply counts 
    #the number of occurrences of each distinct word, converts the word 
    #to its integer word id and returns the result as a sparse vector
    corpora.MmCorpus.serialize('/tmp/tweets.mm', corpus)  # store to disk, for later use
    dictionary = corpora.Dictionary.load('/tmp/tweets.dict')
    corpus=corpora.MmCorpus('/tmp/tweets.mm')
    print " file is saved."
    
    
    if (os.path.exists("/tmp/tweets.dict")):
        dictionary = corpora.Dictionary.load('/tmp/tweets.dict')
        corpus = corpora.MmCorpus('/tmp/tweets.mm')
        print("Used files generated from first tutorial")
    else:
        print("Please run first tutorial to generate data set")
    # Creating the object for LDA model using gensim library
    Lda = gensim.models.ldamodel.LdaModel
    ldamodel = Lda(corpus, num_topics=10, id2word = dictionary, passes=20) 

    ## Shows the frequency of words in the topics through pyLDAvis
    #ldamodel.showtopics() #shows topics
    model_show=pyLDAvis.gensim.prepare(ldamodel, corpus, dictionary)
    pyLDAvis.save_html(model_show,"model.html")


    