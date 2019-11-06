import sympy as sm
from sympy import var, pprint, solve, Rational


# Main
var('x')
p = 3 * x**3 - 7 * x**2 / 2 - x / 2 + 1
pprint(p)
pprint(solve(p, x))
pprint(p.subs(x, -1 / 2))
pprint(p.subs(x, Rational(2, 3)))
pprint(p.subs(x, 1))


var('x y z')
expr1 = 0 * x + 2 * y + 5 * z
expr2 = -3 * x + 2 * y - z
expr3 = -x + 2 * y + 2 * z
pprint(solve([expr1, expr2, expr3], [3, -1, 5]))
