import numpy as np
import matplotlib.pyplot as plt
import sympy as sm


# Lilian HIAULT et Tom LHÔPITAL


# Fonctions
 
def mindiv(n):
# retourne le plus petit entier k qui divise n
    if n >= 2:
        k = 2
        while (n % k != 0):
            k += 1
        return k
    
def dec_prem_loop(n):
    reste = n / mindiv(n)
    divprem = [mindiv(n)]
    while reste > 1:
        divprem.append(mindiv(reste))
        reste = reste / mindiv(reste)
    return divprem
    
def dec_prem_rec(n):
    if reste < 2:
        return 
    else:
        return

# Main

# 1
n = eval(input("n : "))
print("1.\nPlus petit diviseur de", n, ":", mindiv(n))

# 2
print("\n2.\nListe des diviseurs premiers de n avec multiplicité (fonction avec boucle):", dec_prem_loop(n))

print("Liste des diviseurs premiers de n avec multiplicité (fonction récursive):", dec_prem_rec(n))
#200376