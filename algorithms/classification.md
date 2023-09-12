# Classification

## Logistic Regression

It is easy to say that the linear regression predicts a “value” of the targeted variable through a linear combination of the given features, while on the other hand, a Logistic regression predicts “probability value” through a linear combination of the given features plugged inside a logistic function. Linear regression is unbounded, and this brings logistic regression into picture. Their value strictly ranges from 0 to 1.

<figure><img src="../_build/html/_images/image3.PNG" alt=""><figcaption><p>Logistic regression uses Sigmoid function to transform linear regression into the logit function. Logit is nothing but log of Odds. Then using log of Odds it calculates the required probability. (<a href="https://www.vebuso.com/2020/02/linear-to-logistic-regression-explained-step-by-step/">Source</a>)</p></figcaption></figure>

### Cost Function

One more thing to note here is that logistic regression uses maximum likelihood estimation (MLE) instead of least squares method of minimizing the error which is used in linear models. In Linear regression we minimized SSE. In Logistic Regression we maximize log likelihood instead. Linear regression uses mean squared error as its cost function. If this is used for logistic regression, then it will be a non-convex function of parameters (theta). Gradient descent will converge into global minimum only if the function is convex.

<figure><img src="../_build/html/_images/image4.PNG" alt=""><figcaption><p>Cost function (<a href="https://pvgisours.tistory.com/59">Source</a>)</p></figcaption></figure>

## Metrics

<figure><img src="../_build/html/_images/image5.PNG" alt=""><figcaption><p>Confusion Matrix and key Metrics</p></figcaption></figure>

<figure><img src="../_build/html/_images/image6.PNG" alt=""><figcaption><p>(a) ROC curve (b) Precision-Recall curve. Both are a helpful diagnostic tool for evaluating a single classifier but challenging for comparing classifiers. Like ROC AUC, we can calculate the area under the curve as a score and use that score to compare classifiers. The focus on the minority class makes the Precision-Recall AUC more useful for imbalanced classification problems. (<a href="https://machinelearningmastery.com/tour-of-evaluation-metrics-for-imbalanced-classification/">Source</a>)</p></figcaption></figure>

In classification problems, various evaluation metrics are used to assess the performance of a machine learning model. The choice of metric depends on the specific characteristics of your problem and your priorities, such as the relative importance of false positives and false negatives. Here's an explanation of common classification metrics and when to use them, along with examples:

1. **Accuracy**:
   * **Use Case**: Suitable for balanced datasets where false positives and false negatives have similar consequences.
   * **Example**: In a spam email classifier, where both false positives (legitimate emails marked as spam) and false negatives (spam emails in the inbox) are undesirable.
2. **Precision**:
   * **Use Case**: When minimizing false positives is crucial, and you want to ensure that the positive predictions made by your model are highly accurate.
   * **Example**: Medical diagnoses like cancer detection, where false positives can lead to unnecessary treatments and stress.
3. **Recall (Sensitivity or True Positive Rate)**:
   * **Use Case**: When minimizing false negatives is critical, and you want to ensure that your model captures as many positive instances as possible.
   * **Example**: An airport security system for detecting prohibited items, where missing a threat (false negative) is far more serious than a false alarm.
4. **F1 Score**:
   * **Use Case**: Balances precision and recall, suitable when you want a single metric that considers both false positives and false negatives.
   * **Example**: Information retrieval systems, where you need to find relevant documents (recall) while minimizing the number of irrelevant ones (precision).
5. **Specificity (True Negative Rate)**:
   * **Use Case**: Relevant in scenarios where minimizing false positives is essential, like fraud detection.
   * **Example**: Credit card fraud detection, where it's important to correctly identify non-fraudulent transactions (true negatives) to prevent blocking legitimate transactions.
6. **ROC AUC (Receiver Operating Characteristic Area Under the Curve)**:
   * **Use Case**: Useful when comparing different models or assessing the overall performance of a classifier across different thresholds.
   * **Example**: Evaluating the performance of various machine learning algorithms in a credit scoring task.
7. **Matthews Correlation Coefficient (MCC)**:
   * **Use Case**: Appropriate for imbalanced datasets, where there is a significant difference in class frequencies.
   * **Example**: Anomaly detection in network security, where normal events far outnumber anomalous ones.
8. **F-beta Score**:
   * **Use Case**: Allows you to adjust the balance between precision and recall using the parameter beta.
   * **Example**: When you want to prioritize either precision (beta < 1) or recall (beta > 1) depending on the specific needs of your application.

