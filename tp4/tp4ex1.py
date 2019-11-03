import numpy as np
import matplotlib.pyplot as plt


# Function
def fibo(n):
    if n < 2:
        return n
    else:
        u = 0
        uMoins2 = 0
        uMoins1 = 1
        for i in range(2, n + 1):
            u = uMoins1 + uMoins2
            uMoins2 = uMoins1
            uMoins1 = u
        return u


def fiboListe(n):
    fibo = [0, 1]
    for i in range(2, n):
        fibo.append(fibo[i - 1] + fibo[i - 2])
    return fibo


# Main
n = eval(input("n : "))
print("Fibonacci(", n, ") = ", fibo(n), sep='')
plt.plot(fiboListe(n))
plt.show()
