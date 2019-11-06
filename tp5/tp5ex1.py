import sympy as sm

# Main
sm.var('x y z')

sm.pprint(sm.expand((x - 1) * (x - 2) * (x + 3)))

sm.pprint(sm.factor(x**3 - 39 * x - 70))

sm.pprint(sm.together(1 / (x + 1) + 1 / y + 1 / z))
sm.pprint(sm.ratsimp(1 / (x + 1) + 1 / y + 1 / z))

sm.pprint(sm.apart((2 * x**2 + 4 * x + 3) / (x**3 - 39 * x - 70)))

sm.pprint(sm.simplify(sm.cos(x + y) + sm.cos(x - y) +
                      sm.sin(x + y) + sm.sin(x - y)))

p = 2 * x**2 - 3 * x + 1
sm.pprint(p)
sm.pprint(p.subs(x, 5))
sm.pprint(sm.simplify(p.subs(x, y + 1) - p.subs(x, y - 1)))

sm.pprint(sm.sqrt(10).evalf())
x = sm.pi
sm.pprint((x**2 + x + 1).evalf())
sm.pprint(sm.pi.evalf(500))
