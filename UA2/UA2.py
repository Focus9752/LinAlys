import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.backends.backend_pdf import PdfPages

plt.figure(1)

# 25 punkter
n_arr = np.array([i for i in range(25)])
x_arr = np.array([])

mu = 2.5

# For X0 = 0.01
x = 0.01                                       
for i in range(25):            
    x = mu*x*(1-x)
    x_arr = np.append(x_arr, x) 

plt.scatter(n_arr, x_arr, label="X0 = 0.01")


x_arr = np.array([])
# For X0 = 0.1
x = 0.1                                       
for i in range(25):            
    x = mu*x*(1-x)
    x_arr = np.append(x_arr, x) 

plt.scatter(n_arr, x_arr, label="X0 = 0.1")

x_arr = np.array([])
# For X0 = 0.3
x = 0.3                                       
for i in range(25):            
    x = mu*x*(1-x)
    x_arr = np.append(x_arr, x) 

plt.scatter(n_arr, x_arr, label="X0 = 0.3")

x_arr = np.array([])
# For X0 = 0.5
x = 0.5                                       
for i in range(25):            
    x = mu*x*(1-x)
    x_arr = np.append(x_arr, x) 

plt.scatter(n_arr, x_arr, label="X0 = 0.5")

# Legend
plt.legend(loc="lower right")

# Akser
ax = plt.gca()
ax.set_xlabel("n")
ax.set_ylabel("x(n)")
plt.title("Opgave a)")
plt.plot()

plt.figure(2)

x_arr = np.array([])

mu = 2.5

# For X0 = mu-1/mu
x = (2.5-1)/2.5                                       
for i in range(25):            
    x = mu*x*(1-x)
    x_arr = np.append(x_arr, x) 

plt.scatter(n_arr, x_arr, label="X0 = \u03BC - 1 / \u03BC")

plt.legend(loc="lower right")
ax = plt.gca()
ax.set_xlabel("n")
ax.set_ylabel("x(n)")
plt.title("Opgave c)")
plt.plot()

plt.figure(3)

# 100 punkter
n_arr = np.array([i for i in range(100)])
x_arr = np.array([])

# For X0 = 0.01, mu=3
mu = 3
x = (2.5-1)/2.5                                       
for i in range(100):            
    x = mu*x*(1-x)
    x_arr = np.append(x_arr, x) 

plt.scatter(n_arr, x_arr, label="X0 = 0.01")

plt.legend(loc="lower right")
ax = plt.gca()
ax.set_xlabel("n")
ax.set_ylabel("x(n)")
plt.title("Opgave d)")
plt.plot()

plt.figure(4)

# 1.000.000 punkter
n_arr = np.array([i for i in range(1000000)])
x_arr = np.array([])

# For X0 = 0.01, mu=3
mu = 3.01
x = (2.5-1)/2.5                                       
for i in range(1000000):            
    x = mu*x*(1-x)
    x_arr = np.append(x_arr, x) 

plt.scatter(n_arr, x_arr, label="X0 = 0.01")

plt.legend(loc="lower right")
ax = plt.gca()
ax.set_xlabel("n")
ax.set_ylabel("x(n)")
plt.title("Opgave e)")
plt.plot()

plt.figure(5)

# 1000 punkter
n_arr = np.array([i for i in range(1000)])
x_arr = np.array([])

# For X0 = 0.01, mu=3
mu = 3.9
x = (2.5-1)/2.5                                       
for i in range(1000):            
    x = mu*x*(1-x)
    x_arr = np.append(x_arr, x) 

plt.scatter(n_arr, x_arr, label="X0 = 0.01")

plt.legend(loc="lower right")
ax = plt.gca()
ax.set_xlabel("n")
ax.set_ylabel("x(n)")
plt.title('"Kaotiskt plot"')
plt.plot()

pdp = PdfPages(r"C:\Users\marcu\OneDrive\Documents\GitHub\LinAlys\UA2\plots.pdf")
pdp.savefig(1)
pdp.savefig(2)
pdp.savefig(3)
pdp.savefig(4)
pdp.savefig(5)
pdp.close()

