titi = input("Entre une lettre :")
titi = titi.lower()
titi_lol = ""


for c in titi:
    if titi.isalpha():
        titi_lol += c

if titi_lol == titi_lol [::-1]:
    print("C'est un palindrome")
else:
    print("Ce n'est pas un palindrome")
