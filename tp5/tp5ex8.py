import sympy as sm
from sympy import var, pprint


# Main
var('x')
f = 1 / 2 * x**2 + x - 1
tan = 3 * (x - 2) + 3
sm.plot(f, tan, (x, -10, 10))
