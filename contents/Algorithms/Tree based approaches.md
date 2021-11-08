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

```{figure} ../Algorithms/images/image10.PNG
---
name: image10
scale: 80%
---
Adaboost Pseudocode
```

---

### XGBoost
[📖Source](https://towardsdatascience.com/log-book-xgboost-the-math-behind-the-algorithm-54ddc5008850)

XGBoost stands for "Extreme Gradient Boosting", where the term "Gradient Boosting" originates from the paper Greedy Function Approximation: A Gradient Boosting Machine, by Friedman. 



---
