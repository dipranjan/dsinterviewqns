## Regression

```{admonition} Problem: Regression Coefficient
:class: tip, dropdown

**Asked By - UPSTART**

Suppose we have two variables, X and Y, where Y = X + some normal white noise.

1. What will our coefficient be of we run a regression of Y on X?

2. What happens if we run a regression of X on Y?
```

```{admonition} Solution:
:class: dropdown

Let's start with $Y = X$, then the regression line is a perfect fit. The points of such a dataset is $(1,1),(2,2),(3,3),(4,4),(5,5)$

Adding some normal white noise to these points $(1,1),(2,3),(3,5),(4,5),(5,5)$. A regression line fit on these points will move up. Hence the coefficients of $Y = mX+c$, $m$ will increase, $c$ might still stay at $0$ or at max increase.

This movement will go in the negative direction if we predict $X$ based on $Y$

```