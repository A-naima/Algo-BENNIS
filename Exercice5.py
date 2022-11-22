x = int(input("Entrez un nombre entier:"))
if x > 0:
    msg="Le nombre est positif"
    if x % 2 == 0:
       msg+= "et pair"
    else:
        msg += "et impair"
elif x < 0:
    msg="Le nombre est negatif."
    if x % 2 == 0:
       msg+= "et pair"
    else:
        msg += "et impair"
else:
     msg="Le zero est positif et pair."

print(f"Le nombre est {msg}")
