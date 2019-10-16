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


# Question 4
def cesar_plus(p, dec):
    phraseCrypt = ""
    listePhrase = p.split(" ")
    for mot in listePhrase:
        phraseCrypt = phraseCrypt + cesar(mot, dec) + " "
    return phraseCrypt


def decesar_plus(p,dec):
    phrase = ""
    listePhraseCrypt = p.split(" ")
    for mot in listePhraseCrypt:
        phrase = phrase + deCesar(mot, dec) + " "
    return phrase


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
"""phrase = ["CE", "MESSAGE", "EST", "CONFIDENTIEL"]
dec = eval(input("Décalage : "))
print(phrase, "décryptée :")
for mot in phrase:
    print(deCesar[mot])"""

# Question 4 et 5
#dec = eval(input("Dec = "))
for dec in range(0, 27):
    phrase1 = "KYV RIK FW GIFXIRDDZEX ZJ KYV RIK FW FIXREZQZEX TFDGCVOZKP"
    print("Décryptée 1 :", decesar_plus(phrase1, dec))
    phrase2 = "BG FTMAXFTMBVL RHN WHGM NGWXKLMTGW MABGZL RHN CNLM ZXM NLXW MH MAXF"
    print("Décryptée 2 :", decesar_plus(phrase2, dec))
    print("\n")
