def suiteLog(x, n):
    if n >= 0:
        xn = x
        for i in range(n):
            xn = 4 * xn * (1 - xn)
    return xn


def suiteLog2(y, n):
    if n >= 0:
        yn = y
        for i in range(n):
            yn = 4 * yn - 4 * yn**2
    return yn


x = 0.23
nMax = 60
print("Résultat de la suite pour x = ", x,
      " et n = ", nMax, " : ", suiteLog(x, nMax))

y = x
print("Résultat de la suite pour y = ", y,
      " et n = ", nMax, " : ", suiteLog2(y, nMax))

# L'écart est dû aux erreurs d'arrondi liées aux calculs en base 2.
