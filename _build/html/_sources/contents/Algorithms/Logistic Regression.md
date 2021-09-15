## Logistic Regression


```{admonition} Problem:
:class: tip, dropdown

**Asked By - ROBINHOOD**

How would you interpret coefficients of logistic regression for categorical and boolean variables?

```

```{admonition} Solution:
:class: dropdown

**Reference:** [Explanation](https://www.displayr.com/how-to-interpret-logistic-regression-coefficients/)

Let's explain this using an example. The table below shows the main outputs from the logistic regression. It is very obvious which are the categorial variables out here:

![Estimate of Coefficients](../Algorithms/images/image1.PNG)

The first category (usually not shown) has a coefficient of $0$. So, if we can say, for example, that:

- The effect of having a DSL service versus having no DSL service $(0.92 - 0 = 0.92)$ is a little more than twice as big in terms of leading to churn as is the effect of being a senior citizen $(0.41)$.
- The effect of having a Fiber optic service is approximately twice as big as having a DSL service.
- If somebody has a One year contract and a DSL service, these two effects almost completely cancel each other out.

Consider the scenario of a senior citizen with a $2$ month tenure, with no internet service, a one year contract and a monthly charge of $$100$. If we compute all the effects and add them up we have:

$0.41$ (Senior Citizen = Yes) $- 0.06 (2*-0.03$; tenure) $+ 0$ (no internet service) $- 0.88$ (one year contract) $+ 0 (100*0$; monthly charge) $= -0.53$.

We then need to add the (Intercept), also sometimes called the constant, which gives us $-0.53- 1.41 = -1.94$. To make the next bit a little more transparent, I am going to substitute $-1.94$ with $x$. The logistic transformation is:

Probability $= \frac{1} {1 + \exp^{-x}} = \frac{1}{1 + \exp^{1.94}} = 0.13 = 13\%$.

Thus, the senior citizen with a $2$ month tenure, no internet service, a one year contract, and a monthly charge of $$100$, is predicted as having a $13\%$ chance of cancelling their subscription. By contrast if we redo this, just changing one thing, which is substituting the effect for no internet service $(0)$ with that for a fiber optic connection $(1.86)$, we compute that they have a $48\%$ chance of cancelling.

```