import matplotlib.pyplot as plt


# Fonctions
def indiceMin(liste):
    min = liste[0]
    iMin = 0
    comp = 0
    for elem in liste:
        if elem < min:
            min = elem
            iMin = comp
        comp += 1
    return iMin

def totalAcc(liste):
    sum = 0
    for elem in liste:
        sum += elem
    return sum


# Main
co = []  # Cours d'ouverture du jour
cc = []  # Cours à la clôture
cma = []  # Cours maximal du jour
cmi = []  # Cours minimal du jour
dt = []  # Date du jour
acc = [] # Accroissements journaliers

# Ouverture et lecture
with open("cac40.csv", encoding="utf-8") as fichier:
    for ligne in fichier:
        # print(ligne)
        ligneEnCours = ligne.split(";")
        co.append(float(ligneEnCours[2]))
        cc.append(float(ligneEnCours[5]))
        cma.append(float(ligneEnCours[3]))
        cmi.append(float(ligneEnCours[4]))
        dt.append(ligneEnCours[1])
        acc.append(float(ligneEnCours[2]) - float(ligneEnCours[5]))

# Nombre de jours
print(len(dt), "jours sont répertoriés dans le fichier.")

# Cours le plus bas
iCmaPlusBas = indiceMin(cma)
print("Le cours le plus bas dans la période est",
      cma[iCmaPlusBas], "le", dt[iCmaPlusBas])

# Accroissements journaliers
print("Total accroissements journaliers :",totalAcc(acc))
