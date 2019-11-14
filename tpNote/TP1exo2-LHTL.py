import numpy as np
import matplotlib.pyplot as plt
import sympy as sm


# Lilian HIAULT et Tom LHÔPITAL


# Fonctions

def liseq(n):
# retourne les cent premières valeurs de la suite
    u_0 = 1 / np.pi
    cpval = [u_0]
    temp = 0
    for i in range(1, 100):
        temp = 22 * cpval[i - 1] * (1 - cpval[i - 1])
        cpval.append(temp - np.floor(temp))
    return cpval

def exaseq(n):
# retourne les cent premières valeurs de la suite avec un précision de 1000 décimales
    u_0 = sm.Float(1 / np.pi)
    cpval = [u_0]
    temp = sm.Float(0)
    for i in range(1, 100):
        temp = (22 * cpval[i - 1] * (1 - cpval[i - 1])).evalf(1000)
        cpval.append(temp - sm.floor(temp))
    return cpval

# Main

# 1
print("1. On constate que la suite converge vers 0.5.")
plt.plot(liseq(1), label = "Q1", color = "b")
plt.plot(exaseq(1), label = "Q2", color = "g")
plt.title("100 premières valeurs de la suite")
plt.legend(loc = 0)
plt.show