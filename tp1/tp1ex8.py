def div35(n):
    i = n - 1
    somme = 0
    while i >= 0:
        if (i % 3 == 0) or (i % 5 == 0):
            print(i)
            somme += i
        i -= 1
    return somme


print(div35(10))
