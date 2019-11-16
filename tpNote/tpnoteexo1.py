import numpy as np
import matplotlib.pyplot as plt
from time import perf_counter

# Lilian HIAULT et Tom LHÔPITAL
# Exercice 1 repris après la séance de TP noté

## Fonctions

def mindiv(n): # Retourne le plus petit entier k ≥ 2 qui divise n.
    sqrtn = np.sqrt(n)

    if n >= 2:
        k = 2

        while (n % k != 0) and (k <= sqrtn):
            k += 1

        if (k > sqrtn): # Si on a testé jusqu'à la racine carrée de n sans trouver de diviseur:
            k = n # alors n est premier et son plus petit diviseur est lui-même.

        return k

def dec_prem_loop(n): # Retourne la liste des diviseurs premiers de n avec multiplicité.
    reste = n / mindiv(n)
    divprem = [int(mindiv(n))]

    while reste > 1:
        divprem.append(int(mindiv(reste)))
        reste = reste / mindiv(reste)

    return divprem

def dec_prem_rec(n): # Retourne divprem, la liste des diviseurs premiers de n avec multiplicité.
    if n / mindiv(n) < 2:
        return [int(mindiv(n))]
    else:
        return [int(mindiv(n))] + dec_prem_rec(n / mindiv(n))

## Programme principal

# Question 1
n = 200376
print("1.\nPlus petit diviseur k ≥ 2 de", n, ":", mindiv(n))

# Question 2
m = 63075
print("\n2.\nListe des diviseurs premiers de", m, "avec multiplicité (fonction avec boucle) :", dec_prem_loop(m))
print("Liste des diviseurs premiers de", m, "avec multiplicité (fonction récursive) :", dec_prem_rec(m))

# Question 3
x = []
nbmoyfactprem = []

t_start = perf_counter()

for n in range(2, 10001): # Pour n allant  de 2 à 10000:
    x.append(n)
    sum = 0

    for i in range(2, n + 1): # On calcule la somme des facteurs premiers (avec multiplicité) jusqu'au rang n.
        sum += (len(dec_prem_loop(i)))

    nbmoyfactprem.append((1 / (n - 1) * sum)) # On calcule le nombre moyen de facteurs premiers (avec multiplicité) jusqu'au rang n, que l'on stocke dans la liste nbmoyfactprem.

t_end = perf_counter()
print("\n3.\nTemps de calcul :", round(t_end - t_start, 2), "secondes")

plt.plot(x, nbmoyfactprem, label = "n variant de 2 à 10000", color = "green")
plt.xlim(2, 10000)
#plt.xticks(np.linspace(start = 2, stop = 10000, num = 20, dtype = int))
plt.xticks([2, 250, 500, 1000, 1500, 2000, 3000, 4000, 5000, 7500, 10000])
plt.title("Nombre moyen de facteurs premiers (avec multiplicité) jusqu'au rang n ≥ 2")
plt.legend(loc = 0)
plt.xkcd()
plt.show()
