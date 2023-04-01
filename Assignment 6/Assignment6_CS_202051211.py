#!/usr/bin/env python
# coding: utf-8

# # Assignment 6
# 
# ## Glen Quadros
# ## 202051211

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# In[3]:


female_pop_df = pd.read_csv('/Users/glenquadros/Desktop/Data Analysis and Visualization/Assignment 6/population_of_female.csv')


# In[5]:


female_pop_df.tail()


# In[6]:


primary_comp_rate_female_df = pd.read_csv('/Users/glenquadros/Desktop/Data Analysis and Visualization/Assignment 6/primary_completion_rate_female.csv')


# In[7]:


primary_comp_rate_female_df.tail()


# ### 1. Create a column named “average_rate” in “primary_completion_rate_female.csv” that contains the average (over time) completion rate.

# In[8]:


primary_comp_rate_female_df['average_rate'] = primary_comp_rate_female_df.mean(axis=1)


# In[9]:


primary_comp_rate_female_df


# ### 2. Create a column named “Latest Population” in “population_of_female.csv” that contains the latest population of females in the country.

# In[12]:


female_pop_df['Latest Population'] = female_pop_df['2021']


# In[15]:


female_pop_df.tail()


# ### 3. What is the weighted average of primary rates of different countries? The weight should be the Latest population of females in the country.

# In[20]:


weights = female_pop_df['Latest Population']/female_pop_df['Latest Population'].sum()


# In[21]:


weights


# ### 4. What is the Median of average primary completion rate?

# In[22]:


female_pop_df['Latest Population'].median()


# ### 5. What is the InterQuartile Range of average primary completion rate?

# In[23]:


IQR = female_pop_df["Latest Population"].quantile(0.75) - female_pop_df["Latest Population"].quantile(0.25)


# In[24]:


IQR


# ### 6. What is the Variance of average primary completion rate?

# In[25]:


female_pop_df['Latest Population'].var()


# In[ ]:




