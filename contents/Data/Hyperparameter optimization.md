---
html_meta:
  "description lang=en": "Interview resource of Data Science Interview focusing on Hyperparameter optimization."
  "keywords": "interview, data science, machine learning, Hyperparameter, optimization, tuning"
  "property=og:locale": "en_US"
---

## Hyperparameter Optimization

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

Now this last step can be an extremely time and resource intensive process depending upon the model and range of the hyperparameters provided. There are many ways to perfrom the last step. Let's start with an example, suppose you are trying to optimize a XGBoost model and this is the **parameter space**:

- 'max_depth': [3,6,10],
- 'learning_rate': [0.01, 0.05, 0.1],
- 'n_estimators': [100, 500, 1000]

#### Grid Search

Grid search will search all 27 combinations and find out the combination which gives the best possible value for the parameter of your choice. But the caveat being it takes huge amount of time and resources to perform grid search.

#### Randomized Search

Same as Grid search, just that instead of searching the entire parameter space you randomly sample a subset of it, say you sample 10 of the 27 possible combinations. Random search might not give the best possible combination but in most cases it gives reasonably good result.

#### Halving Grid Search

[📚 Source](https://scikit-learn.org/stable/modules/grid_search.html#successive-halving-user-guide)

Successive halving (SH) is like a tournament among candidate parameter combinations. SH is an iterative selection process where all candidates (the parameter combinations) are evaluated with a small amount of resources at the first iteration. Only some of these candidates are selected for the next iteration, which will be allocated more resources. For parameter tuning, the resource is typically the number of training samples, but it can also be an arbitrary numeric parameter such as `n_estimators` in a random forest.

#### Bayesian Optimization

[📚 Additional Material](http://neupy.com/2016/12/17/hyperparameter_optimization_for_neural_networks.html#bayesian-optimization)

Bayesian optimization (BO) is a global optimization method for noisy black-box functions. Applied to hyperparameter optimization, BO builds a probabilistic model of the function mapping from hyperparameter values to the objective evaluated on a validation set. By iteratively evaluating a promising hyperparameter configuration based on the current model, and then updating it, BO aims to gather observations revealing as much information as possible about this function and, in particular, the location of the optimum. It tries to balance exploration (hyperparameters for which the outcome is most uncertain) and exploitation (hyperparameters expected close to the optimum). In practice, BO has been shown to obtain better results in fewer evaluations compared to grid search and random search, due to the ability to reason about the quality of experiments before they are run.

In plain English, BO evaluates hyperparameters that appear more promising from past results, and finds better settings, rather than using random search with fewer iterations. The performance of the past hyperparameter affects future decisions.

#### Evolutionary Optimization

Evolutionary hyperparameter optimization follows a process inspired by the biological concept of evolution:

- Create an initial population of random solutions (i.e., randomly generate tuples of hyperparameters, typically 100+)
- Evaluate the hyperparameters tuples and acquire their fitness function (e.g., 10-fold cross-validation accuracy of the machine learning algorithm with those hyperparameters)
- Rank the hyperparameter tuples by their relative fitness
- Replace the worst-performing hyperparameter tuples with new hyperparameter tuples generated through crossover and mutation
- Repeat steps 2-4 until satisfactory algorithm performance is reached or algorithm performance is no longer improving

#### Population-based training

Population Based Training (PBT) learns both hyperparameter values and network weights. Multiple learning processes operate independently, using different hyperparameters. As with evolutionary methods, poorly performing models are iteratively replaced with models that adopt modified hyperparameter values and weights based on the better performers. This replacement model warm starting is the primary differentiator between PBT and other evolutionary methods. PBT thus allows the hyperparameters to evolve and eliminates the need for manual hypertuning. The process makes no assumptions regarding model architecture, loss functions or training procedures.

PBT and its variants are adaptive methods: they update hyperparameters during the training of the models. On the contrary, non-adaptive methods have the sub-optimal strategy to assign a constant set of hyperparameters for the whole training.


### Open Source Tools

[📚 Source](hhttps://neptune.ai/blog/best-tools-for-model-tuning-and-hyperparameter-optimization)

#### Ray Tune

Ray provides a simple, universal API for building distributed applications. Tune is a Python library for experiment execution and hyperparameter tuning at any scale. Tune is one of the many packages of Ray. Ray Tune is a Python library that speeds up hyperparameter tuning by leveraging cutting-edge optimization algorithm such as Ax/Botorch, HyperOpt, and Bayesian Optimization at scale.

#### Optuna

Optuna is designed specially for machine learning. It’s a black-box optimizer, so it needs an objective function. This objective function decides where to sample in upcoming trials, and returns numerical values (the performance of the hyperparameters). It uses different algorithms, such as GridSearch, Random Search, Bayesian and Evolutionary algorithms to find the optimal hyperparameter values.

#### HyperOpt

Hyperopt is a Python library for serial and parallel optimization over awkward search spaces, which may include real-valued, discrete, and conditional dimensions. It uses Bayesian optimization algorithms for hyperparameter tuning, to choose the best parameters for a given model. It can optimize a large-scale model with hundreds of hyperparameters. HyperOpt requires 4 essential components for the optimization of hyperparameters: the search space, the loss function, the optimization algorithm, a database for storing the history (score, configuration).

#### Scikit-Optimize

Scikit-Optimize is an open-source library for hyperparameter optimization in Python. It was developed by the team behind Scikit-learn. It’s relatively easy to use compared to other hyperparameter optimization libraries. It has sequential model-based optimization libraries known as Bayesian Hyperparameter Optimization (BHO). The advantage of BHO is that they find better model settings than random search in fewer iterations.