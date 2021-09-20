#!/usr/bin/env python
# coding: utf-8

# ## Data Manipulation

# ```{admonition} Problem: Score Bucketization
# :class: dropdown, tip
# 
# **Asked By - GOOGLE**
# 
# Let's say you're given a list of standardized test scores from high schoolers from grades $9$ to $12$.
# 
# Given the dataset, write code in Pandas to return the cumulative percentage of students that received scores within the buckets of $<50, <75, <90, <100$.
# 
# Example Input:
# 
# user_id | grade | test score
# --------+-------+-----------
# 1       | 10    | 85
# 2       | 10    | 60
# 3       | 11    | 90
# 4       | 10    | 30
# 5       | 11    | 99
# 
# Example Output:
# 
# grade   |test score  |percentage 
# --------+------------+-----------
# 10      | <50        | 30%
# 10      | <75        | 65%
# 10      | <90        | 96%
# 10      | <100       | 99%
# 11      | <50        | 15%
# 11      | <75        | 50%
# 
# 
# ```

# In[1]:


import pandas as pd
import numpy as np

df = pd.DataFrame([[1,10,85],[2,10,60],[3,11,90],[4,10,30],[5,11,99]], columns = ["user_id","grade","test score"])

df["<50"] = np.where(df["test score"]<50,1,0)
df["<75"] = np.where(df["test score"]<75,1,0)
df["<90"] = np.where(df["test score"]<90,1,0)
df["<100"] = np.where(df["test score"]<100,1,0)

df = df.groupby(["grade"])[["<50","<75","<90","<100"]].sum().reset_index()
df = df.melt(id_vars=["grade"],var_name="test score",value_name="count")

df["grp_ttl"] = df.groupby("grade")["count"].transform('max')
df["percentage"] = 100*df["count"]/df["grp_ttl"]

df = (df[["grade","test score","percentage"]].copy()).sort_values(["grade","percentage"],ascending=True)

df["percentage"] = df.percentage.astype(int).astype(str)
df["percentage"] = df["percentage"] + "%"

df.head(10)

