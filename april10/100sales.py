# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 18:47:25 2018

@author: user
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("100 Sales Records.csv")

print(df.columns)
print(df.iloc[:10,:10])
cost = np.array(df['Total Profit']).reshape(-1,1)
print(cost)
country = np.array(df['Country']).reshape(-1,1)
print(country)
plt.scatter(country,cost)
plt.show()
plt.hist(cost,bins=20)
plt.show()
tcost =np.array(df['Total Cost']).reshape(-1,1)
for i in tcost:
    if i >= 1000000:
        print(i)