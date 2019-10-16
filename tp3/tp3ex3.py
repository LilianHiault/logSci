import numpy as np


# Functions
# Question 2
def affine(mot, a, b):
    motCrypt = ""
    for c in mot:
        motCrypt += chr(((a * (ord(c) - 65) + b) % 26) + 65)
    return motCrypt


# Question 3
def inverse(a):
    inv = -1
    for i in range(0,26):
        if (i * a) % 26 == 1:
            inv = i
    return inv


# Question 4
def de_affine(mot, a, b):
    motDec = ""
    for c in mot:
        motDec += chr(((ord(c) - 65 - b)) * inverse(a) % 26 + 65)
    return motDec


# Main
# Question 1
ensA = []
for a in range(0, 26):
    if np.gcd(a, 26) == 1:
        #print(a, "est premier avec 26")
        ensA.append(a)

print("Ensemble des a premiers avec 26 :", ensA, '\n')

# Question 2
#print("Exemple de cryptage :", affine("SALUT", 3, 5))

# Question 3
"""if inverse(a) == -1:
    print("xx' n'est pas inversible modulo 26")
else:
    print("L'inverse de a modulo 26 est :", inverse(a))"""

# Questions 4 et 5

"""mot = input("Mot : ")
a = eval(input("a : "))
b = eval(input("b : "))
motCrypt = affine(mot, a, b)
print(mot, "crypté :", motCrypt)
print(motCrypt, "déchiffré est :", de_affine(motCrypt, a, b))"""

# Question 6
motCode = "KYBIX"

for a in ensA:
    for b in range(11):
        print(motCode, "décodé :", de_affine(motCode, a, b))
    print("")

# print("Hello world!", sep = '', end = '')
