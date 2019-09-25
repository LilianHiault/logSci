import numpy as np


def suite(a, n):
    v = np.log10((1 + a) / a)
    for i in range(1, n - 1):
        v = 1 / (n - 1) - a * v
        print("v(", i, ") =", v)
    return v


a = 3
n = 40
print("Avec a =", a, "v(", n, ") = ", suite(a, n))
