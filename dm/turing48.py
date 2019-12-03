# Défi Turing 48

somme = 0
for i in range(1, 2014):
    somme += i**i
print("Les 10 premiers chiffres de la somme de 1¹ + 2² + ... + 2013²⁰¹³ sont : ",
      int(str(somme)[:10]))
