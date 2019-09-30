import numpy as np


# Functions

# Question 1
def pgcd(a, b):
    a = abs(a)
    b = abs(b)
    if b == 0:
        return a
    else:
        return pgcd(b, a % b)


# Question 2
def phi(n):
    nbEntiers = 0
    for k in range(1, n + 1):
        if pgcd(k, n) == 1:
            nbEntiers += 1
    return nbEntiers


def phiFraction():
    nb = 0
    for k in range(30):
        if pgcd(k, 30) == 1:
            nb += 1
    return nb


# Question 3
def farey(n):
    longueur = 0
    for i in range(1, n):
        longueur += phi(i)
    return longueur


# Main

# Question 1
#a = eval(input("a = "))
#b = eval(input("b = "))
#print("PGCD de", a, "et", b, "=", pgcd(a, b))

# Question 2
n = eval(input("n = "))
#print("phi(", n, ")", "=", phi(n))
#print("Nombre de fractions irréductibles dont le dénominateur est 30 :", phiFraction())

# Question 3
print("Suite de Farey avec n =", n, "est", farey(n))
