import matplotlib.pyplot as mpl

import numpy as np

x = np.linspace(0, 20, 100) # Create a list of evenly spaced number over range

mpl.plot(x, np.sin(x)) # Plot the sine of each x point

mpl.show()