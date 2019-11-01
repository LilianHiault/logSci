import numpy as np
from time import time


# Functions
def harmonique(n):
    if n == 0:
        return 0
    else:
        return harmonique(n - 1) + 1 / n


def fibo_r(u):
    if u == 0:
        return 0
    elif u == 1:
        return 1
    else:
        return fibo_r(u - 1) + fibo_r(u - 2)


# Main
n = eval(input("n = "))
print("Harmonique(", n, ") = ", harmonique(n), sep='')
t_start = time()
print("Fibonacci(", n, ") = ", fibo_r(n), sep='')
t_fin = time()
print("Temps d'exécution de fibo(", n, ") : ", t_fin - t_start, " sec.", sep='')
