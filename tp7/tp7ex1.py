# TP 7 Exercice 1
from numpy.random import randint
import matplotlib.pyplot as plt


# Fonctions
def exp():
    experience = []
    for i in range(100):
        experience.append(randint(0, 2))
    return experience


def pf():
    experience = exp()
    pile = 0
    for lancer in experience:
        if lancer == 1:
            pile += 1
    return pile


# Main
sup = 0
inf = 0
egal = 0
for i in range(20000):
    if pf() > 53:
        sup += 1
    elif pf() <= 40:
        inf += 1

print("Probabilité que le nombre de pile soit supérieur à 53 :", sup/20000)
print("Probabilité qu'il soit inférieur ou égal à 40 :", inf/20000)

plt.
