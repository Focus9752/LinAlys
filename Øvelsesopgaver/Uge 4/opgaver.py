import sympy as sp
from sympy import *
from sympy import Symbol

# US 8.3 

# a)
x = Symbol("X")
defint = integrate(x*sp.sin(x), (x, 0, pi))

print(defint)

# b)
defint = integrate(sp.sin(x)/x, (x, pi/2, pi))

print(defint)



