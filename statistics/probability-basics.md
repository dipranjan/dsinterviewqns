---
description: >-
  Probability theory is the mathematical foundation of statistical inference,
  which is indispensable for analyzing data affected by chance, and thus
  essential for data scientists.
---

# Probability Basics

<figure><img src="../.gitbook/assets/prob basic cartoon" alt=""><figcaption></figcaption></figure>

Probability theory is the mathematical framework that allows us to analyze chance events in a logically sound manner. The probability of an event is a number indicating how likely that event will occur.

Note that when we say the probability of a head is 1/2, we are not claiming that any sequence of coin tosses will consist of exactly 50% heads. If we toss a fair coin ten times, it would not be surprising to observe 6 heads and 4 tails, or even 3 heads and 7 tails. But as we continue to toss the coin over and over again, we expect the long-run frequency of heads to get ever closer to 50%.&#x20;

**In general, it is important in statistics to understand the distinction between theoretical and empirical quantities. Here, the true (theoretical) probability of a head was 1/2, but any realized (empirical) sequence of coin tosses may have more or less than exactly 50% heads.**

## Common Terminologies

The **sample space is the set of all possible outcomes in the experiment**: for some dice $$Ω = {1, 2, 3, 4, 5, 6}$$.

Any **subset of Ω is a valid event**. we can speak of the event $$F$$ of rolling a 4, $$F = {4}$$.

Consider the outcome of a single die roll and call it $$X$$. A reasonable question one might ask is “What is the average value of $$X$$?". We define this notion of “average” as a weighted sum of outcomes. This is called the **expected value**, or expectation of $$X$$, denoted by $$E(X)$$,

$$
Weighted Average = \frac{1}{6} * (1 + 2 + 3 + 4 + 5 + 6) = 3.5
$$

If you play the game $$\infty$$ times the average value becomes $$E(X)$$

The **variance** of a random variable $$X$$ is a nonnegative number that summarizes on average how much $$X$$ differs from its mean, or expectation. The square root of the variance is called the **standard deviation.**

$$
Var(X) = \frac{(1−3.5)^2+(2−3.5)^2+(3−3.5)^2+(4−3.5)^2+(5−3.5)^2+(6−3.5)^2}{6} = \frac{17.5}{6}
$$

## Set

A set, broadly defined, is a collection of objects. In the context of probability theory, we use set notation to specify compound events. For example, we can represent the event _roll an even numbe_r by the set {2, 4, 6}.

## Permutation and Combination

It can be surprisingly difficult to count the number of sequences or sets satisfying certain conditions. This is where **Premutation and Combination** comes in. For example, consider a bag of marbles in which each marble is a different color. If we draw marbles one at a time from the bag without replacement, how many different ordered sequences (permutations) of the marbles are possible? How many different unordered sets (combinations)?

* Permutation($$AB \neq BA$$ , order matters) = $$nPr = \frac{n!}{(n-r)!}$$
* Combination ($$AB = BA$$, order does not matter) = $$nCr = \frac{n!}{r!(n-r)!}$$

## Joint & Conditional Probability

* Joint Probability is the probability of two independent events occurring: $$P(A \cap B) = P(A)*P(B)$$
* Conditional probability tells the probability of $$B$$ given $$A$$ has occurred, it allows us to account for information we have about our system of interest: $$P(B|A) = \frac{P(A \cap B)}{P(A)}$$

**If both are same, then A and B are independent events.**

## Bayes' Theorem

Bayes' theorem, named after 18th-century British mathematician Thomas Bayes, is a mathematical formula for determining conditional probability. **Conditional probability is the likelihood of an outcome occurring, based on a previous outcome occurring.**

<figure><img src="../.gitbook/assets/Baye&#x27;s theorem" alt=""><figcaption><p>Baye's Theorem</p></figcaption></figure>

An easy way of remembering it is using the below example:

What is the probability of a fruit being banana given that it is long and yellow?

$$
P(Banana|Long,Yellow) = \frac{P(Long|Banana)*P(Yellow|Banana)*P(Banana)}{P(Long)*P(Yellow)}
$$

## MAP vs MLE

The Maximum Aposteriori Probability (MAP) Estimation of the random variable y, given we have observed IID $$(x_1, x_2, x_3, ... )$$ here we try to accommodate our prior knowledge when estimating. In Maximum Likelihood Estimation (MLE), we assume we don’t have any prior knowledge of the quantity being estimated.

<figure><img src="../.gitbook/assets/MAP vs MLE" alt=""><figcaption><p>MAP vs MLE</p></figcaption></figure>

## Questions

<details>

<summary>[UBER] Dice in increasing order</summary>

We throw 3 dice one by one. What is the probability that we obtain 3 points in strictly increasing order?

**Answer**

Suppose we get $$4$$ in the first roll then,

