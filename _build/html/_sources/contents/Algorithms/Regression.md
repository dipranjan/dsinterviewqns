## Regression

### Linear Regression

$Y = b_0 + b_1 * x_1 + b_2 * x_2 + \epsilon$

The idea is to find the line or plane which best fits the data. Collectively, $b_0, b_1, b_2$ are called regression coefficients. $\epsilon$ is the error term, the part of $Y$ the regression model is unable to explain.

```{figure} ../Algorithms/images/image2.PNG
---
name: image2
---
[📖Source](https://www.shutterstock.com/image-illustration/annotated-diagram-explaining-components-graph-showing-1406041139) 
```

#### Metrics

Now once you have the model fit next comes the metrics to measure how good the fit is, some of the common metrics are as follows:

- **$RSS$** (Residual sum of squares) $= (Y_{actual} - Y_{predicted})^2$, it changes with scale change
- **$TSS$** (Total sum of squares) $= (Y_{actual} - Y_{avg})^2$
- **$R^2$** $= 1-\frac{RSS}{TSS} $, more the better, increases with more coefficients
- **$RSE$** (Residual Standard Error) $ = \sqrt{\frac{RSS}{d.o.f}}$, here $d.o.f = n-2$

#### Feature selection

- Hypothesis testing and using p-values to understand if the feature is important or not
- Using metrics like Adjusted $R^2$, AIC, BIC, etc. which takes into consideration the number of features used to build the model and penalizes accordingly



#### Assumptions

- The relationship between $X$ and $Y$ is **linear**. Because we are fitting a linear model, we assume that the relationship really is linear, and that the errors, or residuals, are simply random fluctuations around the true line.
- The error terms are **normally distributed**. This can be checked with a Q-Q plot
- Error terms are independent of each other. This can be checked with a ACF plot. This can be used while checking independence while using a time-series data
- Error terms are **homoscedastic**, i.e. they have constant variance. Residulas Vs Fitted graph should be flat. This means that the variability in the response is changing as the predicted value increases. This is a problem, in part, because the observations with larger errors will have more pull or influence on the fitted model.
- The independent variables are not multicollinear. **Multicollinearity** is when a variable can be explained as a combination of other variables. This can be checked by using VIF(Variance inflation factor) $= \frac{1}{1-R_i^2}$.
	- A VIF score of $>10$ indicates there there is a problem
	- If a multicollinear variable is present the coefficients swing wildly thereby affecting the interpretability of the model. P-vales are not reliable. But it doesnot affect prediction or the goodness of fit statistics.
	- To deal with multicollinearity
		- drop variables
		- create new features from existing ones
		- PCA/PLS



### Questions

```{admonition} Problem: Regression Coefficient
:class: tip, dropdown

**Asked By - UPSTART**

Suppose we have two variables, $X$ and $Y$, where $Y = X +$ some normal white noise.

1. What will our coefficient be of we run a regression of $Y$ on $X$?

2. What happens if we run a regression of $X$ on $Y$?
```

```{admonition} Solution:
:class: dropdown

Let's start with $Y = X$, then the regression line is a perfect fit. The points of such a dataset is $(1,1),(2,2),(3,3),(4,4),(5,5)$

Adding some normal white noise to these points $(1,1),(2,3),(3,5),(4,5),(5,5)$. A regression line fit on these points will move up. Hence the coefficients of $Y = mX+c$, $m$ will increase, $c$ might still stay at $0$ or at max increase.

This movement will go in the negative direction if we predict $X$ based on $Y$

```

```{admonition} Problem: Linear Regression in Time Series
:class: tip, dropdown

Do you think Linear Regression should be used in Time series analysis?
```

```{admonition} Solution:
:class: dropdown

Linear Regression as per me can be used in Time Series but might not always give good results. 2 reasons which come up are:

- Linear Regression is good for intrapolation but not for extrapolation so the results can vary wildly
- When Linear Regression is used but observations are correlated (as in time series data) you will have a biased estimate of the variance
- Moreover, time-series data have a pattern, such as during peak hours, festive seasons, etc., which would most likely be treated as outliers in the linear regression analysis

```