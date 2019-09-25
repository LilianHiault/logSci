# Suite de Fibonacci

import numpy as np


# Exercice 1
def fiboListe(n):
    fibo = [0, 1]
    for i in range(2, n):
        fibo.append(fibo[i - 1] + fibo[i - 2])
    return fibo


# Exercice 2
def fibo(n):
    return fibo


# Main
n = eval(input("n = "))

# Exercice 1
print("Suite de Fibonacci de 0 à n :", fiboListe(n))

# Exercice 2
print("Suite de Fibonacci de 0 à n :", fibo(n))
