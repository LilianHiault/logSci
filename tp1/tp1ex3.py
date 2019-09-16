import numpy as np


def nombreDeChiffres(x):
    return int(np.log10(x) + 1)


print("Pi au carré vaut ", np.sin(np.pi ** 2))
print("Log néperien de 2021 : ", np.log(2021))
x = 1001
print("Log10 de ", x, " : ", np.log10(x))

print(x, " a ", nombreDeChiffres(x), " chiffres.")

print("2**64 - 1 a ", nombreDeChiffres(2**64 - 1), " chiffres.")

# log(a^b) = b log(a)
print("123**234 a ", int(234 * np.log10(123) + 1), " chiffres.")
