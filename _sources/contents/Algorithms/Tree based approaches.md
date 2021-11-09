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

