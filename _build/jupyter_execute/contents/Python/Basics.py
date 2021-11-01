#!/usr/bin/env python
# coding: utf-8

# ## Basics

# ### Questions

# ```{admonition} Problem: [SNAPCHAT] Palindrome Checker
# :class: dropdown, tip
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


# ```{admonition} Problem: [UBER] Sum to N
# :class: dropdown, tip
# 
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


# ```{admonition} Problem: [STARBUCKS] Max Profit
# :class: dropdown, tip
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


# ```{admonition} Problem: [IBM] Isomorphic string check
# :class: dropdown, tip
# 
# Write a function which will check if each character of string1 can be mapped to a unique character of string2.
# 
# Example: 
# string1 = 'donut'
# string2 = 'fatty'
# 
# string_map(string1, string2) == False # as n and u both get mapped to t
# 
# string1 = 'enemy'
# string2 = 'enemy'
# 
# string_map(string1, string2) == True # as e's get mapped to e even though there is two e
# 
# string1 = 'enemy'
# string2 = 'yneme'
# 
# string_map(string1, string2) == False # as e's dont get mapped uniquely
# 
# ```

# In[49]:


def string_map(string1, string2):    
    if(string1==string2):
        status = True
    elif(len(string1)!=len(string2)):
        status = False
    else:
        tempstore = {}
        for i,j in enumerate(string1):
            if(j in tempstore):               
                if(tempstore[j] != string2[i]):
                    status = False
                    break
            elif(string2[i] in tempstore.values()):
                    status = False
                    break
            else:
                tempstore[j] = string2[i]
                status = True
    return status

print(string_map('enemy', 'enemy'))
print(string_map('enemy', 'yneme'))
print(string_map('cat', 'ftt'))
print(string_map('ctt', 'fat'))
print(string_map('cat', 'fat'))


# ```{admonition} Problem: [WORKDAY] Sorted String merge
# :class: dropdown, tip
# 
# Given two sorted lists, write a function to merge them into one sorted list.
# 
# What's the time complexity?
# 
# ```

# In[58]:


def mergeArrays(arr1, arr2):
    
    n1 = len(arr1)
    n2 = len(arr2)
    arr3 = [None] * (n1 + n2)
    i = 0
    j = 0
    k = 0
    # Traverse both array
    while i < n1 and j < n2:     
        # Check if current element of first array is smaller than current element of second array. 
        # If yes, store first array element and increment first array index. Otherwise do same with second array
        
        if arr1[i] < arr2[j]:
            arr3[k] = arr1[i]
            k = k + 1
            i = i + 1
        else:
            arr3[k] = arr2[j]
            k = k + 1
            j = j + 1
     
 
    # Store remaining elements
    # of first array
    while i < n1:
        arr3[k] = arr1[i];
        k = k + 1
        i = i + 1
 
    # Store remaining elements
    # of second array
    while j < n2:
        arr3[k] = arr2[j];
        k = k + 1
        j = j + 1
    print("Array after merging")
    for i in range(n1 + n2):
        print(str(arr3[i]), end = " ")
 

arr1 = [1, 3, 5, 7]
arr2 = [2, 4, 6, 8]
mergeArrays(arr1, arr2)

# Next coming to the time complexity it is linear as the execution time of the algorithm grows in direct proportion to the size of the data set it is processing.
# For merging two arrays, we are always going to iterate through both of them no matter what, 
# so the number of iterations will always be m+n and the time complexity being O(m+n) where m = len(arr1) and n = len(arr2)


# ```{admonition} Problem: [POSTMATES] Weekly Aggregation
# :class: dropdown, tip
# 
# Given a list of timestamps in sequential order, return a list of lists grouped by week (7 days) using the first timestamp as the starting point.
# 
# Example:
# 
# ts = [
#     '2019-01-01', 
#     '2019-01-02',
#     '2019-01-08', 
#     '2019-02-01', 
#     '2019-02-02',
#     '2019-02-05',
# ]
# 
# output = [
#     ['2019-01-01', '2019-01-02'], 
#     ['2019-01-08'], 
#     ['2019-02-01', '2019-02-02'],
#     ['2019-02-05'],
# ]
# 
# ```

# In[8]:


ts = [
    '2019-01-01', 
    '2019-01-02',
    '2019-01-08', 
    '2019-02-01', 
    '2019-02-02',
    '2019-02-05',
]

from datetime import datetime as dt
from itertools import groupby

first = dt.strptime(inp[0], "%Y-%m-%d")
out = []

for k, g in groupby(ts, key=lambda d: (dt.strptime(d, "%Y-%m-%d") - first).days // 7 ):
    out.append(list(g))

print(out)


# ```{admonition} Problem: [MICROSOFT] Find the missing number
# :class: dropdown, tip
# 
# You have an array of integers of length n spanning 0 to n with one missing. Write a function that returns the missing number in the array
# 
# Example:
# 
# nums = [0,1,2,4,5] 
# missingNumber(nums) -> 3
# Complexity of O(N) required.
# 
# ```

# In[13]:


nums = [0,1,2,4,5]

for i in range(0,len(nums)-1):
    if(nums[i+1]-nums[i]>1):
        print(nums[i]+1)        

