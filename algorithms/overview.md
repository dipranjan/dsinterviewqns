---
description: This page discusses the building blocks of an algorithm.
---

# Overview

As said in the very popular [The Hundred Page Machine Learning Book](https://themlbook.com/) each learning algorithm usually consists of three parts:

1. a loss function
2. an optimization criterion based on the loss function (a cost function, for example)
3. an [optimization routine](overview.md#optimizers) that leverages training data to find a solution to the optimization criterion.&#x20;

These are the building blocks of any learning algorithm. Some algorithms were designed to explicitly optimize a specific criterion (both linear and logistic regressions, SVM). Some others, including decision tree learning and kNN, optimize the criterion implicitly. Decision tree learning and kNN are among the oldest machine learning algorithms and were invented experimentally based on intuition, without a specific global optimization criterion in mind, and (like it often happens in scientific history) the optimization criteria were developed later to explain why those algorithms work.

A common overview of different algorithms is given below:

<figure><img src="../_build/html/_images/image261.PNG" alt=""><figcaption><p>Overview of Different Algorithms (<a href="https://learn.microsoft.com/en-us/azure/machine-learning/algorithm-cheat-sheet">Source</a>) (<a href="https://scikit-learn.org/stable/tutorial/machine_learning_map/">Source</a>)</p></figcaption></figure>

### Optimizers

Optimizers are algorithms used in data science and machine learning to adjust the parameters of a model during training to minimize the error or loss function. Each optimizer has its own way of updating these parameters, and they come with their own advantages and disadvantages.&#x20;

<figure><img src="../.gitbook/assets/image.png" alt=""><figcaption></figcaption></figure>

Here are some common optimizers explained in simple terms with their pros and cons:

1. **Gradient Descent**:
   * **How it works**: Gradient Descent computes the gradient (slope) of the loss function and takes small steps in the direction that reduces the loss.
   * **Pros**: Simple, widely used, and works well in many cases.
   * **Cons**: Can be slow to converge to the optimal solution, especially in high-dimensional spaces.
2. **Stochastic Gradient Descent (SGD)**:
   * **How it works**: Similar to Gradient Descent but updates parameters using a random subset (mini-batch) of the training data.
   * **Pros**: Faster convergence, works well with large datasets, and helps escape local minima.
   * **Cons**: Noisy updates can lead to oscillations, and it may require tuning of the learning rate.
3.  **Mini-Batch Gradient Descent**:

    * **How it works**: A compromise between Gradient Descent and SGD, where updates are made using small batches of data.
    * **Pros**: Faster than Gradient Descent, less noisy than SGD, and suitable for a wide range of problems.
    * **Cons**: Still requires tuning of the learning rate, and convergence depends on the batch size.

    <mark style="color:blue;">In the case of Stochastic Gradient Descent, we update the parameters after every single observation and we know that every time the weights are updated it is known as an iteration. In the case of Mini-batch Gradient Descent, we take a subset of data and update the parameters based on every subset.</mark>
4. **Adam (Adaptive Moment Estimation)**:
   * **How it works**: Combines ideas from RMSprop and Momentum methods by adapting the learning rates for each parameter based on past gradients.
   * **Pros**: Fast convergence, works well with noisy data, and requires less hyperparameter tuning.
   * **Cons**: Might not perform as well on all problem types and could converge to suboptimal solutions in some cases.
5. **RMSprop (Root Mean Square Propagation)**:
   * **How it works**: Adjusts the learning rate for each parameter based on the magnitude of recent gradients.
   * **Pros**: Effective in handling non-stationary or noisy environments, requires less tuning compared to traditional SGD.
   * **Cons**: Not suitable for all problem types and may converge to local minima.
6. **Adagrad (Adaptive Gradient Algorithm)**:
   * **How it works**: Adapts the learning rate for each parameter based on the historical gradient information.
   * **Pros**: Automatically adapts learning rates, which can be beneficial for sparse data.
   * **Cons**: Learning rates can become too small over time, causing slow convergence and potentially overshooting the optimal solution.
7. **Nadam**:
   * **How it works**: A combination of Nesterov Accelerated Gradient (NAG) and Adam optimizers, which combines their advantages.
   * **Pros**: Fast convergence, good for complex models, and less sensitive to the choice of hyperparameters.
   * **Cons**: Computationally more expensive than some other optimizers.

The choice of optimizer depends on the specific problem you are solving, the dataset size, and the architecture of your neural network. It's common to experiment with different optimizers and hyperparameters to find the one that works best for your particular task.
