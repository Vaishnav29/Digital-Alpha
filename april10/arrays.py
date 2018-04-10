# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 19:18:22 2018

@author: user
"""

import numpy as np
a = np.eye(3)
print(a.shape)
b = a.reshape(3,3,1)
print(b.shape)
print(a)
print(b)
