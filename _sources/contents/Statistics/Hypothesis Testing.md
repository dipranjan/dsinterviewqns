## Hypothesis Testing


```{admonition} Problem: Testing Hypotheses with t-Test
:class: tip, dropdown

**Asked By - AMAZON**

You are testing hundreds of hypotheses with a t-test, what considerations should be made?
```

```{admonition} Solution:
:class: dropdown

Type 1 error will scale the more the number of t-tests are run. If $\alpha = 0.05$ then there is $5%$ chance of Type 1 error on a single test, then across many tests $p(Type I)$ will increase. For example with 2 tests:

$
P(type I error) = p(type I error on A OR type I error on B) 
= 2p(type I error on single test) - p(type I error on A AND type I error on B) 
= 2*.05 - .05^2 (assuming independence of tests) = 0.5 - .025 = .075
$

If you want your $p(type I error)$ across n-tests to remain at $5%$, you will need to decrease the  $\alpha\ in each individual test. Bonferroni correction can be applied. Basically alpha will be reduced to alpha/n. n is number of experiments you are running.

Otherwise, you can try and run an F-test to start in order to identify if a least $1$ test sees some significant effect. Then run a t-test on the specific experiment with the highest effect size. Granted, the p-value of the test will also depend on the variance of the sample in the given test, if we assume constant variance across tests, then the test with the highest effect size is in expectation the best performing test. Only running a single t-test will keep your p(type I error) low.

```