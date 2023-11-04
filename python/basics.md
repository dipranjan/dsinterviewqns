---
description: This page deals with Basic Python Questions
---

# Basics

There are some common programming techniques that you must be familiar with if you want to be comfortable enough to solve Python questions live during an interview. Here we have summarized a few of such techniques but do hone your skills using platforms like Leet code to ensure that you perform well during interviews.

We have collated some resources from the internet as a starting point to help you prepare on this:

* [14 Coding Interview Patterns](https://hackernoon.com/14-patterns-to-ace-any-coding-interview-question-c5bb3357f6ed)
* [Sliding Window patterns](https://leetcode.com/problems/frequency-of-the-most-frequent-element/solutions/1175088/C++-Maximum-Sliding-Window-Cheatsheet-Template/)
* [Two Pointers Patterns](https://leetcode.com/discuss/study-guide/1688903/Solved-all-two-pointers-problems-in-100-days)
* [Substring Problem Patterns](https://leetcode.com/problems/minimum-window-substring/solutions/26808/Here-is-a-10-line-template-that-can-solve-most-'substring'-problems/)
* [Dynamic Programming Patterns](https://leetcode.com/discuss/study-guide/458695/Dynamic-Programming-Patterns)
* [Binary Search Patterns](https://leetcode.com/discuss/study-guide/786126/Python-Powerful-Ultimate-Binary-Search-Template.-Solved-many-problems)
* [Backtracking Patterns](https://leetcode.com/problems/permutations/solutions/18239/A-general-approach-to-backtracking-questions-in-Java-\(Subsets-Permutations-Combination-Sum-Palindrome-Partioning\)/)
* [Tree Patterns](https://leetcode.com/discuss/study-guide/937307/Iterative-or-Recursive-or-DFS-and-BFS-Tree-Traversal-or-In-Pre-Post-and-LevelOrder-or-Views)
  * [Tree Iterative Traversal](https://medium.com/leetcode-patterns/leetcode-pattern-0-iterative-traversals-on-trees-d373568eb0ec)
  * [Tree Question Pattern](https://leetcode.com/discuss/study-guide/2879240/TREE-QUESTION-PATTERN-2023-oror-TREE-STUDY-GUIDE)
* [Graph Patterns](https://leetcode.com/discuss/study-guide/655708/Graph-For-Beginners-Problems-or-Pattern-or-Sample-Solutions)
* [Monotonic Stack Patterns](https://leetcode.com/discuss/study-guide/2347639/A-comprehensive-guide-and-template-for-monotonic-stack-based-problems)
* [Bit Manipulation Patterns](https://leetcode.com/discuss/study-guide/3901862/All-Types-of-Patterns-for-Bits-Manipulations-and-How-to-use-it)
* [String Question Patterns](https://leetcode.com/discuss/study-guide/2001789/Collections-of-Important-String-questions-Pattern)
* [DFS + BFS Patterns (1)](https://medium.com/leetcode-patterns/leetcode-pattern-2-dfs-bfs-25-of-the-problems-part-2-a5b269597f52)
* [DFS + BFS Patterns (2)](https://medium.com/leetcode-patterns/leetcode-pattern-2-dfs-bfs-25-of-the-problems-part-2-a5b269597f52)

### Questions

<details>

<summary>[SNAPCHAT] Palindrome Checker</summary>

Given a string, determine whether any permutation of it is a palindrome.

For example, _carerac_ should return _true_, since it can be rearranged to form _racecar_, which is a palindrome. _sunset_ should return _false_, since there’s no rearrangement that can form a palindrome.

**Answer**

<pre class="language-python"><code class="lang-python"># A string can be a palindrome only if it has even pair of characters and at max 1 odd character
<strong>def palindrome(x):
</strong>    char_dict = {}
    for i in x:
# we will check if the element exists else we will add it to the dictionary
        try:
            char_dict[i] = char_dict[i] + 1
        except:
            char_dict.update({i:1})
 # next we will create a list of element counts and use list comprehension 
 # to check if odd element count is 1 and rest all even           
    check = list(char_dict.values())
    if (len([temp for temp in check if temp%2==1]) == 1 and len([temp for temp in check if temp%2==0]) > 1):
        return "palindrome"
    else:
        return "not palindrome"
    
print(palindrome("carerac"))
print(palindrome("abc"))
</code></pre>

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

```python
def pyramid(n):
    counter = 1
    max = 1
    while(max<n):
        for i in range(max, max+counter): # for the second pattern change max to 1
            print(i, end=" ")
            max=max+1
        counter=counter+1
        print(" ")
    
pyramid(6)
```

</details>

<details>

<summary>[UBER] <a href="https://leetcode.com/problems/combination-sum/description/">Sum to N</a></summary>

Given a list of positive integers, find all combinations that equal the value N.

Example:

_integers = \[2,3,5], target = 8,_

_output = \[\[2,2,2,2],\[2,3,3],\[3,5]]_

**Answer**

```python
def combinationSum(candidates, target):
    ans = []                                        # for adding all the answers
    def traverse(candid, arr, sm):                  # arr : an array that contains the accused combination; sm : is the sum of all elements of arr 
        if sm == target: ans.append(arr)            # If sum is equal to target then add it to the final list
        if sm >= target: return                     # If sum is greater than target then no need to move further.
        for i in range(len(candid)):                # we will traverse each element from the array.
            traverse(candid[i:], arr + [candid[i]], sm+candid[i])   #most important, splice the array including the current index, splicing in order to handle the duplicates.
    traverse(candidates,[], 0)
    return ans

combinationSum([2, 3, 5], 8)
```

</details>

<details>

<summary>[STARBUCKS] Max Profit</summary>

Given a list of stock prices in ascending order by datetime, write a function that outputs the max profit by buying and selling at a specific interval.

_Example:_

_stock\_prices = \[10,5,20,32,25,12]_

_buy –> 5 sell –> 32_

**Answer**

```python
li = [10,5,20,32,25,12]
diff = 0
for i,j in enumerate(li):
    try:
        if(diff<(max(li[i+1:])-j)):
            diff = max(li[i+1:])-j
            buy = j
            sell = max(li[i+1:])
        print(j, max(li[i+1:]))
    except:
        print("end")
    
print(buy, sell, diff)
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

_nums = \[0,1,2,4,5] missingNumber(nums) -> 3_

Complexity of O(N) required.

**Answer**

```python
def missingNumber(nums):

  diff = 0
  miss_num = []
  for i, j in enumerate(nums):
    try:
      t_diff = nums[i+1]-nums[i]
      if t_diff>0:
        for k in range(i+1,i+t_diff):
          # print(k)
          miss_num.append(k)
    except:
      pass
  return miss_num

nums = [0,1,2,5,6]
missingNumber(nums)
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

`tuple_list = [(2, 3), (-3, 5), (4, 6), (5, 7)] x_range = (0, 1)`

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

<details>

<summary>Find the majority element in a list.</summary>

a = \[2,3,4,6, 6, 2,2] answer --> 2

**Answer**

```python
a = [2,3,4,6, 6, 2,2]

def major_ele(x):
    counter_dict = {}
    for i in a:
        if i not in counter_dict:
           counter_dict.update({i:1})
        else:
           counter_dict[i] =  counter_dict[i] + 1 
    for i,j in counter_dict.items():
        if j == max(list(counter_dict.values())):
            return i

print(major_ele(a))
```

</details>

<details>

<summary>[INTUIT] Iterator</summary>

Implement an iterator function which takes three iterators as the input and sorts them.

**Answer**

2 Solutions are provided below:

```python
import heapq

def sorted_merge(*iterators):
    # Use heapq.merge to merge and sort the input iterators
    sorted_iterator = heapq.merge(*iterators)
    
    # Return the sorted iterator
    return sorted_iterator

# Example usage:
if __name__ == "__main__":
    # Create three sorted iterators (lists in this case)
    iterator1 = iter([1, 3, 5, 7])
    iterator2 = iter([2, 4, 6, 8])
    iterator3 = iter([0, 9, 10])
    
    # Merge and sort the iterators
    sorted_iterator = sorted_merge(iterator1, iterator2, iterator3)
    
    # Iterate through the sorted values
    for value in sorted_iterator:
        print(value)

```

```python
def sort_iterators(it1, it2, it3):
  """Sorts three iterators.

  Args:
    it1: The first iterator.
    it2: The second iterator.
    it3: The third iterator.

  Returns:
    An iterator that yields the sorted elements of the three iterators.
  """
  # Create a list to store the elements of the three iterators.
  elements = []

  # Iterate over the three iterators and add the elements to the list.
  for element in it1:
    elements.append(element)
  for element in it2:
    elements.append(element)
  for element in it3:
    elements.append(element)

  # Sort the list.
  elements.sort()

  # Create an iterator that yields the elements of the sorted list.
  return iter(elements)
```

</details>

<details>

<summary>[SPLUNK] Last Page Number</summary>

We're given a string of integers that represent page numbers.

Write a function to return the last page number in the string. If the string of integers is not in correct page order, return the last number in order.

```
input = '12345'
output = 5

input = '12345678910111213'
output = 13

input = '1235678'
output = 3
```

**Answer**

```python
def get_last_page(int_string):
    print(int_string)
    count = 0
    counter2 = 0
    for i in int_string:
        count = count+1+counter2//10
        counter2 = counter2+1
        if(str(counter2)==int_string[count-1:count+counter2//10]):
            pass
        else:
            return counter2-1
```

</details>

<details>

<summary>Python Recursion</summary>

Explain Python recursion with an example.

**Answer**

Recursion is a programming technique that allows a function to call itself. This can be useful for solving problems that involve self-similar structures, such as trees and graphs.

```python
def factorial(n): # 6! = 6*3*2*1
  if(n==0 or n==1): # define the base case
    return 1
  return factorial(n-1)*n # recursively call the func

factorial(6)
```

This function works by calling itself recursively to calculate the factorial. The base cases are when n is 0 or 1, in which case the function simply returns n.

Recursion can be a powerful tool, but it is important to use it carefully. If a recursive function is not designed carefully, it can easily lead to stack overflows.

</details>

<details>

<summary>[INTUIT] <a href="https://leetcode.com/problems/subarray-product-less-than-k/">Subarray Product Less Than K</a></summary>

This was asked in INTUIT Sr. Data Scientist initial round using Glider

Given an array of integers `nums` and an integer `k`, return _the number of contiguous subarrays where the product of all the elements in the subarray is strictly less than_ `k`.

&#x20;**Example 1:**

<pre><code><strong>Input: nums = [10,5,2,6], k = 100
</strong><strong>Output: 8
</strong><strong>Explanation: The 8 subarrays that have product less than 100 are:
</strong>[10], [5], [2], [6], [10, 5], [5, 2], [2, 6], [5, 2, 6]
Note that [10, 5, 2] is not included as the product of 100 is not strictly less than k.
</code></pre>

**Example 2:**

<pre><code><strong>Input: nums = [1,2,3], k = 0
</strong><strong>Output: 0
</strong></code></pre>

&#x20;**Constraints:**

* `1 <= nums.length <= 3 * 104`
* `1 <= nums[i] <= 1000`
* `0 <= k <= 106`

**Answer**

You are not only required to solve the problem in a limited time frame (\~30mins) but the ask is also to ensure that the all test-cases pass and at least one of them fails if the code does not meet the required time complexity even if you get the required answer.

```python
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], max_product: int) -> int:        
        result = 0
        for i in range(1, len(nums)):
            for j, l in enumerate(nums):
                temp = nums[j:j+i]
                res = 1
                for m in temp:
                    res = m*res
                if(res<max_product and len(temp)==i):
                    result +=1      
        return result
```

The above code fails some test cases as it has O(n^3) complexity. There is the two-pointer or inchworm approach given below which solves the problem along with taking care of the complexity. Click on the Leetcode link above and check the discussions if you want to understand it better:

```python
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], max_product: int) -> int:        
        left = 0
        result = 0
        product = 1
        
        for right in range(len(nums)):
            product *= nums[right]
            
            if product >= max_product:
                while product >= max_product and left <= right:
                    product /= nums[left]
                    left += 1
            
            result += right - left + 1
        
        return result
```



</details>

<details>

<summary><a href="https://leetcode.com/problems/reverse-vowels-of-a-string/description/?envType=study-plan-v2&#x26;envId=leetcode-75">Reverse Vowels in a String</a></summary>

Given a string `s`, reverse only all the vowels in the string and return it.

The vowels are `'a'`, `'e'`, `'i'`, `'o'`, and `'u'`, and they can appear in both lower and upper cases, more than once.

**Example 1:**

<pre><code><strong>Input: s = "hello"
</strong><strong>Output: "holle"
</strong></code></pre>

**Example 2:**

<pre><code><strong>Input: s = "leetcode"
</strong><strong>Output: "leotcede"
</strong></code></pre>

**Answer**

This can be solved using the 2-pointer approach:

```python
class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        vow = "aeiouAEIOU"
        left = 0
        right = len(s)-1
        while left < right:
            if s[left] in vow and s[right] in vow:
                
                s[left], s[right] = s[right], s[left]
                
                left += 1; right -= 1
            
            elif s[left] not in vow:
                left += 1
            
            elif s[right] not in vow:
                right -= 1            
        return ''.join(s)
```

</details>

<details>

<summary><a href="https://leetcode.com/problems/move-zeroes/description/?envType=study-plan-v2&#x26;envId=leetcode-75">Swap numbers</a></summary>

Given an integer array `nums`, move all `0`'s to the end of it while maintaining the relative order of the non-zero elements.

**Note** that you must do this in-place without making a copy of the array.

**Example:**

<pre><code><strong>Input: nums = [0,1,0,3,12]
</strong><strong>Output: [1,3,12,0,0]
</strong></code></pre>

**Answer**

```python
class Solution:
    def moveZeroes(self, nums: list) -> None:
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]

            # wait while we find a non-zero element to
            # swap with you
            if nums[slow] != 0:
                slow += 1
```

**Algorithm complexity:**\
_Time complexity: O(n)_. Our fast pointer does not visit the same spot twice.\
_Space complexity: O(1)_. All operations are made in-place

</details>

<details>

<summary>[SALESFORCE] Interpolation</summary>

![](<../.gitbook/assets/image (1).png>)

**Answer**

```python
x = [25, 50, 100]
y = [5.0, 4.0, 3.0]

def interporlate(n):
  if(n in x):
    return y[x.index(n)]
  elif(n > x[-1]):
    x_t = x[-1]-x[-2]
    y_t = y[-1]-y[-2]
    return y[-1] + (y_t / x_t * (n-x[-1]))
  elif(n < x[0]):
    x_t = x[0]-x[1]
    y_t = y[0]-y[1]
    return y[0] + (y_t / x_t * (n-x[0]))
  else:
    for i,j in enumerate(x):
      if n<j:
        break
    x_t = x[i-1]-x[i]
    y_t = y[i-1]-y[i]
    return y[i-1] + (y_t / x_t * (n-x[i-1]))


print(interporlate(50))
print(interporlate(150))
print(interporlate(25))
print(interporlate(75))
```

</details>

<details>

<summary>[SALESFORCE] Prison Problem</summary>

<img src="../.gitbook/assets/image (2).png" alt="" data-size="original">

**Answer**

```python
def prison(size, x, y):
  x_t = list(range(0,6,1))
  y_t = list(range(0,6,1))
  x_t = [a for a in x_t if a not in x]
  y_t = [a for a in y_t if a not in y]

  # accounting for the outer walls, we will add 0 as starting
  # and add +1 to all others
  x_t = list(map(lambda t: t + 1, x_t))
  y_t = list(map(lambda t: t + 1, y_t))
  x_t.insert(0,0)
  y_t.insert(0,0)

  max_x = 1
  max_y = 1

  for i,j in enumerate(x_t):
    try:
      if(max_x< x_t[i+1]-j):
        max_x = x_t[i+1] -j    
    except:
      pass

  for i,j in enumerate(y_t):
    try:
      if(max_y< y_t[i+1]-j):
        max_y = y_t[i+1] -j
    except:
      pass

  return "Max cell size: ", max_x*max_y


prison(5, [3, 2], [0, 1, 3])
```

</details>
