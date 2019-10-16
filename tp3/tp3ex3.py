import numpy as np


# Functions
# Question 2
def affine(mot, a, b):
    motCrypt = ""
    for c in mot:
        motCrypt += chr(((a * (ord(c) - 65)+b) % 26) + 65)
    return motCrypt


# Question 3
def inverse(a):



# Main
# Question 1
for a in range(0, 26):
    if np.gcd(a, 26) == 1:
        print(a, "est premier avec 26")

# Question 2
print("Exemple de cryptage :", affine("SALUT", 3, 5))

## print("Hello world!", sep = '', end = '')
