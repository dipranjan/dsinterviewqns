#!/usr/bin/env python
# coding: utf-8

# ## NLP

# ```{admonition} Problem: [OKCUPID] Term Frequency
# :class: dropdown, tip
# 
# Say you are given a text document in the form of a string with the following sentences:
# 
# **Input**
# 
# `
# document = "I have a nice car with a nice tires"
# `
# 
# **Output**
# 
# `
# {
# "I":0.11,
# "have":0.11,
# "a":0.22,
# "nice":0.22,
# "car": 0.11,
# "with":0.11,
# "tires":0.11
# }
# `
# Write a program in python to determine the TF (term frequency) values for each term of this document.
# ```

# In[10]:


# term freq = freq of term 't' in doc 'd' / total terms in 'd'

def tf(doc):
    temp_list = doc.split(" ") # split terms
    final_dict = {} # store final dictionary with term freq
    for i in temp_list:
        if i not in final_dict.keys(): # check if term is already present in dict
            final_dict[i] = round(temp_list.count(i)/len(temp_list),2) # calculating tf
    return final_dict

tf("I have a nice car with a nice tires")

