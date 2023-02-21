# -*- coding: utf-8 -*-
"""Assignment4 CS 202051211.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1Z7xAFiXRZEVetuDv7xAX49Dv3o63BuB7

# Assignment 4

## Glen Quadros
"""

import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

egg_df = pd.read_csv('/content/Egg_Production_2007_2012.csv')

milk_df = pd.read_csv('/content/Milk_Production_2007_2012.csv')

"""## 1. Merge two data frames such that the new data frame has multi-level columns (like years under milk and eggs). Try to change the column names if required."""

egg_df.head()

milk_df.head()

egg_df = egg_df.set_index('States/Uts')

milk_df = milk_df.set_index('States/Uts')

columns1 = [('Milk','2007-08'),('Milk','2008-09'),('Milk','2009-10'),('Milk','2010-11'),('Milk','2011-12')]
columns2 = [('Eggs','2007-08 (In lakh nos.)'),('Eggs','2008-09 (In lakh nos.)'),('Eggs','2009-10 (In lakh nos.)'),('Eggs','2010-11 (In lakh nos.)'),('Eggs','2011-12 (In lakh nos.)')]

egg_df.columns = pd.MultiIndex.from_tuples(columns2)

milk_df.columns = pd.MultiIndex.from_tuples(columns1)

df = milk_df.join(egg_df)

df.head()

"""## 2. Present the production of milk in Gujarat, Kerala, Andhra Pradesh, Uttar Pradesh and Punjab on 2007-2008 as a Pie chart. The pie chart should consist of proportion in percentage and labels for each piece."""

places = ["Gujarat","Kerala","Andhra Pradesh","Uttar Pradesh","Punjab"]

plt.title('Production of milk (2007-2008)')

pie = df.iloc[:,0:1]
pie = pie.filter(items=places,axis=0)
pie = pie.T
x = pie.values.flatten()
plt.pie(x, labels=places, explode=[0,0.3,0,0,0])
plt.show()

"""## 3. Plot five pie charts of egg production in Gujarat, Kerala, Andhra Pradesh, Uttar Pradesh and Punjab for the five years range. Each pie chart should represent the proportional egg production in Gujarat, Kerala, Andhra Pradesh, Uttar Pradesh and Punjab for a given year."""

pie1 = egg_df.filter(items=places, axis=0)
pie1 = pie1.T
vals = pie1.T.values

fig, axes = plt.subplots(2,3,figsize=(18,12))
fig.delaxes(axes[1][2])
axes[0][0].pie(pie1.loc[("Eggs","2007-08 (In lakh nos.)")].values, labels=places, autopct='%.0f%%')
axes[0,0].set_title("2007-08")
axes[0][1].pie(pie1.loc[("Eggs","2008-09 (In lakh nos.)")].values, labels=places, autopct='%.0f%%')
axes[0,1].set_title("2008-09")
axes[0][2].pie(pie1.loc[("Eggs","2009-10 (In lakh nos.)")].values, labels=places, autopct='%.0f%%')
axes[0,2].set_title("2009-10")
axes[1][0].pie(pie1.loc[("Eggs","2010-11 (In lakh nos.)")].values, labels=places, autopct='%.0f%%')
axes[1,0].set_title("2010-11")
axes[1][1].pie(pie1.loc[("Eggs","2011-12 (In lakh nos.)")].values, labels=places, autopct='%.0f%%')
axes[1,1].set_title("2011-12")

"""## 4. Plot Stacked Area Chart that represents the proportional egg production state wise over five years. There would be five stacked colors for Gujarat, Kerala, Andhra Pradesh, Uttar Pradesh"""

pie1.plot(kind='area', stacked=True, figsize=(16,9))

