import numpy as np
import matplotlib.pyplot as plt


# Functions
def triangle(x, y, c):
    plt . fill([x, x + c, x + c / 2], [y, y, y + c * np.sqrt(3) / 2], " b ")


def t2s(n, x, y, c):
    print("n:", n, " / x:", x, " / y:", y, " / c:", c, sep='')
    if n == 0:
        triangle(x, y, c)
    else:
        t2s(n - 1, x, y, c / 2)
        t2s(n - 1, x + c / 2, y, c / 2)
        t2s(n - 1, x + c / 4, y + ((np.sqrt(3) / 2) / 2**n), c / 2)
        print()
        # Remplacer les /4 et /2 par des /2**n ou /2**n-1 ?


# Main
""""triangle(0, 0, 0.5)
triangle(0.5, 0, 0.5)
triangle(0.25, np.sqrt(3) / 4, 0.5)"""

n = eval(input("Niveau du TdS : "))
x = 0
y = 0
c = 1
t2s(n, x, y, c)

plt.show()
