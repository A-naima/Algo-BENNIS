def table_multi(n):
    tab = []
    for i in range(1,10):
        resultat = n*i
        tab.append(f"{n} * {i} = {round(resultat, 2)}")
    print(f"Voici la table de multiplication {n}")
    for i in range(0,9):
          print(tab[i])
nbr = float(input("Entre un nombre:"))

table_multi(nbr)