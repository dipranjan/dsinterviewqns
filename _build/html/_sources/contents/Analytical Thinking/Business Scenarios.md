---
html_meta:
  "description lang=en": "Interview resource of Data Science Interview focusing on Business Scenarios."
  "keywords": "interview, data science, machine learning, Business Scenarios, practice questions"
  "property=og:locale": "en_US"
---

## Business Scenarios

```{admonition} Problem: [SALESFORCE] User Aquisition
:class: tip, dropdown

Suppose as a Netflix product Analyst you are speaking with a Product Manager of Netflix. You get the question as to "I would want to understand user base of Netflix". What would be your approach?

```

```{admonition} Solution:
:class: dropdown

This type of questions are basically a coversation and tries to judge your skills in breaking down the problem statement and providing an analytical solution.

- Ask follow up questions, these problem statements are kept vague to encourage you to ask questions
- Define KPIs
- Speak about your assumptions
- Break down the problem statement into 2-3 pieces and tell how would you solve them
```


```{admonition} Problem: [SALESFORCE] Survey Monkey Alternative
:class: tip, dropdown

Suppose your company has launched a Survey Monkey competitor and the PM wants to understand user growth. There are 2 flavors of the product:

- Unlimited survey's for 3 for a pro license
- One survey per license for a normal license

```

```{admonition} Solution:
:class: dropdown

This type of questions are basically a coversation and tries to judge your skills in breaking down the problem statement and providing an analytical solution.

- Ask follow up questions, these problem statements are kept vague to encourage you to ask questions
- Define KPIs
- Speak about your assumptions
- Break down the problem statement into 2-3 pieces and tell how would you solve them
```


```{admonition} Problem: [NETFLIX] Licensing Valuation
:class: tip, dropdown

Let's say that you're working at Netflix.

The company executives are working to renew a deal with another TV network that grants Netflix exclusive licensing to stream their hit TV series (think something like Friends or The Office). One of the executives wants to know how to approach this deal.

We know that the TV show has been on Netflix for a year already. 

How would you approach valuing the benefit of keeping this show on Netflix? 
```

```{admonition} Solution:
:class: dropdown

Some of the factors which you can consider are as follows:

- Has the viewership stayed consistent or waned?
- Has there been any Social media backlash?
- Is there a new season or reunion or movie coming up?
- How many people who viewed this on Netflix renewed their subscriptions?
- What percent of viewers who saw this completed the entire series?
- How many of the people are repeat viewers of this seris?
```

```{admonition} Problem: [SQUARE] Growing Small Business
:class: tip, dropdown

Let’s say that you’re in charge of Square’s small business division. 

The CEO wants to hire a customer success manager for help managing a new software product. Another executive thinks that it’s worth just instituting a free trial instead.

What would be your recommendation on utilizing a customer success manager versus just a free trial to get new or existing customers to use the new product?

```

```{admonition} Solution:
:class: dropdown

SOLUTION PENDING

```

```{admonition} Problem: [INSTAGRAM] Promoting Instagram
:class: tip, dropdown
[📖Source](https://www.interviewquery.com/questions/promoting-instagram) 

Let's say you work on the growth team at Facebook and are tasked with promoting Instagram from within the Facebook app.

Where and how could you promote Instagram through Facebook?

```

```{admonition} Solution:
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