# Bias/Variance Tradeoff

## Bias

* Error between average model prediction and ground truth
* The bias of the estimated function tells us the capacity of the underlying model to predict the values

$$bias = \mathbb{E}[f'(x)] - f(x)$$

## Variance

* Average variability in the model prediction for the given dataset
* The variance of the estimated function tells you how much the function can adjust to the change in the dataset

$$variance = \mathbb{E}[(f'(x) - \mathbb{E}[f'(x)])^2]$$

**High Bias:**

* Overly simplified Model
* Under-fitting
* High error on both test and train data

**High Variance:**

* Overly complex Model
* Over-fitting
* Low error on train data and high on test
* Starts modelling the noise in the input

<figure><img src="../.gitbook/assets/image24.png" alt=""><figcaption><p><a href="https://stanford.edu/~shervine/teaching/cs-229/cheatsheet-machine-learning-tips-and-tricks">📖Source</a></p></figcaption></figure>

**Bias variance Trade-off**

* Increasing bias (not always) reduces variance and vice-versa
* The best model is where the error is reduced.
* Compromise between bias and variance while choosing the best model
