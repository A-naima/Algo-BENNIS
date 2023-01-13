n1 = str(input("Entrez votre nom : "))
p1 = str(input("Entrez votre prénom : "))
n2 = str(input("Entrez le deuxième nom : "))
p2 = str(input("Entrez le deuxième prénom : "))
n1.upper().isupper()
print(f"Le nom et prénom de la première personne est {n1} {p1}.")
print(f"Le nom et prénom de la deuxième personne est {n2} {p2}.")

if n1 < n2:
    print("cas1")
    print(p2.capitalize())