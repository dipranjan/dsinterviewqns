---
description: >-
  This page contains a preliminary discussion into what the different
  mathematical concepts are and how they relate to data science.
---

# Mathematical Motivation

{% hint style="info" %}
The motivation (pun-intended) for having this chapter came when I was studying an [_Introduction to Probability for Data Science_](https://services.publishing.umich.edu/wp-content/themes/mpub-services/library/pdf/PDSdownload100.pdf) by _Stanley H_. _Chan._ A lot of material in this chapter is taken from the book, do check it out.
{% endhint %}

Data Science, Machine Learning is at its core widely dependent on different mathematical concepts which have been developed over centuries. But in this age of easy-to-use packages, frameworks, AutoML solutions we often tend to forget or skip it. In this chapter we would like to quickly glance at some of the broad mathematical topics and how they relate to Data Science. Obviously, it is not in the scope of this book to cover the topics in depth, but the goal here is to leave you with an appreciation of goes behind the algorithms and if needed you can always explore more on your own.

“Data science” has different meanings to different people. If you ask a biologist, data science could mean analyzing DNA sequences. If you ask a banker, data science could mean predicting the stock market. If you ask a software engineer, data science could mean programs and data structures; if you ask a machine learning scientist, data science could mean models and algorithms. However, one thing that is common in all these disciplines is the concept of uncertainty. <mark style="color:yellow;">We choose to learn from data because we believe that the latent information is embedded in the data</mark> — unprocessed, contains noise, and could have missing entries. If there is no randomness, all data scientists can close their business because there is simply no problem to solve. However, the moment we see randomness, our business comes back. <mark style="color:yellow;">Therefore, data science is the subject of making decisions in uncertainty.</mark>

## Infinite Series

Imagine that you have a fair coin. What is the probability that you need to flip the coin three times to get one head?

Since the coin is fair, the probability of obtaining a head is 1/2 . The probability of getting a tail followed by a head is 1/2 × 1/2 = 1/4 . Similarly, the probability of getting two tails and then a head is 1/2 × 1/2 × 1/2 = 1/8 . If you follow this logic, you can write down the probabilities for all other cases. For your convenience, we have drawn the first few in Figure 1.1. As you have probably noticed, the probabilities follow the pattern { 1/2 , 1/4 , 1/8 , . . .}.

<figure><img src=".gitbook/assets/image (4) (1).png" alt=""><figcaption><p>The histogram of flipping a coin until we see a head. The x-axis is the number of coin flips, and the y-axis is the probability.</p></figcaption></figure>

Let us ask something harder: On average, if you want to be 90% sure that you will get a head, what is the minimum number of attempts you need to try? Five attempts? Ten attempts? Indeed, if you try ten attempts, you will very likely accomplish your goal. However, this would seem to be overkill.&#x20;

$$P[success-after-4-attempts] = 1/2 + 1/4 + 1/8 + 1/16 = 0.9375$$. You should be aware that the 93.75% only says that the probability of achieving the goal is high. If you have a bad day, you may still need more than four attempts. Therefore, when we stated the question, we asked for 90% “on average”. Sometimes you may need more attempts and sometimes fewer attempts, but on average, you have a 93.75% chance of succeeding.&#x20;

A geometric series is useful when handling situations such as N − 1 failures followed by a success. However, we can easily twist the problem by asking: What is the probability of getting one head out of 3 independent coin tosses?&#x20;

In general, the number of combinations can be systematically studied using combinatorics. However, the number of combinations motivates us to discuss another background technique known as the binomial series. The binomial series is instrumental in algebra when handling polynomials such as $$(a + b)^2 or (1 + x)^3$$.

The binomial theorem makes the most sense when we also learn about the Pascal’s identity. But we will not cover it in detail here.

## Approximation

Consider a function, $$f(x) = log(1 + x)$$ , for  $$x >0$$ as shown below. This is a nonlinear function, and we all know that nonlinear functions are not fun to deal with. For example, if you want to integrate the function $$\int_a^b x log(1 + x) \,dx$$, then the logarithm will force you to do integration by parts. However, in many practical problems, you may not need the full range of $$x >0$$ . Suppose that you are only interested in values $$x <<1$$  Then the logarithm can be approximated, and thus the integral can also be approximated.

<figure><img src=".gitbook/assets/image (6) (1).png" alt=""><figcaption></figcaption></figure>

<mark style="color:yellow;">Given a function it is often useful to analyze its behavior by approximating using its local information. Taylor approximation (or Taylor series) is one of the tools for such a task.</mark> It is a geometry-based approximation. It approximates the function according to the offset, slope, curvature, and so on. The Taylor series has an infinite number of terms. If we use a finite number of terms, we obtain the nth-order Taylor approximation:

<figure><img src=".gitbook/assets/image (5).png" alt=""><figcaption></figcaption></figure>

_What order of approximation is good?_ It depends on where you want the approximation to be good, and how far you want the approximation to go. The difference between first-order and second-order approximations is shown below:

<figure><img src=".gitbook/assets/image (2) (1) (1).png" alt=""><figcaption></figcaption></figure>

## Calculus

How can the fundamental theorem of calculus ever be useful when studying probability? Two concepts: probability density function and cumulative distribution function and these two functions are related to each other by the fundamental theorem of calculus.

## Linear Algebra

This is one of the most important pillars on which the domain rests.&#x20;

* It provides a way to vectorize and represent the data:

<figure><img src=".gitbook/assets/image (3) (1).png" alt=""><figcaption><p>Suppose we have a crime dataset and we want to figure out which factors influence the crime rate of a city. One way to do it is to put the numbers in matrices and vectors, as shown above. With this vector expression of the data, the analysis questions can roughly be translated to finding β’s in the last equation.</p></figcaption></figure>

* How can you calculate how different your prediction is from the expected output? Loss Functions, of course. A loss function is an application of the **Vector Norm** in Linear Algebra. The norm of a vector can simply be its magnitude.
* Regularization is a very important concept in data science. It’s a technique we use to prevent models from overfitting. _Regularization is actually another application of the Norm._
* Bivariate analysis is an important step in **data exploration**. We want to study the relationship between pairs of variables. Covariance or Correlation are measures used to study relationships between **two continuous variables**.
* One of the most common classification algorithms that regularly produces impressive results. It is an application of the concept of **Vector Spaces** in Linear Algebra.
* Principal Component Analysis, or PCA, is an unsupervised dimensionality reduction technique. PCA finds the **directions of maximum variance** and projects the data along them to reduce the dimensions. Without going into the math, these directions are the [**eigenvectors**](https://www.youtube.com/watch?v=PFDu9oVAE-g) **of the covariance matrix** of the data.
* Machine learning algorithms cannot work with raw textual data. We need to convert the text into some numerical and statistical features to create model inputs. Word Embeddings is a way of representing words as **low dimensional vectors** of numbers while preserving their context in the document.
* Latent Semantic Analysis (LSA), or Latent Semantic Indexing, is one of the techniques of Topic Modeling. It is another application of **Singular Value Decomposition**.
* In Computer Vision the image is represented as a 3d Tensor

By going through this list of a few applications of Linear Algebra you must have guessed the importance of Linear Algebra. As I rightly read somewhere, if Machine Learning is Batman then Linear Algebra is Robin.

## Combinatorics

Combinatorics concerns the number of configurations that can be obtained from certain discrete experiments. It is useful because it provides a systematic way of enumerating cases. Combinatorics often becomes very challenging as the complexity of the event grows.

To motivate the discussion of combinatorics, let us start with the following problem. Suppose there are 50 people in a room. What is the probability that at least one pair of people have the same birthday (month and day)? (We exclude Feb. 29 in this problem.)

The first thing you might be thinking is that since there are 365 days, we need at least 366 people to ensure that one pair has the same birthday. Therefore, the chance that 2 of 50 people have the same birthday is low. This seems reasonable, but let’s do a simulated experiment. In Figure 1.16 we plot the probability as a function of the number of people. For a room containing 50 people, the probability is 97%. To get a 50% probability, we just need 23 people! How is this possible?

<figure><img src=".gitbook/assets/image (6).png" alt=""><figcaption><p>The probability for two people in a group to have the same birthday as a function of the number of people in the group.</p></figcaption></figure>

<figure><img src=".gitbook/assets/image (1) (1) (1) (1) (1) (1) (1) (1) (1).png" alt=""><figcaption><p>The probability for two people to have the same birthday as a function of the number of people in the group. When there is only one person, this person can land on any of the 365 days. When there are two people, the first person has already taken one day (out of 365 days), so the second person can only choose 364 days. When there are three people, the first two people have occupied two days, so there are only 363 days left. If we generalize this process, we see that the number of configurations is 365 × 364 × · · · × (365 − k + 1), where k is the number of people in the room.</p></figcaption></figure>

So imagine that you keep going down the list to the 50th person. The probability that none of these 50 people will have the same birthday is as little as 3%. If you take the complement, you can show that with 97% probability, there is at least one pair of people having the same birthday.

Why is the probability so high with only 50 people while it seems that we need 366 people to ensure two identical birthdays? The difference is the notion of <mark style="color:yellow;">probabilistic</mark> and <mark style="color:yellow;">deterministic</mark>. The 366-people argument is deterministic. If you have 366 people, you are certain that two people will have the same birthday. This has no conflict with the probabilistic argument because the probabilistic argument says that with 50 people, we have a 97% chance of getting two identical birthdays. With a 97% success rate, you still have a 3% chance of failing. It is unlikely to happen, but it can still happen. The more people you put into the room, the stronger guarantee you will have. However, even if you have 364 people and the probability is almost 100%, there is still no guarantee. So there is no conflict between the two arguments since they are answering two different questions.

Permutations and combinations are two ways to enumerate all the possible cases. While the <mark style="color:yellow;">conclusions are probabilistic</mark>, as the birthday paradox shows, <mark style="color:yellow;">permutation and combination are deterministic</mark>. We do not need to worry about the distribution of the samples, and we are not taking averages of anything. Thus, modern data analysis seldom uses the concepts of permutation and combination.&#x20;

Does it mean that combinatorics is not useful? Not quite, because it still provides us with powerful tools for theoretical analysis. For example, in binomial random variables, we need the concept of combination to calculate the repeated cases. The Poisson random variable can be regarded as a limiting case of the binomial random variable, and so combination is also used. <mark style="color:yellow;">Therefore, while we do not use the concepts of permutation per se, we use them to define random variables</mark>.

## Conclusion

In conclusion we would like to highlight the significance of the birthday paradox. Many of us come from an engineering background in which we were told to ensure reliability and guarantee success. We want to ensure that the product we deliver to our customers can survive even in the worst-case scenario. We tend to apply deterministic arguments such as requiring 366 people to ensure complete coverage of the 365 days. In modern data analysis, the worst-case scenario may not always be relevant because of the complexity of the problem and the cost of such a warranty. The probabilistic argument, or the average argument, is more reasonable and cost-effective, as you can see from our analysis of the birthday problem. <mark style="color:yellow;">The heart of the problem is the trade-off between how much confidence you need versus how much effort you need to expend.</mark> Suppose an event is unlikely to happen, but if it happens, it will be a disaster. In that case, you might prefer to be very conservative to ensure that such a disaster event has a low chance of happening. Industries related to risk management such as insurance and investment banking are all operating under this principle.

