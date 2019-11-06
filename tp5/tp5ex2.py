import sympy as sm


def suiteLog(x, n):
    if n >= 0:
        xn = x
        for i in range(n):
            xn = (4 * xn * (1 - xn)).evalf(500)
    return xn


def suiteLog2(y, n):
    if n >= 0:
        yn = y
        for i in range(n):
            yn = 4 * yn - 4 * yn**2
    return yn


x = sm.Float(0.23)
nMax = 60
print("Résultat de la suite pour x =", x,
      " et n =", nMax, ":", suiteLog(x, nMax).evalf(20))

y = x
print("Résultat de la suite pour y =", y,
      " et n =", nMax, ":", suiteLog2(y, nMax))
