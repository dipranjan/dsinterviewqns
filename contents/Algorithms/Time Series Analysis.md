---
html_meta:
  "description lang=en": "Interview resource of Data Science Interview focusing on Time Series Analysis."
  "keywords": "interview, data science, machine learning, Time Series, ARIMA, SARIMA, ARIMAX, Prophet"
  "property=og:locale": "en_US"
---

## Time Series Analysis

**Reference:** [📖Explanation](https://nbviewer.jupyter.org/github/Yorko/mlcourse_open/blob/master/jupyter_english/topic09_time_series/topic9_part1_time_series_python.ipynb)

```{figure} ../Algorithms/images/image14.PNG
---
name: image14
scale: 70%
---
```

A time series is simply a series of data points ordered in time. In a time series, time is often the independent variable and the goal is usually to make a forecast for the future.

- **Moving Average:** Here the assumption is that future value of our variable depends on the average of its $k$ previous values. Moving average has another use case - smoothing the original time series to identify trends. The wider the window, the smoother the trend. In the case of very noisy data, which is often encountered in finance, this procedure can help detect common patterns. This can also be used to determine anamolies based on the confidence level.

- **Weighted average:** It is a simple modification to the moving average. The weights sum up to `1` with larger weights assigned to more recent observations.
$\hat{y}_{t} = \displaystyle\sum^{k}_{n=1} \omega_n y_{t+1-n}$

- **Exponential smoothing:** Here instead of weighting the last $k$ values of the time series, we start weighting all available observations while exponentially decreasing the weights as we move further back in time.
$\hat{y}_{t} = \alpha \cdot y_t + (1-\alpha) \cdot \hat y_{t-1} $

	The $\alpha$ weight is called a smoothing factor. It defines how quickly we will "forget" the last available true observation. The smaller $\alpha$ is, the more influence the previous observations have and the smoother the series is.

- **Double Exponential smoothing:** Up to now, the methods that we've discussed have been for a single future point prediction (with some nice smoothing). That is cool, but it is also not enough. Let's extend exponential smoothing so that we can predict two future points (of course, we will also include more smoothing).

	Series decomposition will help us -- we obtain two components: intercept (i.e. level) $\ell$ and slope (i.e. trend) $b$. We have learnt to predict intercept (or expected series value) with our previous methods; now, we will apply the same exponential smoothing to the trend by assuming that the future direction of the time series changes depends on the previous weighted changes. As a result, we get the following set of functions:

	$$\ell_x = \alpha y_x + (1-\alpha)(\ell_{x-1} + b_{x-1})$$

	$$b_x = \beta(\ell_x - \ell_{x-1}) + (1-\beta)b_{x-1}$$

	$$\hat{y}_{x+1} = \ell_x + b_x$$

	The first one describes the intercept, which, as before, depends on the current value of the series. The second term is now split into previous values of the level and of the trend. The second function describes the trend, which depends on the level changes at the current step and on the previous value of the trend. In this case, the $\beta$ coefficient is a weight for exponential smoothing. The final prediction is the sum of the model values of the intercept and trend.

- **Triple exponential smoothing a.k.a. Holt-Winters:**

	The idea is to add a third component - seasonality. This means that we should not use this method if our time series is not expected to have seasonality. Seasonal components in the model will explain repeated variations around intercept and trend, and it will be specified by the length of the season, in other words by the period after which the variations repeat. For each observation in the season, there is a separate component; for example, if the length of the season is 7 days (a weekly seasonality), we will have 7 seasonal components, one for each day of the week.

	The new system of equations:

	$$\ell_x = \alpha(y_x - s_{x-L}) + (1-\alpha)(\ell_{x-1} + b_{x-1})$$

	$$b_x = \beta(\ell_x - \ell_{x-1}) + (1-\beta)b_{x-1}$$

	$$s_x = \gamma(y_x - \ell_x) + (1-\gamma)s_{x-L}$$

	$$\hat{y}_{x+m} = \ell_x + mb_x + s_{x-L+1+(m-1)modL}$$

	The intercept now depends on the current value of the series minus any corresponding seasonal component. Trend remains unchanged, and the seasonal component depends on the current value of the series minus the intercept and on the previous value of the component. Take into account that the component is smoothed through all the available seasons; for example, if we have a Monday component, then it will only be averaged with other Mondays. You can read more on how averaging works and how the initial approximation of the trend and seasonal components is done [here](http://www.itl.nist.gov/div898/handbook/pmc/section4/pmc435.htm). Now that we have the seasonal component, we can predict not just one or two steps ahead but an arbitrary $m$ future steps ahead, which is very encouraging.

	Below is the code for a triple exponential smoothing model, which is also known by the last names of its creators, Charles Holt and his student Peter Winters. Additionally, the Brutlag method was included in the model to produce confidence intervals:

	$$\hat y_{max_x}=\ell_{x−1}+b_{x−1}+s_{x−T}+m⋅d_{t−T}$$

	$$\hat y_{min_x}=\ell_{x−1}+b_{x−1}+s_{x−T}-m⋅d_{t−T}$$

	$$d_t=\gamma∣y_t−\hat y_t∣+(1−\gamma)d_{t−T},$$

	where $T$ is the length of the season, $d$ is the predicted deviation. Other parameters were taken from triple exponential smoothing. You can read more about the method and its applicability to anomaly detection in time series [here](http://fedcsis.org/proceedings/2012/pliks/118.pdf).

	Exponentiality is hidden in the recursiveness of the function – we multiply by $(1-\alpha)$ each time, which already contains a multiplication by $(1-\alpha)$ of previous model values.


#### Stationarity

Before we start modeling, we should mention such an important property of time series, **stationarity**.

So why is stationarity so important? Because it is easy to make predictions on a stationary series since we can assume that the future statistical properties will not be different from those currently observed. Most of the time-series models, in one way or the other, try to predict those properties (mean or variance, for example). Furture predictions would be wrong if the original series were not stationary.

When running a linear regression the assumption is that all of the observations are all independent of each other. In a time series, however, we know that observations are time dependent. It turns out that a lot of nice results that hold for independent random variables (law of large numbers and central limit theorem to name a couple) hold for stationary random variables. So by making the data stationary, we can actually apply regression techniques to this time dependent variable.

**Dickey-Fuller test** can be used as a check for stationarity. If ‘Test Statistic’ is greater than the ‘Critical Value’ then the time series is stationary.

There are a few ways to deal with non-stationarity:

- Deflation by CPI
- Logarithmic
- First Difference
- Seasonal Difference
- Seasonal Adjustment

Plot the ACF and PACF charts and find the optimal parameters.


#### ARIMA family


We will explain this model by building up letter by letter. $SARIMA(p, d, q)(P, D, Q, s)$, Seasonal Autoregression Moving Average model:

- $AR(p)$ - autoregression model i.e. regression of the time series onto itself. The basic assumption is that the current series values depend on its previous values with some lag (or several lags). The maximum lag in the model is referred to as $p$. To determine the initial $p$, you need to look at the PACF plot and find the biggest significant lag after which **most** other lags become insignificant.
- $MA(q)$ - moving average model. Without going into too much detail, this models the error of the time series, again with the assumption that the current error depends on the previous with some lag, which is referred to as $q$. The initial value can be found on the ACF plot with the same logic as before. 

Let's combine our first 4 letters:

$AR(p) + MA(q) = ARMA(p, q)$

What we have here is the Autoregressive–moving-average model! If the series is stationary, it can be approximated with these 4 letters. Let's continue.

- $I(d)$ - order of integration. This is simply the number of nonseasonal differences needed to make the series stationary.

Adding this letter to the four gives us the $ARIMA$ model which can handle non-stationary data with the help of nonseasonal differences. Great, one more letter to go!

- $S(s)$ - this is responsible for seasonality and equals the season period length of the series

With this, we have three parameters: $(P, D, Q)$

- $P$ - order of autoregression for the seasonal component of the model, which can be derived from PACF. But you need to look at the number of significant lags, which are the multiples of the season period length. For example, if the period equals 24 and we see the 24-th and 48-th lags are significant in the PACF, that means the initial $P$ should be 2.

- $Q$ - similar logic using the ACF plot instead.

- $D$ - order of seasonal integration. This can be equal to 1 or 0, depending on whether seasonal differeces were applied or not.


#### Prophet

[📖 Check out this discussion](https://stats.stackexchange.com/questions/472266/inference-in-time-series-prophet-vs-arima)

ARIMA and similar models assume some sort of causal relationship between past values and past errors and future values of the time series. Facebook Prophet doesn't look for any such causal relationships between past and future. Instead, it simply tries to find the best curve to fit to the data, using a linear or logistic curve, and Fourier coefficients for the seasonal components. There is also a regression component, but that is for external regressors, not for the time series itself (The Prophet model is a special case of GAM - Generalized Additive Model).


#### Metrics

- **R squared:** coefficient of determination (in econometrics, this can be interpreted as the percentage of variance explained by the model), $(-\infty, 1]$

$R^2 = 1 - \frac{SS_{res}}{SS_{tot}}$ 

- **Mean Absolute Error:** this is an interpretable metric because it has the same unit of measurment as the initial series, $[0, +\infty)$

$MAE = \frac{\sum\limits_{i=1}^{n} |y_i - \hat{y}_i|}{n}$ 

- **Median Absolute Error:** again, an interpretable metric that is particularly interesting because it is robust to outliers, $[0, +\infty)$

$MedAE = median(|y_1 - \hat{y}_1|, ... , |y_n - \hat{y}_n|)$

- **Mean Squared Error:** the most commonly used metric that gives a higher penalty to large errors and vice versa, $[0, +\infty)$

$MSE = \frac{1}{n}\sum\limits_{i=1}^{n} (y_i - \hat{y}_i)^2$

- **Mean Squared Logarithmic Error:** practically, this is the same as MSE, but we take the logarithm of the series. As a result, we give more weight to small mistakes as well. This is usually used when the data has exponential trends, $[0, +\infty)$

$MSLE = \frac{1}{n}\sum\limits_{i=1}^{n} (log(1+y_i) - log(1+\hat{y}_i))^2$

- **Mean Absolute Percentage Error:** this is the same as MAE but is computed as a percentage, which is very convenient when you want to explain the quality of the model to management, $[0, +\infty)$

$MAPE = \frac{100}{n}\sum\limits_{i=1}^{n} \frac{|y_i - \hat{y}_i|}{y_i}$ 

---

#### Questions

```{admonition} Problem: Cross Validation with Time Series
:class: tip, dropdown

Can cross validation be used with Time Series to estimate model parameters automatically?

```

```{admonition} Solution:
:class: dropdown

Normal cross-validation cannot be used for time series because one cannot randomly mix values in a fold while preserving this structure. With randomization, all time dependencies between observations will be lost. But something like "cross-validation on a rolling basis" can be used.

The idea is rather simple -- we train our model on a small segment of the time series from the beginning until some $t$, make predictions for the next $t+n$ steps, and calculate an error. Then, we expand our training sample to $t+n$ value, make predictions from $t+n$ until $t+2*n$, and continue moving our test segment of the time series until we hit the last available observation. As a result, we have as many folds as $n$ will fit between the initial training sample and the last observation.
```

```{admonition} Problem: CNNs in Time Series
:class: tip, dropdown

How are CNNs used for Time Series Prediction?
```

```{admonition} Solution:
:class: dropdown

- The ability of CNNs to learn and automatically extract features from raw input data can be applied to time series forecasting problems. A sequence of observations can be treated like a one-dimensional image that a CNN model can read and distill into the most salient elements.
- The capability of CNNs has been demonstrated to great effect on time series classification tasks such as automatically detecting human activities based on raw accelerator sensor data from fitness devices and smartphones.
- CNNs have the support for multivariate input, multivariate output, it can learn arbitrary but complex functional relationships, but does not require that the model learn directly from lag observations. Instead, the model can learn a representation from a large input sequence that is most relevant for the prediction problem.
```

```{admonition} Problem: Data Prep for Time Series
:class: tip, dropdown

What are some of Data Preprocessing Operations you would use for Time Series Data?  
```

```{admonition} Solution:
:class: dropdown
It depends on the problem, but some common ones are:
- Parsing time series information from various sources and formats.
- Generating sequences of fixed-frequency dates and time spans.
- Manipulating and converting date times with time zone information.
- Resampling or converting a time series to a particular frequency.
- Performing date and time arithmetic with absolute or relative time increments.
```

```{admonition} Problem: Missing Value in Time Series
:class: tip, dropdown

What are some of best ways to handle missing values in Time Series Data?  
```

```{admonition} Solution:
:class: dropdown

The most common methodology used for handling missing, unequally spaced, or unsynchronized values is *linear interpolation*. 

The idea is to create estimated values at the desired time stamps. These can be used to generate multivariate time series that are synchronized, equally spaced, and have no missing values.
Consider the scenario where $y_i$ and  $y_j$ are values for the time series at times $t_i$ and  $t_j$, repectively, where $i < j$. Let $t$ be a time drawn from the interval $(t_i, t_j)$. Then, the interpolated value of the series is given by: 
$y = y_i + \frac{t-t_i}{t_j-t_i}*(y_j-y_i)$
```

```{admonition} Problem: Stationarity
:class: tip, dropdown

Can you explain why time series has to be stationary? 
```

```{admonition} Solution:
:class: dropdown

Stationarity is important because, in its absence, a model describing the data will vary in accuracy at different time points. As such, stationarity is required for sample statistics such as means, variances, and correlations to accurately describe the data at all time points of interest.

Looking at the time series plots below, you can notice how the mean and variance of any given segment of time would do a good job representing the whole stationary time series but a relatively poor job representing the whole non-stationary time series. For instance, the mean of the non-stationary time series is much lower from $600<t<800$ and its variance is much higher in this range than in the range from $200<t<400$.

![Stationary vs Non-Stationary](../Algorithms/images/image20.PNG)

What quantities are we typically interested in when we perform statistical analysis on a time series? We want to know
- Its expected value,
- Its variance, and
- The correlation between values $s$ periods apart for a set of values.

To calculate these thingswe use a mean across many time periods. The mean across many time periods is only informative if the expected value is the same across those time periods. If these population parameters can vary, what are we really estimating by taking an average across time?

(Weak) stationarity requires that these population quantities must be the same across time, making the sample average a reasonable way to estimate them.
```

```{admonition} Problem: IQR in Time Series
:class: tip, dropdown

How is Interquartile range used in Time series? 
```

```{admonition} Solution:
:class: dropdown

It is mostly used to detect outliers in Time Series data.
```

```{admonition} Problem: Irregular Data 
:class: tip, dropdown

What does irregularly-spaced spatial data mean in Time series?
```

```{admonition} Solution:
:class: dropdown
- A lot of techniques assume that data is sampled at regularly-spaced intervals of time. This interval between adjacent samples is called the *sampling period*.
- A lot of data is not or cannot be sampled with a fixed sampling period. For example, if we measure the atmosphere using sensors, the terrain may not allow us to place weather stations exactly 50 miles apart.

There are many different ways to deal with this kind of data which does not have a fixed sampling period. One approach is to interpolate the data onto a grid and then use a technique intended for gridded data.
```

```{admonition} Problem: Sliding Window 
:class: tip, dropdown

Explain the Sliding Window method in Time series?
```

```{admonition} Solution:
:class: dropdown
- Time series can be phrased as supervised learning. Given a sequence of numbers for a time series dataset, we can restructure the data to look like a supervised learning problem.
- In the sliding window method, the previous time steps can be used as input variables, and the next time steps can be used as the output variable. 

In statistics and time series analysis, this is called a lag or lag method. The number of previous time steps is called the window width or size of the lag. This sliding window is the basis for how we can turn any time series dataset into a supervised learning problem.
```

```{admonition} Problem: LSTM vs MLP 
:class: tip, dropdown
Can you discuss on the usage of LSTM vs MLP in Time Series?
```

```{admonition} Solution:
:class: dropdown

Multilayer Perceptrons, or MLPs for short, can be applied to time series forecasting. A challenge with using MLPs for time series forecasting is in the preparation of the data. Specifically, lag observations must be flattened into feature vectors. My understanding is that LSTMs captures the relations between time steps, whereas simple MLPs treat each time step as a separated feature (doesn't take succession into consideration).

RNNs are known to be superior to MLP in case of sequential data. But complex models like LSTM and GRU require a lot of data to achieve their potential.
```

```{admonition} Problem: Sequential vs Non-Sequential
:class: tip, dropdown
Can a CNN (or other non-sequential deep learning models) outperform LSTM (or other sequential models) in time series data 
```

```{admonition} Solution:
:class: dropdown
*(Source)[https://ai.stackexchange.com/questions/16818/can-non-sequential-deep-learning-models-outperform-sequential-models-in-time-ser]*
You are right CNN based models can outperform RNN. You can take a look at this [paper](https://arxiv.org/pdf/1803.01271.pdf) where they compared different RNN models with TCN (temporal convolutional networks) on different sequence modeling tasks. Even though there are no big differences in terms of results there are some nice properties that CNN based models offers such as: parallelism, stable gradients and low training memory footprint. In addition to CNN based models there are also attention based models (you might want to take a look at the [transformer](https://papers.nips.cc/paper/7181-attention-is-all-you-need.pdf))
```

