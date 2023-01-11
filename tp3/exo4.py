n = int(input("Entrez un nombre:"))
x = n
list = []
factorielle = 1

y = input("Boucle (While ou For):")
if y == "While":
    y = 1
    while n>=1:
        factorielle = factorielle * n
        n = n -1

if y == "For":
    factorielle =1
    for y in range (1,n+1):
        factorielle *= y
print(f"La factorielle de {x}, est {factorielle}")