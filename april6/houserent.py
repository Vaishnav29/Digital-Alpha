# -*- coding: utf-8 -*-
"""
Created on Sat Apr  7 18:07:38 2018

@author: user
"""

import matplotlib.pyplot as plt
import numpy as np
x= [425,430,430,435,435,435,435,435,440,440,440,440,440,445,445,445,445,445,450,450,450,450,450,450,450,460,460,460,465,465,465,470,470,472,475,475,475,480,480,480,480,485,490,490,490,500,500,500,500,510,510,515,525,525,525,535,549,550,570,570,575,575,580,590,600,600,600,600,615,615]
frequency_dict = {}
for i in x:
    if frequency_dict.get(i):
        frequency_dict[i] +=1
    else:
        frequency_dict[i] = 1
X = []
Y = []
for key,value in frequency_dict.items():
    X.append(key)
    Y.append(value)
plt.scatter(X,Y,color='red')
x_mean = np.mean(X)
y_mean = np.mean(Y)
numer = 0
denom = 0
for i in range(len(X)):
    numer = numer + ((X[i] - x_mean)*(Y[i] - y_mean))
    denom = denom + (X[i] - x_mean)**2
b2= numer/denom
b1 = y_mean - b2*x_mean
print("y = %f + %f x"%(b1,b2))
x_min = np.min(X)
x_max = np.max(X)
xFinal = np.linspace(x_min,x_max,10)
yFinal = b1 + b2*xFinal
plt.plot(xFinal,yFinal,'g')