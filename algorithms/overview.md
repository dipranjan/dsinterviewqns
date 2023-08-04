# Overview

As said in the very popular [The Hundred Page Machine Learning Book](https://themlbook.com/) each learning algorithm usually consists of three parts:

1. a loss function
2. an optimization criterion based on the loss function (a cost function, for example)
3. an optimization routine that leverages training data to find a solution to the optimization criterion.&#x20;

These are the building blocks of any learning algorithm. Some algorithms were designed to explicitly optimize a specific criterion (both linear and logistic regressions, SVM). Some others, including decision tree learning and kNN, optimize the criterion implicitly. Decision tree learning and kNN are among the oldest machine learning algorithms and were invented experimentally based on intuition, without a specific global optimization criterion in mind, and (like it often happens in scientific history) the optimization criteria were developed later to explain why those algorithms work.

A common overview of different algorithms is given below:

<figure><img src="../_build/html/_images/image261.PNG" alt=""><figcaption><p>Overview of Different Algorithms (<a href="https://learn.microsoft.com/en-us/azure/machine-learning/algorithm-cheat-sheet">Source</a>) (<a href="https://scikit-learn.org/stable/tutorial/machine_learning_map/">Source</a>)</p></figcaption></figure>
