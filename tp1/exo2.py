#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 16:05:53 2021

@author: tugdual
"""
import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(0,10,1000)
m = np.tanh(x)
plt.figure(figsize = (5,5))
plt.plot(x,m, color = 'black')
plt.grid(True)
plt.xlim(0,5)
plt.ylim(0,1.1)
liste = np.arange(0.25,1.51,0.25)
for i in liste :
    plt.plot(x,x*i)
plt.show()