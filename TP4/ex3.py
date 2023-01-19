nMax = 3
va = []
vb = []
n = int(input(f"Choisir la taille des vecteurs entre (1 et {nMax}"))
while n < 1 or n > nMax:
    n = int(input(f"La taille des vecteurs n'est pas entre (1 et {nMax}"))

for i in range(n):
    va.append(int(input(f"Entrez les composants de va[{i}]")))
    vb.append(int(input(f"Entrez les composants de va[{i}]")))

pro_scalable = 0
for i in range(n):
    pro_scalable += va[i] * vb[i]
print(f"Le produit scalable de va par bv est {pro_scalable}")