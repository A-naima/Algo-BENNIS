binome = ('l1', 'l2')


print(binome)

new = str(input ("Entrez le nouveau login souhaitéln"))

binome = list (binome)

binome [1] = new

binome = tuple(binome)

print(binome)

newL = str(input("Entrez le nouveau login a ajouter : \n"))

binome = list (binome)

binome.append(newL)

binome = tuple(binome)

print(binome)