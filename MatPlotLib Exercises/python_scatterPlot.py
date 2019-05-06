import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


A = pd.read_csv('data_1d.csv', header=None).as_matrix()
x = A[:,0] #scatter data 
y = A[:,1] #scatter data
x_line = np.linspace(0, 100, 100)
y_line = 2 * x_line + 1

plt.scatter(x,y)
plt.plot(x_line, y_line)
plt.show()

