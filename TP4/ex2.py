nbr =int(input("Donnez le nombre d'étudiant :"))
t = 0
note = []
for i in range(nbr):
    n = float(input(f"Note de l'étudiant {i+1}:"))
    note.append(n)
    t +=n
    clas = t / nbr
print(f"Moyenne de classe:{clas}")
print(f"Numéro de l'étudiant | note | écart à la moyenne")
for i in range(nbr):
    n = note[i]
    ecart = note[i]-clas
print(f"{i+1}|{n}|{ecart}")