# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


# that command tells this notebook to put plots into the notebook
import matplotlib.pyplot as plt
import numpy as np
lstY = [9, 4, 3, 5, 2, 1, 9, 4, 6, 7]

x = np.arange(10) # like range()
#y = np.random.rand(10) # ten random floats, 0->1
y = np.array(lstY)

plt.plot(x,y, '*--')

plt.xlabel('xaxis')
plt.ylabel('yaxis')
plt.title('graph!')
