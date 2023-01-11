import random
random_number = random.randint(0, 100)

x= 0

while True:
    y = int(input("Devinez une valeur entre 0 et 100: "))
    x+= 1
    if y == random_number:
        print(f"Félicitations, vous avez deviné la valeur mystère en {x} tours!")
        break
    elif y > random_number:
        print("Le nombre est plus petit")
    else:
        print("Le nombre est plus grand")
