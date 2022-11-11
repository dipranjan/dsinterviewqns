# Business Scenarios

```
:class: tip, dropdown

Suppose as a Netflix product Analyst you are speaking with a Product Manager of Netflix. You get the question as to "I would want to understand user base of Netflix". What would be your approach?
```

```
:class: dropdown

This type of questions are basically a coversation and tries to judge your skills in breaking down the problem statement and providing an analytical solution.

- Ask follow up questions, these problem statements are kept vague to encourage you to ask questions
- Define KPIs
- Speak about your assumptions
- Break down the problem statement into 2-3 pieces and tell how would you solve them
```

```
:class: tip, dropdown

Suppose your company has launched a Survey Monkey competitor and the PM wants to understand user growth. There are 2 flavors of the product:

- Unlimited survey's for 3 for a pro license
- One survey per license for a normal license
```

```
:class: dropdown

This type of questions are basically a coversation and tries to judge your skills in breaking down the problem statement and providing an analytical solution.

- Ask follow up questions, these problem statements are kept vague to encourage you to ask questions
- Define KPIs
- Speak about your assumptions
- Break down the problem statement into 2-3 pieces and tell how would you solve them
```

```
:class: tip, dropdown

Let's say that you're working at Netflix.

The company executives are working to renew a deal with another TV network that grants Netflix exclusive licensing to stream their hit TV series (think something like Friends or The Office). One of the executives wants to know how to approach this deal.

We know that the TV show has been on Netflix for a year already. 

How would you approach valuing the benefit of keeping this show on Netflix? 
```

```
:class: dropdown

Some of the factors which you can consider are as follows:

- Has the viewership stayed consistent or waned?
- Has there been any Social media backlash?
- Is there a new season or reunion or movie coming up?
- How many people who viewed this on Netflix renewed their subscriptions?
- What percent of viewers who saw this completed the entire series?
- How many of the people are repeat viewers of this seris?
```

```
:class: tip, dropdown

Let’s say that you’re in charge of Square’s small business division. 

The CEO wants to hire a customer success manager for help managing a new software product. Another executive thinks that it’s worth just instituting a free trial instead.

What would be your recommendation on utilizing a customer success manager versus just a free trial to get new or existing customers to use the new product?
```

```
:class: dropdown

SOLUTION PENDING
```

```
:class: tip, dropdown
[📖Source](https://www.interviewquery.com/questions/promoting-instagram) 

Let's say you work on the growth team at Facebook and are tasked with promoting Instagram from within the Facebook app.

Where and how could you promote Instagram through Facebook?
```

```
:class: dropdown

Goal: Increase awareness of Instragram through Facebook Hypothesis: Showing Instragram ads to users in their News Feed will increase the likelihood that they will login to Instragram by $X%$.

Run A/B test:
- Control group: no changes
- Variant group: will be shown Instagram ads as the first ad they see when scrolling through their News Feed.
- Randomly assign users to each group, making sure they’re not biased and are representative of the population.
- Set a significance level like 95%
- Set experiment time, how long the long experiement run
- Set the power,usually 80%
- Esimate intended effect size - 20%

Metrics:
- Number of Instagram logins after being exposed to the Instagram ad, 24 hours
- Instagram logins / number of users - Percent logging into Instagram after using Facebook
- Stop-gap metric: Ad revenue, CTR, revenue per session. Since we’re taking up ad space, we want to see how much these ads cost us
- The other idea is: Notifying ppl on Facebook when their friends join Instagram. We can do a regression of number of friends on Instagram vs % of those users who use Instagram

Another thing to add to this would be to look at including an Instagram reference/clickable when a user uploads a new photo/video to Facebook. It is a natural fit there since Instagram is a photo/video sharing paltform and it is a natural integration to bring those together for those users who do not have Instagram.
```

