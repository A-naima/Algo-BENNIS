

b100 = 0
b50 = 0
b10 = 0
deux = 0
un = 0

val = int(input("Entrez la valeur a compter : \n"))

start_input = val

while val != 0:
    for i in range(10):
        if (val - 100) >= 0:
            val = val - 100
            b100 = b100+ 1
        else:
            break
    for x in range(10):
        if (val - 50) >= 0:
            val = val - 50
            b50 = b50 + 1
        else:
            break
    for y in range(10):
        if (val - 10) >= 0:
            val = val -10
            b10 = b10 + 1
        else:
            break
    for z in range(10):
        if (val - 2) >= 0:
            val = val -2
            deux = deux + 1
        else:
            break
    for t in range(10):
        if (val - 1) >= 0:
            val = val -1
            un = un + 1
        else:
            break


print(f"La valeur {start_input} est composée de : \n- {b100} Billets de 100\n- {b50} Billets de 50\n- {b10} Billets de 10\n- {deux} Pièces de 2\n- {un} Pièces de 1\n")