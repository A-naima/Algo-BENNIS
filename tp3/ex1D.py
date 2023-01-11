a = int(input("Entrez une valeur supérieur à 1:"))
b = 0
somme = 0

while somme <= a:
    b += 1
    somme += b

b -= 1
print(f"Le plus grand nombre N tel que la somme des entiers de 0 à N soit inférieure ou égale à {a} est {b}")
