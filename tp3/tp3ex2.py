import numpy as np


# Functions
# Question 1
def cesar(mot, dec):
    motCrypt = ""
    for c in mot:
        motCrypt += chr((ord(c) - 65 + dec) % 26 + 65)
    return motCrypt

# Question 2
def deCesar(motCrypt, dec):
    mot = ""
    for c in motCrypt:
        mot += chr((ord(c) - 65 - dec) % 26 + 65)
    return mot


# Main
# Question 1
"""mot = input("Mot à crypter : ")
dec = eval(input("Décalage : "))
print("Cryptage de César du mot", mot, "avec le décalage", dec, ":", cesar(mot, dec))"""

# Question 2
"""motCrypt = input("Mot à décrypter : ")
decCrypt = eval(input("Décalage : "))
print("Décryptage de César du mot", motCrypt, "avec le décalage", decCrypt, ":", deCesar(motCrypt, decCrypt))"""

# Question 3
phrase = ["CE", "MESSAGE", "EST", "CONFIDENTIEL"]
dec = eval(input("Décalage : "))
for i in phrase:
    
