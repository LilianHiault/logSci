# Défi Turing 65


def derDigit(nb):
    return int(str(nb)[-1])


somme = 0
prod = 1
for i in range(2014):
    nb = i
    prod = 1
    while nb != 0:  # On mutliplie par le dernier chiffre puis on divise par 10 jusqu'à ce que le nombre soit 0
        prod *= derDigit(nb)
        nb //= 10
    if (i + prod) == 2014:
        somme += i
        # print(i)

print("La somme des nombres qui donnent 2014 lorsqu'on leur ajoute le produit de leurs chiffres est : ", somme)
