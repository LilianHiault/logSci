# Fonctions
def indiceMin(liste):
    min = liste[0]
    iMin = 0
    for i in liste:
        if liste[i] > min:
            min = liste[i]
            iMin = i
    return i


# Main

co = []  # Cours d'ouverture du jour
cc = []  # Cours à la clôture
cma = []  # Cours maximal du jour
cmi = []  # Cours minimal du jour
dt = []  # Date du jour

with open("cac40.csv", encoding="utf-8") as fichier:
    for ligne in fichier:
        # print(ligne)
        ligneEnCours = ligne.split(";")
        co.append(float(ligneEnCours[2]))
        cc.append(float(ligneEnCours[5]))
        cma.append(float(ligneEnCours[3]))
        cmi.append(float(ligneEnCours[4]))
        dt.append(ligneEnCours[1])

print(len(dt), "jours sont répertoriés dans le fichier.")

iCmaPlusBas = indiceMin(cma)
print("Le cours le plus bas dans la période est", cma[iCmaPlusBas], "le", dt[iCmaPlusBas])