Total Probability = $$P(4) * P(5) * P(6) = 1/6 * 1/6 * 1/6 = 1/216$$

Similarly for $$3$$, $$P(3) * P(4,5 | 4,6 | 5,6) = 1/6 * (1/36 + 1/36 + 1/36) = 3/216$$

Taking into consideration $$P(1)$$ and $$P(2)$$ we have the total as $$= 10/216 + 6/216 + 3/216 + 1/216 = 20/216$$

</details>

<details>

<summary>[LINKEDIN] Cards in increasing order</summary>

Imagine a deck of 500 cards numbered from 1 to 500. If all the cards are shuffled randomly and you are asked to pick three cards, one at a time, what's the probability of each subsequent card being larger than the previous drawn card?

**Answer**

It is actually easy to solve this if you think on it a little. Let's pick any $$3$$ cards, now if you rearrange it there will only be $$1$$ way in which each subsequent card is larger the previous card. So, a total of $$6$$ **** ways to arrange the cards out of which only $$1$$ is valid. So the result is $$\frac{1}{6}$$.

</details>

<details>

<summary>[STATE FARM] Cards without replacement</summary>

Pull 2 cards from a deck without replacement what is probability _that both are of different colors._

There can be many variants to this question.

**Answer**

[Source](https://www.quora.com/Two-cards-are-drawn-for-a-pack-of-52-cards-What-is-the-probability-that-both-the-cards-are-of-the-same-colour)

Here it is not specified which color the cards should be - they can be either red or black.

The probability that the first card drawn is either red or black is $$1$$ since these two are the only possible outcomes.

After the first draw, the total number of cards remaining in the pack is $$51$$, out of which $$25$$ cards are of the same colour as that of the card that is already drawn. Hence the probability of drawing a card of the same colour as the first one is $$\frac{25}{51}$$.

⇒ The probability of drawing two cards of the same colour is $$1*\frac{25}{51}=\frac{25}{51}$$.

_Another approach to this can be:_

Two cards of a particular color can be drawn in $$C(26,2)$$ ways.

⇒ Two cards of either red or black can be drawn in $$2×C(26,2)$$ ways.

The total number of ways of drawing any two cards from the pack is $$C(52,2)$$.

⇒ The probability of drawing two cards of the same colour is $$\frac{2×C(26,2)}{C(52,2)} = \frac{2×26!}{2!×24!}\frac{2!×50!}{52!}=\frac{25}{51}$$

</details>

<details>

<summary>[FACEBOOK] N Dice</summary>

Suppose you're playing a dice game. You have 2 dice.

* What's the probability of rolling at least one 3?
* What's the probability of rolling at least one 3 given N die?

**Answer**

P(at least 1 three) = P(exactly 1 three) + P(2 three) = 1/6 \* 5/6 + 5/6 \* 1/6 + 1/36 = 11/36

_Solution received from the community via_ [_mail_](mailto:thedatascienceinterviewbook@gmail.com)

To count the number of ways to throw at least $$1$$ three for $$N$$ dice, you need to sum overall $$k$$, $$1<k<=N$$, where $$k$$ is the number of threes you throw. For each $$k$$, there are $$C(N,k)$$ possible combinations of dice that are three. For each of these combinations, there are $$5$$ possible values for the other $$N-K$$ dice. So, the number of ways to throw $$k$$ threes with $$N$$ dice is $$5^{(N-k)}*C(N,k)$$.

The total sum over $$1<k<=N$$ is $$\sum_{k=1}^N 5^{(N-k)} \begin{pmatrix} n\ k\ \end{pmatrix} = 6^N-5^N$$. Since there are $$6^N$$ ways to throw the dice, the probability is $$(6^N - 5^N)/6^N = 1 - (5/6)^N$$.

There is a simpler way to solve this problem: calculate the number of ways to not throw any threes, then subtract this number from the total number of ways to throw the dice. For $$N=2$$, this is $$1 - (5/6)^2 = 1 - 25/36 = 11/36$$. For $$N$$, it is $$1 - (5/6)^N$$ You can see that this is equivalent to the probability calculated using the above sum: $$1 - (5/6)^N$$.

**`Tip:`**` ``Check the general case for N=2 and see if the numbers match`

</details>

<details>

<summary>[FACEBOOK] 3 Zebras</summary>

Three zebras are chilling in the desert. Suddenly a lion attacks.

Each zebra is sitting on a corner of an equally length triangle. Each zebra randomly picks a direction and only runs along the outline of the triangle to either edge of the triangle.

What is the probability that none of the zebras collide?

**Answer**

Each zebra has 2 options of travel: clockwise or anticlockwise. So a total of $$2*2*2 = 8$$ options.

Out of this only way in which they donot collide is if all of them travel clockwise or anticlockwise. So a total of $$2$$.

Therefore the probability of no collision $$= 2/8 = 25%\$$

</details>

