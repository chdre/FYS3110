import numpy as np
from scipy.optimize import fsolve
import matplotlib.pyplot as plt

N = 100
beta = 1.0      #alpha = hbar^2/ma

E = np.zeros((N,3))
K = np.zeros(N)

def func(z,l):
    K = 2.0*np.pi*l/float(N)   #dropping a since cos(Ka)
    f = np.cos(z) + beta*np.sin(z)/z - np.cos(K)
    return f

def solver(l,n):
    z0 = n**2
    z = fsolve(func,z0,args=(l))
    return z**2

for n in range(1,4):
    for l in range(0,N):
        E[l,n-1] = solver(l,n)

l_arr = np.linspace(0,N-1,100)
K = 2.0*np.pi*l_arr/float(N)

plt.plot(K,E)
plt.legend(["1","2","3"])
plt.show()
