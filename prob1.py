# Problem 1

import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import statistics as st

dataset = pd.read_csv('house_rent.csv')
X = dataset.iloc[:, 0].values

# Calculating mean, median and mode
mean = np.mean(X)
print("mean is", mean)
median = np.median(X)
print("median is", median)
modex = st.mode(X)
print("mode is", modex)

# Frequency distribution
from collections import Counter
fd = Counter(X)
print(fd)

# Cumulative frequency distribution
from scipy.stats import cumfreq
cf = cumfreq(X)
print(cf)

# 25th, 50th and 75th percentile values
p1 = np.percentile(X, 25)
print("25th percentile is", p1)
p2 = np.percentile(X, 50)
print("50th percentile is", p2)
p3 = np.percentile(X, 75)
print("75th percentile is", p3)

# variance and co-efficient of variance
vari = np.var(X)
print("Variance is", vari)
std_dev = np.std(X)
co_v = (std_dev/mean)*100
print("Co-eeficient of variance is", co_v)