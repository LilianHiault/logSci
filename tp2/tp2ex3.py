import numpy as np


# Exercice 1
def inverse(l):
    return l[::-1]


# Exercice 2
def dec(b):
    decimal = 0
    bin = inverse(b)
    comp = 0
    for i in bin:
        decimal += i * 2**comp
        comp += 1
    return decimal


# Exercice 4
def binaire(n):
    l = []
    puissance = 1
    while 2**puissance < n:
        puissance *= 2
    while n > 0:
        l.append(n // 2**puissance)
        n %= 2**puissance
        puissance -= 1
    return l


l = [1, 1, 0, 1]
print("Inverse de", l, ":", inverse(l))
print("Décimal de", l, ":", dec(l))
# Exercice 3
bin1 = [1, 1, 0, 1, 1, 0, 0]
bin2 = [1, 0, 1, 0, 1, 0, 1, 0]
print(bin1, "(2) +", bin2, "(2) =", dec(bin1) + dec(bin2), "(10)")
# Exercice 4
n = 13
print("Écriture en binaire de", n, ":", binaire(n))
