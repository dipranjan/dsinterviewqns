---
html_meta:
  "description lang=en": "Interview resource of Data Science Interview focusing on Decision Tree based models."
  "keywords": "interview, data science, machine learning, Boosting, Bagging, Random Forest, Decision Tree, Classification"
  "property=og:locale": "en_US"
---

## Tree based approaches

```{warning}
This page is a work in progress
```

### Decision Tree

A decision tree is a flowchart-like structure in which each internal node represents a "test" on an attribute (e.g. whether a coin flip comes up heads or tails), each branch represents the outcome of the test, and each leaf node represents a class label (decision taken after computing all attributes). It is immensly popular primarily due to its ease of explanation which is often a critical requirement in business.

Decision Trees follow Sum of Product (SOP) representation. The Sum of product (SOP) is also known as Disjunctive Normal Form. For a class, every branch from the root of the tree to a leaf node having the same class is conjunction (product) of values, different branches ending in that class form a disjunction (sum).

The primary challenge in the decision tree implementation is to identify which attributes do we need to consider as the root node and each level. Handling this is to know as the attributes selection. We have different attributes selection measures to identify the attribute which can be considered as the root note at each level.

The decision of making strategic splits heavily affects a tree’s accuracy. The decision criteria are different for classification and regression trees.

Decision trees use multiple algorithms to decide to split a node into two or more sub-nodes. The creation of sub-nodes increases the homogeneity of resultant sub-nodes. In other words, we can say that the purity of the node increases with respect to the target variable. The decision tree splits the nodes on all available variables and then selects the split which results in most homogeneous sub-nodes.

```{figure} ../Algorithms/images/image11.PNG
---
name: image11
scale: 80%
---
Decision Tree
```

The algorithm selection is also based on the type of target variables. Let us look at some algorithms used in Decision Trees:

- ID3 → (extension of D3)
- C4.5 → (successor of ID3)
- CART → (Classification And Regression Tree)
- CHAID → (Chi-square automatic interaction detection Performs multi-level splits when computing classification trees)
- MARS → (multivariate adaptive regression splines)

The ID3 algorithm builds decision trees using a top-down greedy search approach through the space of possible branches with no backtracking. A greedy algorithm, as the name suggests, always makes the choice that seems to be the best at that moment.

**Steps in the ID3 algorithm:**

- It begins with the original set as the root node.
- On each iteration of the algorithm, it iterates through the unused attributes of the set and calculates a measure of Homogeneity:
	- **Gini Index:** Gini Index uses the probability of finding a data point with one label as an indicator for homogeneity — if the dataset is completely homogeneous, then the probability of finding a datapoint with one of the labels is 1 and the probability of finding a data point with the other label is zero
	- **Information Gain / Entropy-based:** The idea is to use the notion of entropy which is a central concept in information theory. Entropy quantifies the degree of disorder in the data. Entropy is always a positive number between zero and 1. Another interpretation of entropy is in terms of information content. A completely homogeneous dataset has no information content in it (there is nothing non-trivial to be learnt from the dataset) whereas a dataset with a lot of disorder has a lot of latent information waiting to be learnt.
	- For Regression models the split can happen by checking metrics like $R^2$
- It then selects the attribute which has the smallest Entropy or Largest Information gain
- The set is then split by the selected attribute to produce a subset of the data
- The algorithm continues to recur on each subset, considering only attributes never selected before

Decision trees have a strong tendency to overfit the data. So practical uses of the decision tree must necessarily incorporate some ’regularization’ measures to ensure the decision tree built does not become more complex than is necessary and starts to overfit. There are broadly two ways of regularization on decision trees:
- **Truncation:** Truncate the decision tree during the training (growing) process preventing it from degenerating into one with one leaf for every data point in the training dataset. Below criterion are used to decide if the decision tree needs to be grown further:
	- Minimum Size of the Partition for a Split: Stop partitioning further when the current partition is small enough.
	- Minimum Change in Homogeneity Measure: Do not partition further when even the best split causes an insignificant change in the purity measure (difference between the current purity and the purity of the partitions created by the split).
	- Limit on Tree Depth: If the current node is farther away from the root than a threshold, then stop partitioning further.
	- Minimum Size of the Partition at a Leaf: If any of partitions from a split has fewer than this threshold minimum, then do not consider the split. Notice the subtle difference between this condition and the minimum size required for a split.
	- Maxmimum number of leaves in the Tree: If the current number of the bottom-most nodes in the tree exceeds this limit then stop partitioning.
- **Pruning:** Let the tree grow to any complexity. However add a post-processing step in which we prune the tree in a bottom-up fashion starting from the leaves. It is more common to use pruning strategies to avoid overfitting in practical implementations. One popular approach to pruning is to use a validation set. This method called reduced-error pruning, considers every one of the test (non-leaf ) nodes for pruning. Pruning a node means removing the entire subtree below the node, making it a leaf, and assigning the majority class (or the average of the values in case it is regression) among the training data points that pass through that node. A node in the tree is pruned only if the decision tree obtained after the pruning has an accuracy that is no worse on the validation dataset than the tree prior to pruning. This ensures that parts of the tree that were added due to accidental irregularities in the data are removed, as these irregularities are not likely to repeat.

