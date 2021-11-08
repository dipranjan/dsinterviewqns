---
html_meta:
  "description lang=en": "Interview resource of Data Science Interview focusing on Industry application, practical success or failure of Data Science and Machine Learning Projects."
  "keywords": "interview, data science, machine learning, Generative, Discriminative"
  "property=og:locale": "en_US"
---

## Industry Application

```{admonition} Zillow
:class: Warning, dropdown

Zillow's rise and fall is a classic casestudy on both what to do and what not to do with data science and machine learning.

- Zillow was the brainchild of Richard Barton, the 54 year old American internet entrepreneur who also founded Expedia and Glassdoor
- Zestimate, which debuted in 2006, it was a proprietary algorithm based on a neural network model which used house facts, location, housing market trends, property values, data from county, tax assessor records, as well as direct feeds from hundreds of multiple listing services and brokerages to determine the price of a house
- It was very successful in driving conversation around property, so much so that browsing property valuations became a hobby for many. With shows like Saturday Night Live encouraging the habit, it became trendy to find the value of your neighboring houses to identify how posh of an area you live in.
- Zestimate has a median error rate of $1.9%$ for homes that are on-market and $6.9%$ for homes that are off-market. But this accuracy varies widely across cities and their corresponding housing markets. In Cincinnati, for instance, approximately $35%$ of Zestimates for off-market homes were within $5%$ of the eventual sales prices, and $82%$ were within $20%$ of the price. Comparatively, in Denver, $51%$ of Zestimates were within $5%$ of the sales price, and $94%$ were within $20%$ of the sales figure
- Zillow, had recognized the need to improve the accuracy of its valuation model. In 2017, the company launched a contest with a \$1M prize money, Zestimate was on average around $10K off of the actual sales price of a median-priced home, and that the information provided by the winning team would reduce that margin by around $1.3K, the prize went to a group of data scientists and engineers from three different countries: Chahhou Mohamed of Morocco, Jordan Meyer of the United States and Nima Shahbazi of Canada
- In February Zillow announced that the Zestimate would represent "an initial cash offer" for eligible homes spread across 20 cities, from Nashville, Houston, Phoenix, Miami to Denver and Los Angeles
- The problem started due to the pandemic, since summer of 2020 the housing market in USA was hot and quite some unforeseen trends had cropped up. For example, post pandemic there was a sudden increase in demand for bigger houses in the suburbs, which based on historical data was difficult to generate an estimate of. There were data issues too, Zillow missed out on having real time brokering data in new markets, post sales data also takes time to be updated hence there was always a lag as to what prices the recent houses have sold at. Other issues have also been pointed at, Zillow said it did not find enough workers to revamp and repair the houses it had bought in order to put them in the market. Zillow had tweaked its algorithms to price houses aggressively and at the end it had a purchased houses at a higher price that it could sell in a market that was cooling down
- By October 17th, there were signs of trouble: Zillow had paused new house offers for the year as it sorted through a backlog of properties under contract. On November 1st, Zillow marketed nearly 7,000 houses for a total of $2.8 Billion. The operation was shut down a day later by its board of directors

So what went wrong, nothing that we already don't know of, extrapolating existing data in new pandemic era market, unforeseen market dynamics, over reliance on algorithmic outputs while not considering ground realities.
```



