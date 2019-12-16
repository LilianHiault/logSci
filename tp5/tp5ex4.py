import sympy as sm
from sympy import var, pprint


# Main
var('x a b c h u v w')
p = a * x**2 + b * x + c

pprint(sm.solve([p.subs(x, 0) - u, p.subs(x, h / 2) - v,
                 p.subs(x, h) - w], [a, b, c]))

sol = p.subs(a, (2*(u-2*v+w))/(h**2))
sol = sol.subs(b, (-3*u+4*v-w)/h)
sol = p.subs(c, u)

sol = sol.subs(u, 0).subs(v, 2).subs(w, 1).subs(h, 2)

pprint(sol)

sm.plot(sol, (x, 0, 2))
