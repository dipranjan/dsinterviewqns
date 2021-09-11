#!/usr/bin/env python
# coding: utf-8

# ## Statistics

# ```{admonition} Problem:
# :class: tip
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

