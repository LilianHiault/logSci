import matplotlib.pyplot as plt


# Fonctions
def iMaxL(liste):
    max = liste[0]
    iMax = 0
    comp = 0
    for elem in liste:
        if elem > max:
            max = elem
            iMax = comp
        comp += 1
    return iMax


def medLi(liste):
    listeMed = liste[:]
    listeMed.sort()
    if len(liste) % 2 == 0:
        return (listeMed[len(liste) / 2] + listeMed[(len(liste) / 2) + 1]) / 2
    else:
        return listeMed[len(liste)//2]

def popMoy(liste):
    lPopMoy = []
    nbVilles = 0;
    for popVille in liste:
        if popVille >= 1000 and popVille <= 20000:
            lPopMoy.append(popVille)
            nbVilles += 1


def distPts(xa, ya, xb, yb):
    return ((xb - xa)**2 + (yb - ya)**2)**(1/2)



# Main

# Listes
insee = []
nom = []
alt = []
post = []
long = []
lat = []
pop = []
surface = []

# Ouverture et lecture du fichier
with open("villes.csv", encoding="utf-8") as fichier:
    for ligne in fichier:
        if ligne[0] != "I":
            lCourante = ligne.split(";")
            insee.append(lCourante[0])
            nom.append(lCourante[1])
            alt.append(lCourante[2])
            post.append(lCourante[3])
            long.append(float(lCourante[4]))
            lat.append(float(lCourante[5]))
            pop.append(int(lCourante[6]))
            surface.append(lCourante[7])

# Analyse des résultats

# Ville la plus au Nord
print(nom[iMaxL(lat)], "est la ville la plus au Nord.")

# Latitude et longitude médiane
print("La latitude médiane est :", medLi(lat))
print("La longitude médiane est :", medLi(long))

# Commune médiane
distMed = distPts(lat[0], medLi(lat), long[0], medLi(long))
indice = 0
for i in range(len(nom)):
    if distPts(lat[i], medLi(lat), long[i], medLi(long)) < distMed:
        distMed = distPts(lat[i], medLi(lat), long[i], medLi(long))
        indice = i

print("La ville la plus proche du point médian est ", nom[indice], "dont les coordonnées sont : ", long[indice], lat[indice])

# Population des communes ayant entre 1000 et 20 000 habitants

# Visualiser les communes de France
latGr = []
longGr = []
latPet = []
longPet = []
for i in range(len(nom)):
    if pop[i] > 100000:
        latGr.append(lat[i])
        longGr.append(long[i])
    else:
        latPet.append(lat[i])
        longPet.append(long[i])

plt.plot(longPet, latPet, '.', color = 'b')
plt.plot(longGr, latGr, '.', color = 'r', markersize = 5)
plt.legend(loc=0)
plt.title("Communes de France")
plt.axis("equal")
plt.show()
