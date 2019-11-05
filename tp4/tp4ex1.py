import numpy as np
import matplotlib.pyplot as plt


# Function
def fiboListe(n):
    fibo = [0, 1]
    for i in range(2, n):
        fibo.append(fibo[i - 1] + fibo[i - 2])
    return fibo


# Main
n = eval(input("n : "))
plt.plot(fiboListe(n))
plt.xlim(5, 25)
plt.yscale('log')
plt.show()
