import numpy as np


# Functions
def pgcd(a, b):
    a = abs(a)
    b = abs(b)
    if b == 0:
        return a
    else:
        return pgcd(b, a % b)


# Main
a = eval(input("a = "))
b = eval(input("b = "))
print("PGCD de", a, "et", b, ":", pgcd(a, b))