```
:class: tip, dropdown

[Source](https://www.linkedin.com/feed/update/urn:li:activity:6984161706524442624/)

LinkedIn’s marketing team tested two versions of email campaigns, A and B, in San Francisco(SF) and New York City (NYC). Of the 100,000 emails sent, 80% of the emails were version A while the rest were version B. Address the two questions below to guide the marketing team.
- Given that the click-through-rate (CTR) of email A was 15% while that of email B was 30%, which version is more effective?
- In SF, the CTR of email A was 15% while that of email B was 12.5%. In NYC, the CTR of email A was 15% while that of email B was 41.7%. 

The summary table below shows the number of emails per variation per city. Explain your assessment

| Variations | NYC    | SF     |
|------------|--------|--------|
| A          | 20,000 | 60,000 |
| B          | 12,000 | 8,000  |
```

```
:class: dropdown

**[Candidate]** Before I address your question, I will first organize CTR numbers you presented in a summary table:

| Variations | Size   | CTR | Count  |
|------------|--------|-----|--------|
| A          | 80,000 | 15% | 12,000 |
| B          | 20,000 | 30% | 6,000  |

As you mentioned, a total of 100,000 emails were dispatched, 80% being email A while the remaining being email B. Given the 15% CTR for email A and 30% CTR for email B, the counts of conversions were 12,000 and 6,000, A and B respectively. 

**[Interviewer]** Very well. What is your assessment?

**[Candidate]** Just based on CTR’s, email is more effective in conversion. However, the result might be due to chance.

**[Interviewer]** Can you elaborate?

**[Candidate]** To assess the CTR difference between the two emails, I would suggest a statistical test.

**[Interviewer]** Interesting. How would you use a statistical test?

**[Candidate]** First, I would state the hypothesis:

$H_o$: The CTR’s of emails A and B are the same.
$H_a$: The CTR’s of emails A and B are different.

Second, I would use either a chi-square contingency test or a T-test for two-sample proportions. If p-value of a test is less than the significance level at 0.05, reject the null hypothesis and conclude there is statistical significance in the CTR’s of the two emails. Finally, I can conclude that email B brings higher CTR than email A.

**[Interviewer]** Okay. Do you believe the unequal sample sizes between A and B pose an issue?

**[Candidate]** Not necessarily. I could foresee how the test's power may decrease as a consequence of the unequal sample size. However, one of the statistical tests I proposed assume that the sample size being equal. Therefore, I do not see an issue.

Coming to the second question:

**[Candidate]** The change in click-through-rates within each city is a well-known statistical phenomenon called Simpson’s Paradox, which states that trend changes or reverses when observations are grouped. In the previous problem, you stated that the CTR of email A was 15%
while that of email B was 30%, which suggests that email B produced higher CTR than email A. However, within SF, email A performed better than email B.

**[Interviewer]** Your observation that the reversal in CTR’s is Simpson’s Paradox is correct. What else can you tell me about the problem?

**[Candidate]** As I had done in the previous problem, let me organize the numbers in a summary table, rounded:

|            | Total        |              | NYC    |               | SF     |               |
|------------|--------------|--------------|--------|---------------|--------|---------------|
| Variations | Size         | Conversions  | Size   | Conversions   | Size   | Conversions   |
| A          | 80,000 (80%) | 12,000 (15%) | 20,000 | 3,000 (15%)   | 60,000 | 9000 (15%)    |
| B          | 20,000 (20%) | 6,000 (30%)  | 12,000 | 5,000 (41.7%) | 8,000  | 1,000 (12.5%) |

I have generic observations about the table. I see that the distribution of emails are higher for version B than A. I also see that San Francisco received higher allocation of email A than New York while New York received higher allocation of email B than email A.

**[Interviewer]** Okay, do you see any issues with unequal email allocations between the two cities?

**[Candidate]** Not at all as the primary metric is proportion, not count.

**[Interviewer]** Do you have a hypothesis on why CTR’s vary?

**[Candidate]** I presume that the version A email could be a generic email that does not improve CTR in one city over another. Version B might resonate with NYC market; hence, the CTR is at least 3X higher than that of version A. Perhaps, version B includes jobs in a finance industry that’s more prevalent in NYC than SF. I want to emphasize that the observed CTR’s occurred due to chance alone.

**[Interviewer]** What statistical method would you use to validate whether cities affect click-through-rate of emails?

**[Candidate]** If we disregard the possibility of interaction effect between email variations and cities, then we can use T-test for sample proportions to test whether cities affect email conversions.

First, I would establish the following hypothesis:
$H_o: CTR_{NYC} = CTR_{SF}$
$H_a: CTR_{NYC} ≠ CTR_{SF}$
Next, I would create the following numerical summary pooled across variations by city:

| Cities | Calculations                        | CTR's |
|--------|-------------------------------------|-------|
| NYC    | (3,000 + 5,000) / (20,000 + 12,000) | 25%   |
| SF     | (9,000 + 1,000)/6,000 + 60,000)     | -15%  |

Next, I would calculate the sample standard error, and calculate the T-statistic:
$T − Statistic = \frac{(CTR_{NYC} − CTR_{SF})}{SE}$
If the corresponding p-value is less than the usual significance level at 0.05, then reject the null hypothesis and conclude that there is statistical significance in the difference between the CTRs in the two cities at the significance level of 0.05.

**[Interviewer]** Could you have used a one-sample T-test?

**[Candidate]** Let me think. I believe it is possible to use a one-sample T-test. Instead of comparing the difference of CTR’s between NYC and SF, I can compare if the difference of CTR’s against 0 such that the hypothesis statements is now the following:
$H_o: (CTR_{NYC} − CTR_{SF}) = 0$
$H_a: (CTR_{NYC} − CTR_{SF}) ≠ 0$

Based on this change, the T-statistic is calculated as follows:
$T − Statistic = [(CTR_{NYC} − CTR_{SF}) − 0] / SE$

**[Interviewer]** Suppose that we do care about the interaction effect between city and variation. How would you evaluate it?

**[Candidate]** As I think about this problem more, I realize that I could have applied ANOVA with two main effects and one-interaction effect. The model could assess three null hypothesis at the same time:

- *Hypothesis 1 - There is no difference in CTRs between NYC and SF.*
- *Hypothesis 2 - There is no difference in CTRs between variations A and B.*
- *Hypothesis 3 - There is an interaction effect on CTRs between cities and variations.*

The ANOVA test would provde statistical significance of each of the three terms measured. If there is an interaction effect between the city and email variation, then the p-value of the interaction term will be less than the significance level.

**[Interviewer]** Okay, what is your final recommendation to the marketing team upon learning that there is an interaction effect?

**[Candidate]** I would explain that the statistical test result suggests that there is an effect on CTR given the variation across cities and emails. I would then advise that the study is expanded on more markets to assess this business hypothesis further. In addition, I would suggest that more variations of the email are tested to assess the following assumption - emails tailored to a city’s demography performs better than a generic version across markets.
 
| Assessments             | Rating | Comments                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
|-------------------------|--------|-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Statistical Methodology | 4      | In both problems, the candidate's statistical know-how was fairly strong.  In problem #1, she devised a statistical framework that addressed the interview question.  Her approach of utilizing T-test was appropriate.   In problem #2, most of her responses were solid except on a follow-up question involving one-sample T-test.  Given that sample-size difference between the two groups, mathematically, the statistical test is not possible.                                                |
| Product Sense           | 5      | In both questions, she ensured that her responses are grounded in the marketing problem.  She devised a numerical summary, making sense of the CTR metrics.  This allowed her to suggests approaches that aligned with the problem.  Lastly, in her last problem, when asked about her recommendation, she offered sound suggestions.  The idea of testing email variations on more than two emails makes sense to assess whether emails  focused on target market perform better than a general one. |
| Communication           | 5      | The candidate ensured that she understood the problems, illustrating a numerical summary and explaining her analysis clearly.  Her explanation of statistical were easy to follow and comprehensive. Lastly, she clearly explained recommendations to a  marketing team, suggesting that she possesses fluidity in stakeholder engagement.                                                                                                                                                            |
```
