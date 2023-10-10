import numpy as np
import matplotlib.pyplot as plt
from matplotlib import style
from matplotlib.backends.backend_pdf import PdfPages

import sympy as sp
from sympy import *

x = Symbol("x")

# Opg. 4.1
# a)

expr = (1/x) - cos(x)/sin(x)

print("Grænseværdien for x->0+ er: {}".format(limit(expr, x, 0, "+")
))
print(r"Grænseværdien for x->pi- er: {}".format(limit(expr, x, pi, "-")
))

# c)
sol = nsolve(expr, x, (pi,6))
print("\n Løsningen til f(c)=0 i (pi,2pi) er: {}".format(sol))

# Opg. 4.2
# a)
def f(x):
    if 1 <= x <= 3:
        return x
    else:
        return (1-x**2) / (x-1)*(x-3)

# Plot
x_vals = np.linspace(-10,10, num=10000)
y_vals = [f(num) for num in x_vals]

plt.figure(1)
ax = plt.gca()
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
plt.title("Fig. 1")
plt.plot()
plt.plot(x_vals, y_vals)

# Tæt på x=1
x_vals = np.linspace(0,2, num=1000)
y_vals = [f(num) for num in x_vals]

plt.figure(2)
ax = plt.gca()
ax.set_xlabel("x")
ax.set_ylabel("f(x)")
plt.title("Fig. 2")
plt.plot(x_vals, y_vals)

pdp = PdfPages(r"C:\Users\marcu\OneDrive\Documents\GitHub\LinAlys\UA4\plots.pdf")
pdp.savefig(1)
pdp.savefig(2)
pdp.close()

