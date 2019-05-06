import matplotlib.pyplot as plt
import numpy as np

plt.title ("Line Chart")
plt.xlabel("Time")
x = np.linspace(0, 10, 100)

plt.ylabel("Some function of time")
y = np.sin(x)

plt.plot(x,y)
plt.show()
