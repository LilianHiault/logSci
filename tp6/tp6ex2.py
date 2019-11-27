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
            long.append(lCourante[4])
            lat.append(lCourante[5])
            pop.append(lCourante[6])
            surface.append(lCourante[7])

# Analyse des résultats

# Ville la plus au Nord
print(nom[iMaxL(lat)], "est la ville la plus au Nord.")

# Latitude médiane
print("La latitude médiane est :", medLi(lat))
