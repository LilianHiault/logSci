def carrePlus(n):
    b = n**2 + 2
    return b
    print("Ceci ne s'affichera pas !")


print(carrePlus(345) + carrePlus(567))


def racines(a, b, c):
    if b**2 - 4 * a * c < 0:
        return 0
    elif b**2 - 4 * a * c == 0:
        return 1
    else:
        return 2


print(racines(1, 1, -2))
print(racines(4, -12, 9))
print(racines(2, 1, 1))
