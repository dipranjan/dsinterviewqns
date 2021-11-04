---
html_meta:
  "description lang=en": "Interview resource of Data Science Interview focusing on Regression."
  "keywords": "interview, data science, machine learning, Regression, Linear Regression"
  "property=og:locale": "en_US"
---


## Regression

### Linear Regression

```{figure} ../Algorithms/images/image8.PNG
---
name: image2
scale: 60%
---
[📖Source](https://xkcd.com/605/) 
```

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

[📖Explanation](https://towardsdatascience.com/log-book-practical-guide-to-linear-polynomial-regression-in-r-e0ed2e7f8031)

- Hypothesis testing and using p-values to understand if the feature is important or not
- Using metrics like $\text{Adjusted} R^2$, $AIC$, $BIC$, etc. which takes into consideration the number of features used to build the model and penalizes accordingly
- How do we find the model that minimizes a metric like $AIC$? One approach is to search through all possible models, called all **subset regression**. This is computationally expensive and is not feasible for problems with large data and many variables. An attractive alternative is to use **stepwise regression** about which we learned above, this successively adds and drops predictors to find a model that lowers $AIC$. Simpler yet are **forward selection** and **backward selection**. In forward selection, you start with no predictors and add them one-by-one, at each step adding the predictor that has the largest contribution to , stopping when the contribution is no longer statistically significant. In backward selection, or backward elimination, you start with the full model and take away predictors that are not statistically significant until you are left with a model in which all predictors are statistically significant.
- **Penalized Regression** or **Regularization**:

	[📖Explanation](https://www.analyticsvidhya.com/blog/2016/01/ridge-lasso-regression-python-complete-tutorial/)

	Penalized regression is similar in spirit to AIC. Instead of explicitly searching through a discrete set of models, the model-fitting equation incorporates a constraint that penalizes the model for too many variables (parameters). Rather than eliminating predictor variables entirely — as with stepwise, forward, and backward selection — penalized regression applies the penalty by reducing coefficients, in some cases to near zero. Common penalized regression methods are ridge regression and lasso regression.
	Regularization is nothing but adding a penalty term to the objective function and control the model complexity using that penalty term. It can be used for many machine learning algorithms. Both Ridge and Lasso regression uses $L2$ and $L1$ regularizations.
	- **Ridge Regression (L2)**: $\text{RSS} + \lambda (\sum_{j=1}^p b_j^2)$, the value of hyperparameter $\lambda$ can be found using cross-validation
	- **Lasso Regression (L1)**: $\text{RSS} + \lambda (\sum_{j=1}^p \lVert b_j\rVert)$, the value of hyperparameter $\lambda$ can be found using cross-validation

```{note}
Ridge brings the coefficients close to $0$ but not exactly to $0$ which results in the model retaining all the features. Lasso on the other hand brings the coefficients to $0$ hence results in reduced features. Lasso shrinks the coefficients by same amount whereas Ridge shrinks them by same proportion.

Elastic Net is another useful techniques which combines both L1 and L2 regularization.
```

#### Assumptions

- The relationship between $X$ and $Y$ is **linear**. Because we are fitting a linear model, we assume that the relationship really is linear, and that the errors, or residuals, are simply random fluctuations around the true line.
- The error terms are **normally distributed**. This can be checked with a Q-Q plot
- Error terms are independent of each other. This can be checked with a ACF plot. This can be used while checking independence while using a time-series data
- Error terms are **homoscedastic**, i.e. they have constant variance. Residulas Vs Fitted graph should be flat. This means that the variability in the response is changing as the predicted value increases. This is a problem, in part, because the observations with larger errors will have more pull or influence on the fitted model.
- The independent variables are not multicollinear. **Multicollinearity** is when a variable can be explained as a combination of other variables. This can be checked by using **VIF(Variance inflation factor)** $= \frac{1}{1-R_i^2}$.
	- A VIF score of $>10$ indicates there there is a problem
	- If a multicollinear variable is present the coefficients swing wildly thereby affecting the interpretability of the model. P-vales are not reliable. But it doesnot affect prediction or the goodness of fit statistics.
	- To deal with multicollinearity
		- drop variables
		- create new features from existing ones
		- PCA/PLS

```{note}
One very important point to remember is that Generalized Linear Regression is called so because $Y$ is linear w.r.t its coefficients $b_0, b_1, b_2$, etc. it is irrespective of whether the features $x_1, x_2$, etc. are linear or not. Meaning $x_1$ can actually be $x_1^2$ and it won't matter.
```

### Non-Linear Regression

In some cases, the true relationship between the outcome and a predictor variable might not be linear.
There are different solutions extending the linear regression model for capturing these nonlinear effects, some of these are covered below.

#### Polynomial Regression

The equation of polynomial becomes something like this.

$Y = b_0 + b_1 * x_1 + b_2 * x_1^2 + b_n * x_1^n $ and so on...

The degree of order which to use is a Hyperparameter, and we need to choose it wisely. But using a high degree of polynomial tries to overfit the data and for smaller values of degree, the model tries to underfit so we need to find the optimum value of a degree. **Polynomial Regression on datasets with high variability chances to result in over-fitting.**

#### Regression Splines
[📖Explanation](https://www.analyticsvidhya.com/blog/2018/03/introduction-regression-splines-python-codes/)
In order to overcome the disadvantages of polynomial regression, we can use an improved regression technique which, instead of building one model for the entire dataset, divides the dataset into multiple bins and fits each bin with a separate model. Such a technique is known as Regression spline.

In polynomial regression, we generated new features by using various polynomial functions on the existing features which imposed a global structure on the dataset. To overcome this, we can divide the distribution of the data into separate portions and fit linear or low degree polynomial functions on each of these portions. The points where the division occurs are called **Knots**. Functions which we can use for modelling each piece/bin are known as Piecewise functions. There are various piecewise functions that we can use to fit these individual bins.

#### Generalized additive models

It does the same thing as above but just removes the need to specifying the knots. It fits spline models with automated selection of knots.




### Questions

```{admonition} Problem: [UPSTART] Regression Coefficient
:class: tip, dropdown

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