Remember that the choice of metric should be based on the specific goals and trade-offs of your problem. It's often a good practice to consider multiple metrics, especially when the consequences of false positives and false negatives differ significantly in your application.

It seems like there might be a typo in your question. I assume you are referring to the **Naive Bayes algorithm**. Naive Bayes is a classification algorithm, not "naive bias." Let me provide a detailed explanation of the Naive Bayes algorithm.

### **Naive Bayes Algorithm**

Naive Bayes is a probabilistic machine learning algorithm used for classification tasks, such as spam email detection, sentiment analysis, and text categorization. It is based on Bayes' theorem, which calculates the probability of an event based on prior knowledge of conditions related to that event.

The Naive Bayes algorithm makes a simplifying assumption known as the "naive" assumption, which is that all features used in the classification are conditionally independent of each other given the class label. This means that the presence or absence of one feature does not affect the presence or absence of another feature.

**3. Model Representation:** In Naive Bayes, the goal is to calculate the probability of a particular class (C) given a set of features (X₁, X₂, ..., Xᵢ). This is represented as:

```
P(C | X₁, X₂, ..., Xᵢ) = P(C) * P(X₁ | C) * P(X₂ | C) * ... * P(Xᵢ | C)
```

Where:

* P(C | X₁, X₂, ..., Xᵢ) is the posterior probability of class C given the features X₁ through Xᵢ.
* P(C) is the prior probability of class C.
* P(Xᵢ | C) is the conditional probability of feature Xᵢ given class C.

&#x20;**Training:** To train a Naive Bayes classifier, you need labeled training data where you know both the features and the corresponding class labels. The training process involves:

a. Calculating Prior Probabilities (P(C)):

* Calculate the prior probability of each class, i.e., the probability that an example belongs to that class based on the training data.

b. Estimating Conditional Probabilities (P(Xᵢ | C)):

* For each feature Xᵢ and each class C, estimate the conditional probability that the feature Xᵢ occurs given the class C. This is typically done using techniques like Maximum Likelihood Estimation (MLE) or Laplace smoothing (to handle zero probabilities).

&#x20;**Types of Naive Bayes:** There are different variants of Naive Bayes classifiers, including:

* **Gaussian Naive Bayes**: Assumes that continuous features follow a Gaussian distribution.
* **Multinomial Naive Bayes**: Used for discrete data like text data, where features represent word counts or frequencies.
* **Bernoulli Naive Bayes**: Suitable for binary data, where features are binary variables.

**Advantages:**

* Naive Bayes is simple, computationally efficient, and scales well to high-dimensional data.
* It works well with small to moderate-sized datasets.
* It is particularly effective for text classification tasks like spam detection and sentiment analysis.

&#x20;**Limitations:**

* The "naive" assumption of feature independence may not hold in some real-world scenarios.
* It can perform poorly when features are highly correlated.
* Handling of continuous and numerical data may require additional preprocessing.

Despite its simplifying assumptions, Naive Bayes is a powerful and often surprisingly effective algorithm, especially for text classification tasks and situations where feature independence is a reasonable approximation.

## Questions

<details>

<summary>[ROBINHOOD] Interpret Coefficients</summary>

How would you interpret coefficients of logistic regression for categorical and boolean variables?

**Answer**