Though there are various ways to truncate or prune trees, the `DecisionTreeClassifier` function in sklearn provides the following hyperparameters which you can control:
- `criterion (Gini/IG or entropy)`: It defines the function to measure the quality of a split. Sklearn supports “gini” criteria for Gini Index & “entropy” for Information Gain. By default, it takes the value “gini”.
- `max_features`: It defines the no. of features to consider when looking for the best split
- `max_depth`: denotes maximum depth of the tree. It can take any integer value or None. If None, then nodes are expanded until all leaves are pure or until all leaves contain less than min_samples_split samples. By default, it takes “None” value.
- `min_samples_split`: This tells above the minimum no. of samples reqd. to split an internal node
- `min_samples_leaf`: The minimum number of samples required to be at a leaf node

---
### Random Forest


---

### Boosting

A horse-racing gambler, hoping to maximize his winnings, decides to create a computer program that will accurately predict the winner of a horse race based on the usual information (number of races recently won by each horse, betting odds for each horse, etc.). To create such a program, he asks a highly successful expert gambler to explain his betting strategy. Not surprisingly, the expert is unable to articulate a grand set of rules for selecting a horse. On the other hand, when presented with the data for a specific set of races, the expert has no trouble coming up with a “rule of thumb” for that set of races (such as, “Bet on the horse that has recently won the most races” or “Bet on the horse with the most favored odds”). 

Although such a rule of thumb, by itself, is obviously very rough and inaccurate, it is not unreasonable to expect it to provide predictions that are at least a little bit better than random guessing. Furthermore, by repeatedly asking the expert’s opinion on different collections of races, the gambler is able to extract many rules of thumb.

In order to use these rules of thumb to maximum advantage, there are two problems faced by the gambler:
- First, how should he choose the collections of races presented to the expert so as to extract rules of thumb from the expert that will be the most useful?
- Second, once he has collected many rules of thumb, how can they be combined into a single, highly accurate prediction rule?

Boosting refers to a general and provably effective method of producing a very accurate prediction rule by combining rough and moderately inaccurate rules of thumb in a manner similar to that suggested above.

---

### AdaBoost
[📖Read](https://towardsdatascience.com/log-book-adaboost-the-math-behind-the-algorithm-a014c8afbbcc)

- AdaBoost starts by assigning equal weight to each datapoint, the idea is to adjust the weights of each observation after every iteration such that the the algorithm is forced to take a harder look at these difficult to classify observations
- Post each iteration we will have a weak learner using which we will calculate 2 things:
	- the updated weights of each $N$ observation for the next iteration
	- the weight that the weak learner itself will have on the final output, in each of the $t$ iterations we will have a learner $h_1$, $h_2$, $h_3$ .. $h_t$ each of which will be combined to make the final model, the weight of each of these individual learners in the final output is given by $\alpha_t$. The models with low error rate will have higher values of $\alpha_t$ and hence higher weight in the final output.
- Before you apply the AdaBoost algorithm, you should specifically remove the Outliers. Since AdaBoost tends to boost up the probabilities of misclassified points and there is a high chance that outliers will be misclassified, it will keep increasing the probability associated with the outliers and make the progress difficult.

```{figure} ../Algorithms/images/image10.PNG
---
name: image10
scale: 80%
---
Adaboost Pseudocode
```

---

### Gradient Boosting

- As always let's start with a crude initial function F₀, something like average of all values in case of regression. It will give us some output, however bad.
- Calculate the loss function
- Next, we should have fit a new model on the residuals given by the Loss function, but there is a subtle twist: we will instead fit on the negative gradient of the loss function (for mathematical proof check the [link](https://towardsdatascience.com/log-book-xgboost-the-math-behind-the-algorithm-54ddc5008850)
- This process of fitting the model iteratively on the -ve gradient will continue till we have reached the minima or the limit of the number of weak learners given by T, this is called the additive approach
- Recall that, in Adaboost,“shortcomings” are identified by high-weight data points. In Gradient Boosting, “shortcomings” are identified by gradients.
This is in short of the intuition as to how Gradient Boosting works. In case of regression and classification the only thing that differs is the loss function that is used.

---

### XGBoost
[📖Read](https://towardsdatascience.com/log-book-xgboost-the-math-behind-the-algorithm-54ddc5008850)

XGBoost stands for "Extreme Gradient Boosting", where the term "Gradient Boosting" originates from the paper Greedy Function Approximation: A Gradient Boosting Machine, by Friedman. It initially started as a research project by Tianqi Chen as part of the Distributed (Deep) Machine Learning Community (DMLC) group. It became well known in the ML competition circles after its use in the winning solution of the Higgs Machine Learning Challenge.

XGBoost and GBM both follow the principle of gradient boosted trees, but XGBoost uses a more regularized (by taking the model complexity into account) model formulation to control over-fitting, which gives it better performance, which is why it’s also known as ‘regularized boosting’ technique. In Stochastic Gradient Descent, used by Gradient Boosting, we use less point to take less time to compute the direction we should go towards, in order to make more of them, in the hope we go there quicker. In Newton’s method, used by XGBoost, we take more time to compute the direction we want to go into, in the hope we have to take fewer steps in order to get there.

