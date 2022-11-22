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

<figure><img src="../_build/html/_images/image241.PNG" alt=""><figcaption><p><a href="https://stanford.edu/~shervine/teaching/cs-229/cheatsheet-machine-learning-tips-and-tricks">📖Source</a></p></figcaption></figure>

**Bias variance Trade-off**

* Increasing bias (not always) reduces variance and vice-versa
* The best model is where the error is reduced.
* Compromise between bias and variance while choosing the best model

## Questions

<details>

<summary>High Bias</summary>

How can you identify a High Bias model? How can you fix it?

**Answer**

A **High Bias** model is due to a simple model and can be easily identified when you see:

1. High training error
2. Validation error or test error is the same as training error

To **fix** a High Bias model, you can:

1. Add more input features
2. Add more complexity by introducing polynomial features
3. Decrease the regularization term

</details>

<details>

<summary>Data Bias</summary>

Can you name a few types of data biases?

**Answer** [(Source)](https://www.telusinternational.com/articles/7-types-of-data-bias-in-machine-learning)

Though not exhaustive, this list contains common examples of data bias in the field, along with examples of where it occurs.

**Sample bias:** Sample bias occurs when a dataset does not reflect the realities of the environment in which a model will run. An example of this is certain facial recognition systems trained primarily on images of white men. These models have considerably lower levels of accuracy with women and people of different ethnicities. Another name for this bias is selection bias.

**Exclusion bias:** Exclusion bias is most common at the data preprocessing stage. Most often it's a case of deleting valuable data thought to be unimportant. However, it can also occur due to the systematic exclusion of certain information. For example, imagine you have a dataset of customer sales in America and Canada. 98% of the customers are from America, so you choose to delete the location data thinking it is irrelevant. However, this means you model will not pick up on the fact that your Canadian customers spend two times more.

**Measurement bias:** This type of bias occurs when the data collected for training differs from that collected in the real world, or when faulty measurements result in data distortion. A good example of this bias occurs in image recognition datasets, where the training data is collected with one type of camera, but the production data is collected with a different camera. Measurement bias can also occur due to inconsistent annotation during the data labeling stage of a project.

**Recall bias:** This is a kind of measurement bias, and is common at the data labeling stage of a project. Recall bias arises when you label similar types of data inconsistently. This results in lower accuracy. For example, let's say you have a team labeling images of phones as damaged, partially-damaged, or undamaged. If someone labels one image as damaged, but a similar image as partially damaged, your data will be inconsistent.

**Observer bias:** Also known as confirmation bias, observer bias is the effect of seeing what you expect to see or want to see in data. This can happen when researchers go into a project with subjective thoughts about their study, either conscious or unconscious. We can also see this when labelers let their subjective thoughts control their labeling habits, resulting in inaccurate data.

**Racial bias:** Though not data bias in the traditional sense, this still warrants mentioning due to its prevalence in AI technology of late. Racial bias occurs when data skews in favor of particular demographics. This can be seen in facial recognition and automatic speech recognition technology which fails to recognize people of color as accurately as it does caucasians.

**Association bias:** This bias occurs when the data for a machine learning model reinforces and/or multiplies a cultural bias. Your dataset may have a collection of jobs in which all men are doctors and all women are nurses. This does not mean that women cannot be doctors, and men cannot be nurses. However, as far as your machine learning model is concerned, female doctors and male nurses do not exist. Association bias is best known for creating gender bias.

</details>

<details>

<summary>KNN vs Bias/Variance</summary>

How can you relate the _KNN Algorithm_ to the _Bias-Variance tradeoff_?

**Answer** ([Source](https://teazrq.github.io/stat542/rlab/knn.html))

$$K$$ nearest neighbor is a simple nonparametric method.

Suppose we collect a set of observations $$(\{x_i, y_i\}_{i=1}^n)$$, the prediction at a new target point is $$\widehat y = \frac{1}{k} \sum_{x_i \in N_k(x_0)} y_i$$, where $$(N_k(x_0))$$ defines the $$(k)$$ samples from the training data that are closest to $$(x_0)$$. As default, closeness is defined using distance measures, such as the Euclidean distance.

If we consider different values of $$k$$, we can observe the trade-off between bias and variance.

<img src="../.gitbook/assets/KNN vs bias var.png" alt="" data-size="original">

&#x20;As $$k$$ increases, we have a more stable model, i.e., smaller variance, however, the bias is also increased. As $$k$$ decreases, the bias also decreases, but the model is less stable. Formally, the prediction error (at a given target point $$x_0$$) can be broken into three parts: the irreducible error, the bias squared, and variance.$$[\begin{aligned} E\Big[ \big( Y - \widehat f(x_0) \big)^2 \Big] &= E \Big[ \big( Y - f(x_0) + f(x_0) -  E[\widehat f(x_0)] + E[\widehat f(x_0)] - \widehat f(x_0) \big)^2 \Big] \\ &= E \Big[ \big( Y - f(x_0) \big)^2 \Big] + E \Big[ \big(f(x_0) -  E[\widehat f(x_0)] \big)^2 \Big] + E\Big[ \big(E[\widehat f(x_0)] - \widehat f(x_0) \big)^2 \Big] + \text{Cross Terms}\\ &= \underbrace{E\Big[ ( Y - f(x_0))^2 \big]}_{\text{Irreducible Error}} + \underbrace{\Big(f(x_0) - E[\widehat f(x_0)]\Big)^2}_{\text{Bias}^2} +  \underbrace{E\Big[ \big(\widehat f(x_0) - E[\widehat f(x_0)] \big)^2 \Big]}_{\text{Variance}} \end{aligned}]$$

</details>

