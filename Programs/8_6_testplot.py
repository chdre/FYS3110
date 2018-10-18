import numpy as np
import matplotlib.pyplot as plt

def f(z):
    return np.cos(z) + np.sin(z)/z

z = np.linspace(1,50,1000)
plt.plot(z,f(z))
plt.show()
