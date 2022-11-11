---
description: This page deals with Basic Python Questions
---

# Basics

### Questions[#](broken-reference)

<details>

<summary>[SNAPCHAT] Palindrome Checker</summary>

Given a string, determine whether any permutation of it is a palindrome.

For example, _carerac_ should return _true_, since it can be rearranged to form _racecar_, which is a palindrome. _sunset_ should return _false_, since there’s no rearrangement that can form a palindrome.

**Answer**

```python
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
```

</details>

<details>

<summary>Pattern Generation</summary>

Write a function to generate this pattern:\
1\
2 3\
4 5 6

Now change the code to output\
1\
1 2\
1 2 3

**Answer**

<pre class="language-python"><code class="lang-python"><strong>def pyramid(n):
</strong>    i = 1
    j = 1
    while i &#x3C; n:
        for k in range(1,j):
            print(i, end=' ') # For the second pattern change i to k
            i += 1
        print(" ") 
        j +=1

pyramid(6)</code></pre>

</details>

<details>

<summary>[UBER] Sum to N</summary>

Given a list of integers, find all combinations that equal the value N.

Example:

_integers = \[2,3,5], target = 8,_

_output = \[\[2,2,2,2],\[2,3,3],\[3,5]]_

**Answer**

{% code overflow="wrap" %}
```python
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

a([2,3,5],8)ython
```
{% endcode %}

</details>

<details>

<summary>[STARBUCKS] Max Profit</summary>

Given a list of stock prices in ascending order by datetime, write a function that outputs the max profit by buying and selling at a specific interval.

_Example:_

_stock\_prices = \[10,5,20,32,25,12]_

_buy –> 5 sell –> 32_

**Answer**

```python
stock_prices = [10,5,20,32,25,12]

diff = []
for i,j in enumerate(stock_prices):
    for k in range(i+1,len(stock_prices)):
        diff.append(stock_prices[k]-j)
        if(len(diff)>2 and (diff[-1]> max(diff[:-1]))):
            buy = j
            sell = stock_prices[k]

print(buy,sell)
```

</details>

<details>

<summary>[IBM] Isomorphic string check</summary>

Write a function which will check if each character of string1 can be mapped to a unique character of string2.

_Example: string1 = ‘donut’ string2 = ‘fatty’_

_string\_map(string1, string2) == False # as n and u both get mapped to t_

_string1 = ‘enemy’ string2 = ‘enemy’_

_string\_map(string1, string2) == True # as e’s get mapped to e even though there is two e_

_string1 = ‘enemy’ string2 = ‘yneme’_

_string\_map(string1, string2) == False # as e’s dont get mapped uniquely_

**Answer**

```python
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
```

</details>

<details>

<summary>[WORKDAY] Sorted String merge</summary>

Given two sorted lists, write a function to merge them into one sorted list.

What’s the time complexity?

**Answer**

{% code overflow="wrap" %}
```python
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
```
{% endcode %}

</details>

<details>

<summary>[POSTMATES] Weekly Aggregation</summary>

Given a list of timestamps in sequential order, return a list of lists grouped by week (7 days) using the first timestamp as the starting point.

_Example:_

_ts = \[ ‘2019-01-01’, ‘2019-01-02’, ‘2019-01-08’, ‘2019-02-01’, ‘2019-02-02’, ‘2019-02-05’, ]_

_output = \[ \[‘2019-01-01’, ‘2019-01-02’], \[‘2019-01-08’], \[‘2019-02-01’, ‘2019-02-02’], \[‘2019-02-05’] ]_

**Answer**

{% code overflow="wrap" %}
```python
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
```
{% endcode %}

</details>

<details>

<summary>[MICROSOFT] Find the missing number</summary>

You have an array of integers of length n spanning 0 to n with one missing. Write a function that returns the missing number in the array

_Example:_

_nums = \[0,1,2,4,5] missingNumber(nums) -> 3_&#x20;

Complexity of O(N) required.

**Answer**

```python
nums = [0,1,2,4,5]

for i in range(0,len(nums)-1):
    if(nums[i+1]-nums[i]>1):
        print(nums[i]+1)
```

</details>

<details>

<summary>[SQUARE] Book Combinations</summary>

You have store credit of N dollars. However, you don’t want to walk a long distance with heavy books, but you want to spend all of your store credit.

Let’s say we have a list of books in the format of tuples where the first value is the price and the second value is the weight of the book -> (price,weight).

Write a function _optimal\_books_ to retrieve the combination allows you to spend all of your store credit while getting at least two books at the lowest weight.

_Note: you should spend all your credit and getting at least 2 books, If no such condition satisfied just return empty list._

_Example:_

```
N = 18
books = [(17,8), (9,4), (18,5), (11,9), (1,2), (13,7), (7,5), (3,6), (10,8)]

def optimal_books(N, books) -> [(17,8),(1,2)]
```

**Answer**

{% code overflow="wrap" %}
```python
# Let's take this step by step
import itertools

def optimal_books(N, books):
    print("(Price,Weight) details of books: ",books)
    print("Store Credit: ",N)
    final_books = [] # empty list to store the final books
    # sorting the books by weight as we need the lightest books
    sorted_books = sorted(books, key = lambda x:x[1]) 
    price = [i[0] for i in sorted_books] #list of prices sorted by weight
    
    for i in range(2,len(price)+1):
        templist = (list(itertools.combinations(price,i))) # generating all combinations of price
        res = [sum(j) for j in templist] # summing individual combination to get total price of each combination
        if N in res: # if the result matches traceback traceback and append the combination         
            tempbooks = (templist[res.index(N)])            
            for k in tempbooks:
                final_books.append(sorted_books[price.index(k)])            
            break
            
    return final_books
        
N = 18
books = [(17,8), (9,4), (18,5), (11,9), (1,2), (13,7), (7,5), (3,6), (10,8)]
print("Best Combination: ",optimal_books(N,books))
```
{% endcode %}

</details>

<details>

<summary>[WISH] Intersecting Lines</summary>

Say you are given a list of tuples where the first element is the slope of a line and the second element is the y-intercept of a line.

Write a function find\_intersecting to find which lines, if any, intersect with any of the others in the given x\_range.

_Example_

`tuple_list = [(2, 3), (-3, 5), (4, 6), (5, 7)] x_range = (0, 1)`&#x20;

_Output_

`def find_intersecting(tuple_list, x_range) -> [(2,3), (-3,5)]`

**Answer**

```python
# for 2 lines to intersect the formulas used here are:
# y = mx + c
# x = (c2-c1)/(m1-m2)
# https://www.cuemath.com/geometry/intersection-of-two-lines/ Check this link for details of the formula

def intersectinglines(tuple_list,x_range):
    output=[]
    for i in range(len(tuple_list)):
        for j in range(i+1,len(tuple_list)):

            x = (tuple_list[j][1]-tuple_list[i][1])/(tuple_list[i][0]-tuple_list[j][0])
            y = tuple_list[j][1]*x+tuple_list[j][0]

            if x>=x_range[0] and x<=x_range[1]:
                output.extend([tuple_list[i],tuple_list[j]])
    return output

tuple_list = [(2, 3), (-3, 5), (4, 6), (5, 7)]
x_range = (0, 1)

intersectinglines(tuple_list, x_range)
```

</details>
