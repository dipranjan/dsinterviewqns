---
html_meta:
  "description lang=en": "Interview resource of Data Science Interview focusing on Generative vs Discriminative Models."
  "keywords": "interview, data science, machine learning, Generative, Discriminative"
  "property=og:locale": "en_US"
---

## Generative vs Discriminative Models

Machine learning models can be classified into two types of models – Discriminative and Generative models. In simple words, a discriminative model makes predictions on the unseen data based on conditional probability and can be used either for classification or regression problem statements. On the contrary, a generative model focuses on the distribution of a dataset to return a probability for a given example.

```{figure} ../Algorithms/images/image7.PNG
---
name: image7
scale: 60%
---
This essentially summarizes Generative vs Discriminative Models [📖Source](https://dataisutopia.com/blog/discremenet-generative-models/)
```

### Discriminative Models

Discriminative models separate classes instead of modeling the conditional probability and don’t make any assumptions about the data points. But these models are not capable of generating new data points. Therefore, the ultimate objective of discriminative models is to separate one class from another.

In case of outliers present in the dataset, then discriminative models work better compared to generative models i.e, discriminative models are more robust to outliers. However, there is one major drawback of these models is the misclassification problem, i.e., wrongly classifying a data point.

Some examples are:
‌
- Scalar Vector Machine(SVMs)
- Conditional Random Fields (CRFs)
- Decision Trees and Random Forest
- Logistic regression
- Traditional Neural Networks
- Nearest Neighbor


### Generative Models

Generative models focus on the distribution of individual classes in a dataset and the learning algorithms tend to model the underlying patterns or distribution of the data points. These models use the concept of joint probability and create the instances where a given feature ($x$) or input and the desired output or label ($y$) exist at the same time.

These models use probability estimates and likelihood to model data points and differentiate between different class labels present in a dataset. Unlike discriminative models, these models are also capable of generating new data points.

However, they also have a major drawback – If there is a presence of outliers in the dataset, then it affects these types of models to a significant extent.

Some examples are:
- Naïve Bayes
- Bayesian networks
- Markov random fields
‌- Hidden Markov Models (HMMs)
- Latent Dirichlet Allocation (LDA)
- Generative Adversarial Networks (GANs)
- Autoregressive Model

### Questions

```{admonition} Problem: Mathematical Intuition
:class: tip, dropdown

Can you describe the distinction between Generative and Discriminative Models from the probability standpoint?

```

```{admonition} Solution:
:class: dropdown

In mathematical terms, a discriminative machine learning trains a model which is done by learning parameters that maximize the conditional probability $P(Y|X)$, while on the other hand, a generative model learns parameters by maximizing the joint probability of $P(X,Y)$.
```

```{admonition} Problem: [AMAZON] Difference between Generative and Discriminative Models
:class: tip, dropdown

Describe both generative and discriminative models and give an example of each?

```

```{admonition} Solution:
:class: dropdown

In simple words, a discriminative model makes predictions on the unseen data based on conditional probability and can be used either for classification or regression problem statements. On the contrary, a generative model focuses on the distribution of a dataset to return a probability for a given example.

Linear Discriminant Analysis (LDA) is a generative model, whereas Logistic Regression is a discriminative model.
```