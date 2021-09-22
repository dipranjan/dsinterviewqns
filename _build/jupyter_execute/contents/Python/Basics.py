#!/usr/bin/env python
# coding: utf-8

# ## Basics

# ```{admonition} Problem: Palindrome Checker
# :class: dropdown, tip
# 
# **Asked By - SNAPCHAT**
# 
# Given a string, determine whether any permutation of it is a palindrome.
# 
# For example, carerac should return true, since it can be rearranged to form racecar, which is a palindrome. sunset should return false, since there's no rearrangement that can form a palindrome.
# ```

# In[1]:


# A string can be a palindrome only if it has even pair of characters and at max 1 odd character


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


# ```{admonition} Problem: Pattern Generation
# :class: dropdown, tip
# Write a function to generate this pattern:\
# 1\
# 2 3\
# 4 5 6
# 
# Now change the code to output\
# 1\
# 1 2\
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


# ```{admonition} Problem: Sum to N
# :class: dropdown, tip
# **Asked By - UBER**
# Given a list of integers, find all combinations that equal the value N.
# 
# Example: 
# 
# integers = [2,3,5], target = 8,
# 
# output = [[2,2,2,2],[2,3,3],[3,5]]
# ```

# In[79]:


# Ref: https://stackoverflow.com/questions/58415182/function-that-find-combination-of-values-that-sums-to-a-given-number

def a(lst, target):
    final_list = [] # list to store all the valid results
    
    def _a(idx, li):
        if target == sum(li): final_list.append(li)
        elif target < sum(li): return
        
        for u in range(idx, len(lst)):
            _a(u , li + [lst[u]]) # recursive call
        return final_list
    
    return _a(0, []) # initial call

a([2,3,5],8)


# ```{admonition} Problem: Max Profit
# :class: dropdown, tip
# **Asked By - STARBUCKS**
# 
# Given a list of stock prices in ascending order by datetime, write a function that outputs the max profit by buying and selling at a specific interval.
# 
# Example:
# 
# stock_prices = [10,5,20,32,25,12]
# 
# buy --> 5
# sell --> 32
# 
# ```

# In[27]:


stock_prices = [10,5,20,32,25,12]

diff = []
for i,j in enumerate(stock_prices):
    for k in range(i+1,len(stock_prices)):
        diff.append(stock_prices[k]-j)
        if(len(diff)>2 and (diff[-1]> max(diff[:-1]))):
            buy = j
            sell = stock_prices[k]

print(buy,sell)

