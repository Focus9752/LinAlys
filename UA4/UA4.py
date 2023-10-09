import numpy as np
import sympy as sp
from sympy import *

x = Symbol("x")

# Opg. 4.1
# a)

f = (1/x) - cos(x)/sin(x)

print("Grænseværdien for x->0+ er: {}".format(limit(f, x, 0, "+")
))
print(r"Grænseværdien for x->pi- er: {}".format(limit(f, x, pi, "-")
))



