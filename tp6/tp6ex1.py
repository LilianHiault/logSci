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
acc = []  # Accroissements journaliers
accpos = 0  # Accroissements journaliers positifs
accneg = 0  # Accroissements journaliers négatifs
accroi = 0

# Ouverture et lecture
with open("cac40.csv", encoding="utf-8") as fichier:
    for ligne in fichier:
        # print(ligne)
        ligneCour = ligne.split(";")
        co.append(float(ligneCour[2]))
        cc.append(float(ligneCour[5]))
        cma.append(float(ligneCour[3]))
        cmi.append(float(ligneCour[4]))
        dt.append(ligneCour[1])
        accroi = float(ligneCour[2]) - float(ligneCour[5])
        acc.append(accroi)
        if accroi >= 0:
            accpos += accroi
        else:
            accneg -= accroi

# Nombre de jours
print(len(dt), "jours sont répertoriés dans le fichier.")

# Cours le plus bas
iCmaPlusBas = indiceMin(cma)
print("Le cours le plus bas dans la période est",
      cma[iCmaPlusBas], "le", dt[iCmaPlusBas])

# Accroissements journaliers
print("Total accroissements journaliers :", totalAcc(acc))

# plt.plot(acc)
plt.bar(0.5, accpos, 1, color='r', label='Accroissement positif', alpha=0.5)
plt.bar(2.5, accneg, 1, color='b', label='Accroissement négatif', alpha=0.5)
plt.title('Accroissement total')
plt.legend(loc=0)
plt.show()
