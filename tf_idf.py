
# coding: utf-8

# ## CS 401 Applied Data Analysis, 2018 autumn
# ## Final Project: Exploration on Media polarity in the News
# ##### Group Members: Ruibin Huang, Liangwei Chen, Fengyu Cai

# #### Objective: In this project, we would like to dig up the potential media polarity about the news on the websites. The main steps of our projects are:
# - Label the news with keywords or topic
#     - Method: TF-IDF
# - Select specific news and medias for analysis
#     - NLTK sentiment analysis package
# - Further analyze based on the chronological and geometrical features of the medias
#     - map or plot

# Technologies applied: spark, Machine Learning, NLTK
# 1. all sentiment analysis packages: stanford corenlp
# 2. Statistics
# 3. Whether we can use other data
# 4. Trump and Cliton: election state

# In[2]:

import sys
import os
from sklearn.feature_extraction.text import TfidfTransformer
from sklearn.feature_extraction.text import CountVectorizer
import re
import pandas as pd
import numpy as np
import gc


# ## Part1: Topic Tagging

# In[2]:

data_path = './data'
file_list = os.listdir(data_path)
file_pd = {}


# In[3]:

countvec = CountVectorizer(stop_words='english', ngram_range=(1,2))


# In[4]:

tfidfvec = TfidfTransformer()


# In[5]:

for file in file_list:
    try:
        file_pd[file] = pd.read_csv(os.path.join(data_path, file), sep='\t', header=None, error_bad_lines=False).dropna()
        file_pd[file].column = ['id', 'word_id', 'word', 'stemmed', 'postag']
    except:
        continue


# In[7]:
file_selected = list(file_pd.keys())


txt_new = {}
for k, v in file_pd.items():
    txt_new[k] = ' '.join(v[3].tolist())


# In[8]:
del file_pd
gc.collect()

txt_list = list(txt_new.values())


# In[9]:

word_freq = countvec.fit_transform(txt_list)


# In[10]:

tfidf = tfidfvec.fit_transform(word_freq)


# In[11]:

tfidf_array = tfidf.toarray()


# In[1]:

word_dic = countvec.get_feature_names()


# In[ ]:

# tfidf_array_sorted = np.argsort(tfidf_array, axis=-1)


# In[ ]:

topic_selection = {}
doc_num, feature_num = np.shape(tfidf_array)
for idx in range(doc_num):
    maxarg = np.argmax(tfidf_array[idx])
    topic_selection[file_selected[idx]] = (word_dic[maxarg], tfidf_array[i, maxarg])


# In[ ]:

import json
with open('record.txt', 'w') as file:
     file.write(json.dumps(topic_selection))

