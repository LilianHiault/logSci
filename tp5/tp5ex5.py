import sympy as sm
from sympy import var, pprint


# Fonctions

# Main
var('x a n')


# 1
print("Question 1 :")
pprint(sm.limit(sm.sqrt(x**2 + x) - sm.sqrt(x**2 + 1), x, sm.oo))
pprint(sm.limit((1 + a/(3*n))**(2*n), n, sm.oo))

# 2
print("Question 2 :")
f = x/(1 + sm.sqrt(x))
pprint(sm.integrate(f))
# pprint(sm.simplify(sm.diff(sm.integrate(f))))
g = 3*x*sm.sqrt(1 + x**2)
pprint(sm.integrate(g))

h = (sm.sqrt(sm.log(x)))/x
pprint(sm.integrate(h, (x, 1, 2)))
