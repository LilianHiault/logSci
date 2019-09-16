a = 10
b = 12
if 1 >= b:
    print("a est plus grand.")
    print("J'ai vérifié !")
else:
    print("b est plus grand.")
    print("b est vraiment plus grand.")
print("Ceci s'affiche toujours.")

a = 10
if a >= 9 and a <= 11:
    print("a est dans l'intervalle [9; 11].")

a = 0
if ( a >= -1 and a < 0) or (a >= 3 and a <= 4):
    print("a appartient à l'intervalle [-1, 0[ U [3,4]")
