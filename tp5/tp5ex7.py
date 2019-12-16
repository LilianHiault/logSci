import sympy as sm
from sympy import pprint, var


# Main
var('x a n')
f = (x**(n - 1)) / (a + x)
vn = sm.integrate(f, (x, 0, 1))
pprint(vn)

print("")
v40 = vn.subs(n, 40)
pprint(v40)

print("")
v40 = v40.subs(a, 3)
pprint(v40)

print("")
v40 = v40.evalf()
pprint(v40)
