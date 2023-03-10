# -*- coding: utf-8 -*-
"""Assignment4_CS_202051211.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1nQwseGdcYGNq5V9b1Kd561wRyCDGJc2y
"""

import pandas as pd
import seaborn as sns
import numpy as np
import matplotlib.pyplot as plt
from joypy import joyplot 
import squarify 
import plotly.express as px 
from itertools import product
from statsmodels.graphics.mosaicplot import mosaic

milk_df = pd.read_csv('/content/Milk_Production_2007_2012.csv')

milk_df.head()

egg_df = pd.read_csv('/content/Egg_Production_2007_2012.csv')

egg_df.head()

merged_dataframe = egg_df.merge(milk_df, on='States/Uts')

merged_dataframe.head()

new_dataframe = merged_dataframe.iloc[:10,[0,1,2,6,7]]
new_dataframe

mosaic_df = pd.melt(new_dataframe, id_vars=['States/Uts'], var_name='Year', value_name='Value')

plt.figure(figsize=(16,9))
mosaic(mosaic_df, ['Year', 'States/Uts'], title='Mosaic Plot for State-wise Data')
plt.show()

plt.figure(figsize=(12, 8))
squarify.plot(sizes=merged_dataframe['2007-08'], label=merged_dataframe['States/Uts'], alpha=0.7)
plt.title("Tree Map for State-wise Data (2007-08)")
plt.axis('off')
plt.show()

