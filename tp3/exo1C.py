a=0
b=0
c=0
for i in range(10):
    while True:
        x=float(input("Entrez une valeur comprise entre 0 et 20 :"))
        if 0 <= x <= 20:
            break
        else:
            print("La valeur entrée n'est pas comprise entre 0 et 20, entrez une autre valeur :")
    if x <10:
                a+= 1
    elif x <15:
        b+= 1
else:
    c+=1
print(f"Nombre de valeurs inférieures strictement à 10: {a}")
print(f"Nombre de valeurs supérieures ou égales à 10 et strictement inférieures à 15: {b}")
print(f"Nombre de valeurs supérieures ou égales à 15: {c}")