**Reference:** [Explanation](https://www.displayr.com/how-to-interpret-logistic-regression-coefficients/)

Let's explain this using an example. The table below shows the main outputs from the logistic regression. It is very obvious which are the categorial variables out here: ![](../contents/Algorithms/images/image1.png)

The first category (usually not shown) has a coefficient of $$0$$. So, if we can say, for example, that:

* The effect of having a DSL service versus having no DSL service $$(0.92 - 0 = 0.92)$$ is a little more than twice as big in terms of leading to churn as is the effect of being a senior citizen $$(0.41)$$.
* The effect of having a Fiber optic service is approximately twice as big as having a DSL service.
* If somebody has a One-year contract and a DSL service, these two effects almost completely cancel each other out.

Consider the scenario of a senior citizen with a $$2$$ month tenure, with no internet service, a one-year contract and a monthly charge of $100. If we compute all the effects and add them up we have:

$$0.41$$ (Senior Citizen = Yes) $$- 0.06 (2*-0.03$$; tenure) $$+ 0$$ (no internet service) $$- 0.88$$ (one year contract) $$+ 0 (100*0$$; monthly charge) $$= -0.53$$.

We then need to add the (Intercept), also sometimes called the constant, which gives us $$-0.53- 1.41 = -1.94$$. To make the next bit a little more transparent, I am going to substitute $$-1.94$$ with $$x$$. The logistic transformation is:

Probability $$= \frac{1} {1 + \exp^{-x}} = \frac{1}{1 + \exp^{1.94}} = 0.13 = 13\%$$.

Thus, the senior citizen with a $$2$$ month tenure, no internet service, a one-year contract, and a monthly charge of \$$$100$$, is predicted as having a $$13%$$ chance of cancelling their subscription. By contrast if we redo this, just changing one thing, which is substituting the effect for no internet service $$(0)$$ with that for a fiber optic connection $$(1.86)$$, we compute that they have a $$48%$$ chance of cancelling.

</details>

<details>

<summary>Multinomial Logistic Regression</summary>

Can Logistic Regression be used for multi class classification?

**Answer**

Logistic regression, by default, is limited to two-class classification problems. Some extensions like one-vs-rest can allow logistic regression to be used for multi-class classification problems, although they require that the classification problem first be transformed into multiple binary classification problems.

Multinomial logistic regression algorithm is an extension to the logistic regression model that involves changing the loss function to cross-entropy loss and predict probability distribution to a multinomial probability distribution to natively support multi-class classification problems.

</details>

<details>

<summary>Choice of Cost Function</summary>

In what situations would you recommend using one metric over the another for classification models?

**Answer**

It all depends on the use case. For example, a diagnostic lab will be concerned with incorrect positive diagnosis. Hence, they will aim for a high specificity value. On the other hand, for a model predicting loan default rate the goal is to identify even a small chance of default, hence we need the model to maximize sensitivity.

</details>

<details>

<summary>[INTUIT] Logistic Regression vs Decision Tree</summary>

What's the difference between decision tree and logistic regression?

**Answer**

Decision trees and logistic regression are both machine learning algorithms used for classification tasks, but they have different approaches and characteristics. Here are the key differences between decision trees and logistic regression:

**1. Algorithm Type:**

* **Decision Tree**: Decision trees are non-linear models that use a tree-like structure to make decisions by recursively splitting the data into subsets based on the most informative features.
* **Logistic Regression**: Logistic regression is a linear model that estimates the probability of a binary outcome by fitting a linear equation to the input features.

**2. Model Complexity:**

* **Decision Tree**: Decision trees can capture complex relationships in the data and can fit highly non-linear decision boundaries.
* **Logistic Regression**: Logistic regression assumes a linear relationship between the input features and the log-odds of the output, making it less flexible for modeling complex, non-linear relationships.

**3. Interpretability:**

* **Decision Tree**: Decision trees are highly interpretable. You can easily visualize the tree structure and understand how decisions are made at each node.
* **Logistic Regression**: Logistic regression provides interpretable coefficients for each feature, indicating the direction and magnitude of their influence on the outcome.

**4. Handling of Numeric vs. Categorical Features:**

* **Decision Tree**: Decision trees can handle both numeric and categorical features without requiring one-hot encoding.
* **Logistic Regression**: Logistic regression typically requires one-hot encoding of categorical features to be included in the model.

**5. Overfitting:**

* **Decision Tree**: Decision trees are prone to overfitting, especially if they are deep and complex. Pruning or limiting the depth of the tree can help mitigate overfitting.
* **Logistic Regression**: Logistic regression is less prone to overfitting, especially when the number of features is limited relative to the number of training samples.

**6. Probability Output:**

* **Decision Tree**: Decision trees can provide class probabilities by counting the proportion of samples in each leaf node belonging to a particular class. However, this can lead to uneven class probability estimates.
* **Logistic Regression**: Logistic regression provides well-calibrated class probabilities, making it suitable for tasks where probability estimates are essential.

**7. Handling Imbalanced Data:**

* **Decision Tree**: Decision trees can struggle with imbalanced datasets, as they tend to favor the majority class in splits.
* **Logistic Regression**: Logistic regression can handle imbalanced datasets better by adjusting the decision threshold or using class weights.

**8. Performance on Linear Problems:**

* **Decision Tree**: Decision trees are not well-suited for linear problems where the decision boundary is best represented by a straight line.
* **Logistic Regression**: Logistic regression is appropriate for linear problems and can capture linear relationships effectively.

In practice, the choice between decision trees and logistic regression depends on the specific characteristics of your data and the problem you are trying to solve. Decision trees are more suitable for non-linear and interpretable problems, while logistic regression is a good choice for problems where linear relationships are predominant and well-calibrated probability estimates are required.

</details>
