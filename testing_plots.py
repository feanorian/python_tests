import matplotlib as mpl
import numpy as np
import matplotlib.pyplot as plt
x_range = np.arange(0.1,10,0.01)
y_range = np.sin(x_range)

plt.plot(x_range,y_range)

plt.savefig('sinewave2')
