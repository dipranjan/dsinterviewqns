---
html_meta:
  "description lang=en": "Interview resource of Data Science Interview focusing on Hyperparameter optimization."
  "keywords": "interview, data science, machine learning, Hyperparameter, optimization, tuning"
  "property=og:locale": "en_US"
---

## Hyperparameter Optimization

```{warning}
This page is a work in progress
```

While building a machine learning model, many design choices need to be made as in how to define the model architecture. For example what should be the depth of my Decision Tree, how many trees should be present in my Random Forest, how many layers should be there in my Meural network, so on and so forth.

In most cases the optimal model architecture is not obvious or readily available to us. **This exploration to select the optimal model architecture automatically from a defined range of options is referred to as hyperparameter optimization or tuning.**

### What's a Hyperparameter?

[📚 Source](https://cloud.google.com/ai-platform/training/docs/hyperparameter-tuning-overview)

Hyperparameters contain the data that govern the training process itself.

Your training application handles **three categories of data** as it trains your model:

- Your **input data (also called training data)**, however, the values in your input data never directly become part of your model.

- Your **model's parameters** are the variables that your chosen machine learning technique uses to adjust to your data. For example, a deep neural network (DNN) is composed of processing nodes (neurons), each with an operation performed on data as it travels through the network. When your DNN is trained, each node has a weight value that tells your model how much impact it has on the final prediction. Those weights are an example of your model's parameters. In many ways, your model's parameters are the model—they are what distinguishes your particular model from other models of the same type working on similar data.

- Your **hyperparameters** are the variables that govern the training process itself. For example, part of setting up a deep neural network is deciding how many hidden layers of nodes to use between the input layer and the output layer, and how many nodes each layer should use. These variables are not directly related to the training data. They are configuration variables. Note that parameters change during a training job, while hyperparameters are usually constant during a job.

---

### Tuning

The process of Hyperparameter Tuning usually involves the following steps:

- Decide on the hyperparameters that is applicable for the model
- Provide a range or set of values for all the hyperparameters
- Run the training process on the set of parameter combinations to find the best hyperparameter which optimizes your model performance

Now this last step can be an extremely time and resource intensive process depending upon the model and range of the hyperparameters provided. There are many ways to perfrom the last step. Let's start with an example, suppose 

#### Grid Search

#### Randomized Search

#### Halving Grid Search

#### Bayesian Optimization

#### Evolutionary Optimization

#### Population-based training

