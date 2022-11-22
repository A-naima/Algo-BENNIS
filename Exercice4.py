base = 4
fromage = 800.0
eau = 2
ail = 2
pain = 400

a = int(input("Nombre de convives"))
fromage1 = fromage * a / base
eau1 = eau * a / base
ail1 = ail * a / base
pain1 = pain * a / base
print(f"Entrez le nombre de perssonne(s) conviées à la fondue :{a}")
print(f"Pour faire une fondue fribourgeoise pour ({a}) personnes, il vous faut :")
print(f"({fromage1}) gr de fromage")
print(f"({eau1}) dl d'eau")
print(f"({ail1}) gousse d'ai")
print(f"({pain1}) gr de pain")