import numpy as np
import sympy as sp
from sympy import *

y = Symbol("y")

lmda = 1
sol1 = nsolve(y * tan(y) - sqrt(lmda - y**2), y, (0, sqrt(lmda)))

lmda = 1/4
sol2 = nsolve(y * tan(y) - sqrt(lmda - y**2), y, (0, sqrt(lmda)))

print(round(sol1, 8))
print(round(sol2, 8))
