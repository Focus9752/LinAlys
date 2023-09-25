import numpy as np
import sympy as sp
from sympy import *

y = Symbol("y")

# Navnet "lambda" er forbudt i python da det bruges til anonyme funktioner
lmda = 1
# Vi leder efter løsninger i intervallet (0, sqrt(lambda)), da vi får oplyst at 0 < y < lambda
sol1 = nsolve(y * tan(y) - sqrt(lmda - y**2), y, (0, sqrt(lmda)))

lmda = 1/4
sol2 = nsolve(y * tan(y) - sqrt(lmda - y**2), y, (0, sqrt(lmda)))

# Afrund til 8 decimaler og print svaret
print(round(sol1, 8))
print(round(sol2, 8))
