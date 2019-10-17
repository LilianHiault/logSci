import numpy as np


# Functions
def facto(n):
    if n == 1:
        return 1
    else:
        return n * facto(n - 1)


def euler(n):
    if n == 0:
        return 1
    else:
        return euler(n - 1) + 1 / facto(n)


# Main
nb = eval(input("Nombre : "))
print("Euler(", nb, ") = ", euler(nb), sep='')
