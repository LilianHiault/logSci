# Défi Turing 17
import time


def divProp(n):
    """Somme des diviseurs propres de a"""
    somme = 0
    for i in range(1, n):
        if n % i == 0:
            somme += i
    return somme

def amicaux(a, b):
    """Si d(a) = b et d(b) = a et a != b alors a et b amicaux"""
    if divProp(a) == b and divProp(b) == a and a != b:
        return 1
    else:
        return 0


# Main
start_time = time.time()

somme = 0
for i in range(1, 100001):
    if amicaux(i, divProp(i)):
        print("Amicaux :", i, divProp(i))
        somme += i
print("La somme des nombres amicaux compris entre 1 et 100 000 est : ", somme)

print("Temps d'execution : %s secondes." % (time.time() - start_time))
