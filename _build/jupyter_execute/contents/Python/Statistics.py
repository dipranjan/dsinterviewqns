#!/usr/bin/env python
# coding: utf-8

# ## Statistics

# ### Questions

# ```{admonition} Problem: JOIN Dataframes
# :class: dropdown, tip
# Can you tell me the ways in which 2 pandas data frames can be joined?
# ```

# ```{admonition} Solution:
# :class: dropdown
# A very high level difference is that merge() is used to combine two (or more) dataframes on the basis of values of common columns (indices can also be used, use left_index=True and/or right_index=True), and concat() is used to append one (or more) dataframes one below the other (or sideways, depending on whether the axis option is set to 0 or 1).
# 
# join() is used to merge 2 dataframes on the basis of the index; instead of using merge() with the option left_index=True we can use join().
# 
# ![Combine DataFrames](images/image1.PNG)
# ```

# ```{admonition} Problem: [GOOGLE] Normal Distribution
# :class: dropdown, tip
# 
# Write a function to generate N samples from a normal distribution and plot the histogram.
# ```

# In[6]:


import numpy as np
import matplotlib.pyplot as plt
from scipy import stats

def normal_sample_generator(N):
    # can be done using np.random.randn or stats.norm.rvs
    #x = np.random.randn(N)
    x = stats.norm.rvs(size=N)
    num_bins = 20
    plt.hist(x, bins=num_bins, facecolor='blue', alpha=0.5)

    y = np.linspace(-4, 4, N)
    bin_width = (x.max() - x.min()) / num_bins
    plt.plot(y, stats.norm.pdf(y) * N * bin_width)

    plt.show()

normal_sample_generator(10000)


# ```{admonition} Problem: [UBER] Bernoulli trial generator
# :class: dropdown, tip
# 
# Given a random Bernoulli trial generator, write a function to return a value sampled from a normal distribution.
# ```

# ```{admonition} Solution:
# :class: dropdown
# Solution pending, [Reference material link](Given a random Bernoulli trial generator, how do you return a value sampled from a normal distribution?)
# ```

# ```{admonition} Problem: [PINTEREST] Interquartile Distance
# :class: dropdown, tip
# 
# Given an array of unsorted random numbers (decimals) find the interquartile distance.
# ```

# In[9]:


# Interquartile distance is the difference between first and third quartile

# first let's generate a list of random numbers

import random
import numpy as np

li = [round(random.uniform(33.33, 66.66), 2) for i in range(50)]
print(li)

qtl_1 = np.quantile(li,.25)
qtl_3 = np.quantile(li,.75)

print("Interquartile distance: ", qtl_1 - qtl_3)


# ````{admonition} Problem: [GENENTECH] Imputing the mdeian
# :class: dropdown, tip
# 
# Write a function cheese_median to impute the median price of the selected California cheeses in place of the missing values. You may assume at least one cheese is not missing its price.
# 
# Input:
# 
# ```python
# import pandas as pd
# 
# cheeses = {"Name": ["Bohemian Goat", "Central Coast Bleu", "Cowgirl Mozzarella", "Cypress Grove Cheddar", "Oakdale Colby"], "Price" : [15.00, None, 30.00, None, 45.00]}
# 
# df_cheeses = pd.DataFrame(cheeses)
# ```
# 
# |          Name         | Price |
# |:---------------------:|:-----:|
# | Bohemian Goat         | 15.00 |
# | Central Coast Bleu    | 30.00 |
# | Cowgirl Mozzarella    | 30.00 |
# | Cypress Grove Cheddar | 30.00 |
# | Oakdale Colby         | 45.00 |
# 
# ````

# In[9]:


import pandas as pd

cheeses = {"Name": ["Bohemian Goat", "Central Coast Bleu", "Cowgirl Mozzarella", "Cypress Grove Cheddar", "Oakdale Colby"], "Price" : [15.00, None, 30.00, None, 45.00]}

df_cheeses = pd.DataFrame(cheeses)

df_cheeses['Price'] = df_cheeses['Price'].fillna(df_cheeses['Price'].median())
df_cheeses.head()

