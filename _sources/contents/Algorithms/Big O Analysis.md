---
html_meta:
  "description lang=en": "Interview resource of Data Science Interview focusing on Machine Learning Framework Tensorflow."
  "keywords": "interview, data science, machine learning, BigO, Big-O, Algorithms"
  "property=og:locale": "en_US"
---

## Big O Analysis

Big O notation (with a capital letter O, not a zero), also called Landau's symbol, is a symbolism used in complexity theory, computer science, and mathematics to describe the asymptotic behavior of functions. Basically, it tells you how fast a function grows or declines.

## Why is Algorithm Analysis Important?

To understand why algorithm analysis is important, we will take help of a simple example.

Suppose a manager gives a task to two of his employees to design an algorithm in Python that calculates the factorial of a number entered by the user.

The manager has to decide which algorithm to use. To do so, he has to find the complexity of the algorithm. One way to do so is by finding the time required to execute the algorithms.

In the Jupyter notebook, you can use the `%timeit` literal followed by the function call to find the time taken by the function to execute. Look at the following script:

````{tab-set-code}

```{code-block} python
'''Alogrithm by Employee 1'''
def fact(n):
    product = 1
    '''Uses for loop'''
    for i in range(n):
        product = product * (i+1)
    return product

%timeit fact(50)

################################

'''Alogrithm by Employee 2'''
def fact(n):
    if n == 0:
        return 1
    else:
        '''Uses recursive call'''
        return n * fact(n-1)

%timeit fact(50)
```
````

Output - 
- 4.16 µs ± 15 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)
- 7.41 µs ± 142 ns per loop (mean ± std. dev. of 7 runs, 100000 loops each)


The execution time shows that the first algorithm is faster compared to the second algorithm involving recursion. This example shows the importance of algorithm analysis. In the case of large inputs, the performance difference can become more significant. However, **execution time is not a good metric to measure the complexity of an algorithm since it depends upon the hardware. A more objective complexity analysis metrics for the algorithms is needed.** This is where Big O notation comes to play.

## Algorithm Analysis with Big-O Notation

Big-O notation signifies the relationship between the input to the algorithm and the steps required to execute the algorithm. It is denoted by a big $O$ followed by opening and closing parenthesis. Inside the parenthesis, the relationship between the input and the steps taken by the algorithm is presented using $n$.

For instance, if there is a linear relationship between the input and the step taken by the algorithm to complete its execution, the Big-O notation used will be $O(n)$. Similarly, the Big-O notation for quadratic functions is $O(n^2)$

The following are some of the most common Big-O functions:

| **Name**    | **Big O**    |
|-------------|--------------|
| Constant    | $O(c)$       |
| Linear      | $O(n)$       |
| Quadratic   | $O(n^2)$     |
| Cubic       | $O(n^3)$     |
| Exponential | $O(2^n)$     |
| Logarithmic | $O(log(n))$  |
| Log Linear  | $O(nlog(n))$ |


```{figure} ../Algorithms/images/image16.PNG
---
height: 200px
name: image16
---
n is the input size and c is a positive constant
```

## Analogy
Imagine the following scenario: You've got a file on a hard drive and you need to send it to your friend who lives across the country. You need to get the file to your friend as fast as possible. How should you send it?

Most people's first thought would be email, FTP, or some other means of electronic transfer. That thought is reasonable, but only half correct. If it's a small file, you're certainly right. It would take 5 - 10 hours to get to an airport, hop on a flight, and then deliver it to your friend. But what if the file were really, really large? Is it possible that it's faster to physically deliver it via plane?

Yes, actually it is. A one-terabyte (1 TB) file could take more than a day to transfer electronically. It would be much faster to just fly it across the country. If your file is that urgent (and cost isn't an issue), you might just want to do that. What if there were no flights, and instead you had to drive across the country? Even then, for a really huge file, it would be faster to drive.

### Time Complexity

This is what the concept of asymptotic runtime, or big $O$ time, means. We could describe the data transfer *algorithm* runtime as:
- Electronic Transfer: $O(s)$, where $s$ is the size of the file. This means that the time to transfer the file increases linearly with the size of the file. (Yes, this is a bit of a simplification, but that's okay for these purposes)
- Airplane Transfer: $O(1)$ with respect to the size of the file. As the size of the file increases, it won't take any longer to get the file to your friend. The time is constant.

```{figure} ../Algorithms/images/image17.PNG
---
height: 200px
name: image17
---
No matter how big the constant is and how slow the linear increase is, linear will at some point surpass the constant.
```

There are many more runtimes than this. Some ofthe most common ones are $O(log N),O(N log N), O(N), O(N^2), O(2^N)$. There's no fixed list of possible runtimes, though. You can also have multiple variables in your runtime. For example, the time to paint a fence that's $w$ meters wide and $h$ meters high could be described as $O(wh)$ .If you needed $p$ layers of paint, then you could say that the time is $O(whp)$.

### Big O of DS Algorithms

```{figure} ../Algorithms/images/image15.PNG
---
name: image15
scale: 50%
---
Big O of some of the popular Machine Learning Algorithms
```

