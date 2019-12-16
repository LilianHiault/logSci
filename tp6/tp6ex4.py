import matplotlib.pyplot as plt
import numpy as np


# Main
data = []
lettres = [0] * 26

# 1
with open("sherlock.txt", encoding="utf-8") as fichier:
    for ligne in fichier:
        data = ligne.upper()
        for i in range(ord("A"), ord("Z") + 1):
            comp = data.count(chr(i))
            lettres[i - 65] += comp

nbOcc = []
for i in range(ord("A"), ord("Z") + 1):
    nbOcc.append([chr(i), lettres[i - 65]])

print(nbOcc)

# 2


def nOcc(couple):
    return couple[1]


nbOcc.sort(reverse=True, key=lambda x: x[1])
print(nbOcc)

# 3

occ = []
lettre = []

for l in range(9):
    occ.append(nbOcc[l][1])
    lettre.append(nbOcc[l][0])

print(occ)
print(lettre)

index = np.arange(len(occ))
largeur = 0.5
plt.bar(index + 1, occ, largeur, color='r')
plt.xticks(index + 1, lettre)

plt.show()
