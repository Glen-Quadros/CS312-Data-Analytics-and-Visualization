# -*- coding: utf-8 -*-
"""Assignment3 CS 202051211

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/11_51x49SXoOoIrLvEF7GwUUl2u3PAZE-
"""

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

!pip install joypy

from joypy import joyplot

df = pd.read_csv('/content/grains_production_india_from_2001_to_2017.csv')

df.head()

df.columns

df.isna().sum()

df = df.dropna()

new_df1 = df[['Year', 'Food Grains (Cereals) - Rice (000 tonnes)',
       'Food Grains (Cereals) - Jowar (000 tonnes)',
       'Food Grains (Cereals) - Bajra (000 tonnes)',
       'Food Grains (Cereals) - Maize (000 tonnes)',
       'Food Grains (Cereals) - Ragi (000 tonnes)',
       'Food Grains (Cereals) - Small Millets (000 tonnes)',
       'Food Grains (Cereals) - Wheat (000 tonnes)',
       'Food Grains (Cereals) - Barley (000 tonnes)',
       'Food Grains (Pulses) - Gram (000 tonnes)',
       'Food Grains (Pulses) - Tur (000 tonnes)',
       'Food Grains (Pulses) - Other Pulses (000 tonnes)']]

new_df1.rename(columns = {'Food Grains (Cereals) - Rice (000 tonnes)' : 'Rice',
       'Food Grains (Cereals) - Jowar (000 tonnes)' : 'Jowar',
       'Food Grains (Cereals) - Bajra (000 tonnes)' : 'Bajra',
       'Food Grains (Cereals) - Maize (000 tonnes)' : 'Maize',
       'Food Grains (Cereals) - Ragi (000 tonnes)' : 'Ragi',
       'Food Grains (Cereals) - Small Millets (000 tonnes)' : 'Small Millets',
       'Food Grains (Cereals) - Wheat (000 tonnes)' : 'Wheat',
       'Food Grains (Cereals) - Barley (000 tonnes)' : 'Barley',
       'Food Grains (Pulses) - Gram (000 tonnes)' : 'Gram',
       'Food Grains (Pulses) - Tur (000 tonnes)' : 'Tur',
       'Food Grains (Pulses) - Other Pulses (000 tonnes)' : 'Other Pulses',
       }, inplace=True
       )

plt.figure(figsize=(15,10))
sns.boxplot(data=new_df1)

plt.figure(figsize=(15,10))
sns.violinplot(data=new_df1)

plt.figure(figsize=(15,10))
sns.stripplot(data=new_df1)

joyplot(new_df1,overlap = 0);

new_df2 = df[['Oilseeds - Ground-nuts (000 tonnes)',
       'Oilseeds - Sesamum (000 tonnes)',
       'Oilseeds - Rapeseed and Mustard (000 tonnes)',
       'Oilseeds - Linseed (000 tonnes)',
       'Oilseeds - Castor seed (000 tonnes)']]

new_df2 = new_df2.rename(columns = {'Oilseeds - Ground-nuts (000 tonnes)' : 'Ground-nuts',
       'Oilseeds - Sesamum (000 tonnes)' : 'Sesamum',
       'Oilseeds - Rapeseed and Mustard (000 tonnes)' : 'Rapeseed and Mustard',
       'Oilseeds - Linseed (000 tonnes)' : 'Linseed',
       'Oilseeds - Castor seed (000 tonnes)' : 'Castor seed'
       })

new_df2

plt.figure(figsize=(15,10))
sns.boxplot(data=new_df2)

plt.figure(figsize=(15,10))
sns.violinplot(data=new_df2)

plt.figure(figsize=(15,10))
sns.stripplot(data=new_df2)

joyplot(new_df2,overlap = 0);