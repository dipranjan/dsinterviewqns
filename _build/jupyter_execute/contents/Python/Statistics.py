#!/usr/bin/env python
# coding: utf-8

# ## Statistics

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

# ```{admonition} Problem: Normal Distribution
# :class: dropdown, tip
# 
# **Asked By - GOOGLE**
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


# ```{admonition} Problem: Bernoulli trial generator
# :class: dropdown, tip
# 
# **Asked By - UBER**
# 
# Given a random Bernoulli trial generator, write a function to return a value sampled from a normal distribution.
# ```

# ```{admonition} Solution:
# :class: dropdown
# Solution pending, [Reference material link](Given a random Bernoulli trial generator, how do you return a value sampled from a normal distribution?)
# ```
