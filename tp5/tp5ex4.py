import sympy as sm
from sympy import var, pprint


# Main
var('x a b c h u v w')
p = a * x**2 + b * x + c

pprint(sm.solve([(p - u).subs(x, 0), (p - v).subs(x, h / 2),
                 (p - w).subs(x, h)], [a, b, c]))

sol = p.subs(a, (2*(u-2*v+w))/(h**2), ).subs(b, (-3*u+4*v-w)/h).subs(c, u)

sol = sol.subs(u, 0).subs(v, 2).subs(w, 1).subs(h, 2)

pprint(sol)

sm.plot(sol, (x, 0, 2))
