import numpy as np


# Functions
# Question 1
def code_une(lt):
    return ord(lt) - 65


# Question 2
def decode_une(c):
    return chr(c + 65)


# Question 3
def code_mot(m):
    code = []
    for i in m:
        code.append(code_une(i))
    return code


def decode_mot(L):
    for i in L:

    return 0


# Main
# Question 1
mot = input("Entrez un mot à coder : ")
"""print("Code : ")
for i in mot:
    print(code_une(i))

# Question 2
code = eval(input("Code : "))
print("Lettre correspondant à", code, ":", decode_une(code))"""

# Question 3
#motCode = input("Mot codé : ")
print("Mot", mot, "codé :", code_mot(mot))
#print("Mot ", motCode, "décodé :", decode_mot(motCode))
