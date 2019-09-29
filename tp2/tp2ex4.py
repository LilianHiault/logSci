# Suite de Fibonacci

import numpy as np


# Question 1
def fiboListe(n):
    fibo = [0, 1]
    for i in range(2, n):
        fibo.append(fibo[i - 1] + fibo[i - 2])
    return fibo


# Question 2
def fibo(u):
    if u == 0:
        return 0
    elif u == 1:
        return 1
    else:
        return fibo(u - 1) + fibo(u - 2)


# Question 3
def sommePairsFibo(n):
    return n


# Main
n = eval(input("n = ")) + 1

# Question 1
print("Suite de Fibonacci de 0 à n :", fiboListe(n))

# Question 2
for i in range(n):
    print("Suite de Fibonacci de u(", i, "):", fibo(i))

# Question 3
print("Somme des nombres pairs de la suite de Fibonacci jusqu'à n =",
      n, " modulo 10 000 007 est :", sommePairsFibo(n))
