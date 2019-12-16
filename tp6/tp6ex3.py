import matplotlib.pyplot as plt
import numpy as np


# Fonctions
def distCf(long, lat):
    lonCf = 0.053843408089816
    latCf = 0.79899719602977
    return ((lonCf - long)**2 + (latCf - lat)**2)**(1 / 2)


# Main

insee = []
nom = []
post = []
long = []
lat = []

with open("villes.csv", encoding="utf-8") as fichier:
    for ligne in fichier:
        if ligne[0] != 'I':
            lcour = ligne.split(";")
            insee.append(lcour[0])
            nom.append(lcour[1])
            post.append(lcour[3])
            long.append(float(lcour[4]))
            lat.append(float(lcour[5]))

# 1
idProche = []
villeProche = []

for i in range(len(nom)):
    if post[i][0:2] == "63" and nom[i] != "Clermont-Ferrand" and len(post[i]) == 5:
        idProche.append([nom[i], distCf(long[i], lat[i])])


def critere(L):
    return L[1]


idProche.sort(key=critere)

for i in range(30):
    print(idProche[i][0])

# 2
print("La commune du département la plus éloignée de Clermont-Ferrand est",
      idProche[-1][0])

# 3
print("Elle se situe à", idProche[-1][1] / (1.56961 * 10**(-4)), "kilomètres.")

# 4
rayon = idProche[-1][1]/2
comp = 0
for i in range(len(idProche)):
    if(idProche[i][1] <= rayon):
        comp += 1

print(comp, "communes se trouvent dans le rayon.")
print("Le pourcentage par rapport au nombre de communes du Puy de Dôme est", comp/len(idProche) * 100, "%")
