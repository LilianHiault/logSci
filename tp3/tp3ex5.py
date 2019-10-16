import numpy as np


# Functions
def harmonique(n):
    if n == 0:
        return 0
    else:
        return harmonique(n - 1) + 1 / n


# Main
n = eval(input("n = "))
print("Harmonique(", n, ") = ", harmonique(n), sep = '')
