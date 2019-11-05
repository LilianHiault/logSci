import numpy as np
import matplotlib.pyplot as plt


# Functions
def feig(a, x, n):
    for i in range(1, n + 1):
        x = a * x * (1 - x)
    return x


def feigLi(xn, a):
    liste = [a * xn * (1 - xn)]
    for i in range(10):
        liste.append(a * liste[i] * (1 - liste[i]))
    return liste


# Main
a = eval(input("a : "))
x = eval(input("x0 : "))
n = eval(input("n : "))
res = feig(a, x, n)
print("Feigenbaum(", n, ") = ", res, " avec a = ", a, " et x0 = ", x, sep='')
print("10 éléments suivants :", feigLi(res, a))
