# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import numpy as np
import matplotlib.pyplot as plt

eps = np.spacing(0)
print(eps)
x = np.linspace(-4,3,101)
fig = plt.figure()

for i in range(len(x)-1):
    if x[i] == 0:
        x[i] = eps

ax = plt.plot(x,np.sin(x)/x)
plt.show()







        
            