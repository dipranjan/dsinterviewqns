---
description: >-
  The theorem gives us the ability to quantify the likelihood that our sample
  will deviate from the population without having to take any new sample to
  compare it with.
---

# Central Limit Theorem

## Sampling distribution

Let's start with an example, suppose from the SAT math scores

* You take a sample of $$10$$ random students from a population of $$100$$. You might get a mean of $$502$$ for that sample.
* Then, you do it again with a new sample of $$10$$ students. You might get a mean of $$480$$ this time.
* Then, you do it again. And again. And again...... and get the following means for each of those three new samples of $$10$$ people: $$550$$, $$517$$, $$472$$

<figure><img src="../_build/html/_images/image81 (1).PNG" alt=""><figcaption></figcaption></figure>

The sampling distribution, which is basically the distribution of sample means of a population, has some interesting properties which are collectively called the **central limit theorem**, _which states that no matter how the original population is distributed, the sampling distribution will follow these three properties_ –

* Sampling Distribution’s Mean $$(\mu_{\bar{x}}) =$$ Population Mean $$(\mu)$$
* Sampling Distribution’s Standard Deviation (Standard Error) $$= \sigma\sqrt{n}$$, where $$\sigma$$ is the population’s standard deviation and $$n$$ is the sample size
* For $$n > 30$$, the sampling distribution becomes a normal distribution. Strongly skewed distributions can require larger sample sizes.

To prove the thrid point let's take a uniform distribution, in the image below $$500,000$$ times for each sample size $$(5, 20, 40)$$ have been drawn and their mean plotted. We’d expect the average to be $$(1 + 2 + 3 + 4 + 5 + 6 / 6 = 3.5)$$. The sampling distributions of the means center on this value. Just as the central limit theorem predicts, as we increase the sample size, the sampling distributions more closely approximate a normal distribution and have a tighter spread of values.

<figure><img src="../_build/html/_images/image91.PNG" alt=""><figcaption></figcaption></figure>

### Confidence Interval <a href="#what_is_confidence_interval" id="what_is_confidence_interval"></a>

([Source](https://www.simplilearn.com/tutorials/data-analytics-tutorial/confidence-intervals-in-statistics))

A confidence interval shows the probability that a parameter will fall between a pair of values around the mean. Confidence intervals show the degree of uncertainty or certainty in a sampling method. They are constructed using confidence levels of 95% or 99%.

<figure><img src="../.gitbook/assets/image (24).png" alt=""><figcaption></figcaption></figure>

The formula for CI is given by: (_mean – (z\* (std\_dev/sqrt(n))_

#### Calculating A Confidence Interval <a href="#calculating_a_confidence_interval" id="calculating_a_confidence_interval"></a>

Imagine a group of researchers who are trying to decide whether or not the oranges produced on a certain farm are large enough to be sold to a potential grocery chain. This will serve as an example of how to compute a confidence interval.

#### Step 1: Determine the sample size (n).

46 oranges are chosen at random by the researchers from farm trees. Consequently, n is 46.

#### Step 2: Determine the samples' means (x).

The researchers next determine the sample's mean weight, which comes out to be 86 grammes.

X = 86.

#### Step 3: Determine the standard deviation (s).

Although utilising the population-wide standard deviation is ideal, this data is frequently unavailable to researchers. If this is the case, the researchers should apply the sample's determined standard deviation.

Let's assume, for our example, that the researchers have chosen to compute the standard deviation from their sample. They get a 6.2-gramme standard deviation.

S = 6.2.

#### Step 4: Determine the confidence interval

In ordinary market research studies, 95% and 99% are the most popular selection for confidence intervals. For this example, let's assume that the researchers employ a 95% confidence interval.

#### Step 5: Find the Z value for the chosen confidence interval

The researchers would subsequently use the following table to establish their Z value:

Confidence Interval Z

80% 1.282

85% 1.440

90% 1.645

95% 1.960

99% 2.576

99.5% 2.807

99.9% 3.291

#### Step 6: Calculate the following formula

The next step would be for the researchers to enter their known values into the formula. Following our example, this formula would look like this:

86 ± 1.960 (6.2/6.782). This calculation yields a value of 86±1.79, which the researchers use as their confidence interval.

#### Step 7: Come to a decision.

According to the study's findings, the real mean of the larger population of oranges is probably (with a 95% confidence level) between 84.21 grammes and 87.79 grammes.
