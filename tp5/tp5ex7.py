import sympy as sm
from sympy import pprint, var


# Main
var('x a n')
f = (x**(n - 1)) / (a + x)
vn = sm.integrate(f, (x, 0, 1))
