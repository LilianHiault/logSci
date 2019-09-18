def syracuse(n):
    nb = n
#    print(nb)
    i = 1
    while nb > 1:
        if nb % 2 == 0:
            nb /= 2
        else:
            nb = (3 * nb + 1) / 2
        i += 1
#        print(nb)
    return i


max = 0
valN = 10
for n in range(10, 10001):
    if syracuse(n) > max:
        max = syracuse(n)
        valN = n
print(max, valN)
