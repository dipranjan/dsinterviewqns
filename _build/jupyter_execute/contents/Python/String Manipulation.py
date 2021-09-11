#!/usr/bin/env python
# coding: utf-8

# ## String Manipulation

# ```{admonition} Problem:
# :class: tip
# 
# **Asked By - SNAPCHAT**
# 
# Given a string, determine whether any permutation of it is a palindrome.
# 
# For example, carerac should return true, since it can be rearranged to form racecar, which is a palindrome. sunset should return false, since there's no rearrangement that can form a palindrome.
# ```

# In[21]:


'''
A string can be a palindrome only if it has even pair of characters and at max 1 odd character
'''

def palindrome_checker(txt):
    temp = {}
    odd_count = 0
    even_count = 0
    for i in (txt): # Storing characters and their count
        if i in temp.keys():
            temp[i] = temp[i] + 1
        else:
            temp[i] = 1
    for i in temp: # Check count of characters
        if temp[i]%2==0:
            even_count = even_count + 1
        else:
            odd_count = odd_count + 1
    if((odd_count>1)or(even_count==0)):
        return False
    else:
        return True    
    
print(palindrome_checker("carerac"))
print(palindrome_checker("sunset"))


# ```{admonition} Problem:
# :class: tip
# Write a function to generate this pattern:
# 1
# 2 3
# 4 5 6
# 
# Change the code to output
# 1
# 1 2
# 1 2 3
# ```

# In[27]:


def pyramid(n):
    i = 1
    j = 1
    while i < n:
        for k in range(1,j):
            print(i, end=' ') # For the second pattern change i to k
            i += 1
        print(" ") 
        j +=1

pyramid(6)

