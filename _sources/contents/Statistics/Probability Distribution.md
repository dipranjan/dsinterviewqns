# Probability Distribution

### Random Variable

Random Variable maps the outcome of sample space into real numbers.

Example: How many heads when we toss 3 coins?

$X$ could be $0, 1, 2$ or $3$ randomly.
And they might each have a different probability.

$X$ = "The number of Heads" is the Random Variable.
In this case, there could be 0 Heads (if all the coins land Tails up), 1 Head, 2 Heads or 3 Heads.
So the Sample Space = ${0, 1, 2, 3}$
But this time the outcomes are NOT all equally likely. 
The three coins can land in eight possible ways:

Looking at the table we see just 1 case of Three Heads, but 3 cases of Two Heads, 3 cases of One Head, and 1 case of Zero Heads. So:
- $P(X = 3) = 1/8 = {HHH}$
- $P(X = 2) = 3/8 = {HHT,HTH,THH}$
- $P(X = 1) = 3/8 = {TTH,THT,TTH}$
- $P(X = 0) = 1/8 = {TTT}$

And this is what becomes the **probability distribution.**

```{figure} ../Statistics/images/image2.PNG
---
height: 250px
name: image2
---
Probability Distribution vs Frequency Distribution
```

**Frequency distribution** comes from actually doing the experiment $n$ number of times as $n --> \infty$ the shape comes closer and closer to the Probability distribution

Now the probability distribution can be of 2 types, discrete and continous. An example of Discrete is shown above. When we use a probability function to describe a discrete probability distribution we call it a **probability mass function (pmf)**. The probability mass function, $f$, just returns the probability of the outcome. Therefore the probability of rolling a $3$ is $f(3) = 1/6$.

When we use a probability function to describe a continuous probability distribution we call it a **probability density function (pdf)**.


### Unbiased Estimator

An unbiased estimator is an accurate statistic that’s used to approximate a population parameter. “Accurate” in this sense means that it’s neither an overestimate nor an underestimate. If an overestimate or underestimate does happen, the mean of the difference is called a “bias.” That’s just saying if the estimator (i.e. the sample mean) equals the parameter (i.e. the population mean), then it’s an unbiased estimator.

```{admonition} Problem:
:class: tip

**Asked By - LIME**

What is an unbiased estimator and can you provide an example for a layman to understand?

```

```{admonition} Solution:
:class: dropdown

One famous example of an unrepresentative sample is the literary digest voter survey, which predicted Alfred Landon would win the 1936 presidential election. The survey was biased, as it failed to include a representative sample of low income voters who were more likely to be democrat and vote for Theodore Roosevelt.

If the sampling had been done correctly then the estimator would have been unbiased as it would match with the actual output from the population, which was win for Theodore Roosevelt.
```


### Maximum Likelihood Estimation (MLE)


:::{note}
**Reference:** [Discussion](https://stats.stackexchange.com/questions/112451/maximum-likelihood-estimation-mle-in-layman-terms), [Explanation](https://www.kdnuggets.com/2019/11/probability-learning-maximum-likelihood.html), [Implementation](https://analyticsindiamag.com/maximum-likelihood-estimation-python-guide/)
:::

Say you have some data. Say you're willing to assume that the data comes from some distribution -- perhaps Gaussian. There are an infinite number of different Gaussians that the data could have come from (which correspond to the combination of the infinite number of means and variances that a Gaussian distribution can have). MLE will pick the Gaussian (i.e., the mean and variance) that is "most consistent" with your data (the precise meaning of consistent is explained below).

So, say you've got a data set of $y={−1,3,7}$. The most consistent Gaussian from which that data could have come has a mean of $3$ and a variance of $16$. It could have been sampled from some other Gaussian. But one with a mean of $3$ and variance of $16$ is most consistent with the data in the following sense: the probability of getting the particular $y$ values you observed is greater with this choice of mean and variance, than it is with any other choice.

Maximum Likelihood Estimation can be applied to both regression and classification problems.

```{admonition} Problem:
:class: tip

**Asked By - SPOTIFY**

Suppose you draw n samples from a uniform distribution U(a, b). What is the MLE estimate of a and b?

```

```{admonition} Solution:
:class: dropdown

Solution Pending

```