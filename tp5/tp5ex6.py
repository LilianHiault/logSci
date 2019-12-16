import sympy as sm
from sympy import var, pprint, sqrt, log


# Main
var('x')
f = (x * log(sqrt(x**2 + 3))) / (sqrt(x**2 + 3))
pprint(f)

u = log(sqrt(x**2 + 3))
du = sm.diff(u, x)
dv = x / sqrt(x**2 + 3)
v = sm.intergrate(dv, x)

prim = (u * v).subs(x, b) - (u * v).subs(x, a)
integr = integrate(du * v, (x, a, b))

pprint(prim)
pprint(integr)

F = prim - integr
pprint(F)
