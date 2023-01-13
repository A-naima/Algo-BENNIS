n = input("Veuillez entrer la note du module 1 et le coefficient correspondant :")
a = n.split(" ")
b = int(a[0])
c = int(a[1])
x = b*c
print(f"La note est {b} et le coefficient {c} ")


n1 = input("Veuillez entrer la note du module 1 et le coefficient correspondant :")
a1 = n1.split(" ")
b1 = int(a1[0])
c1 = int(a1[1])
x1 = b1*c1
print(f"La note est {b1} et le coefficient {c1} ")


n2 = input("Veuillez entrer la note du module 1 et le coefficient correspondant :")
a2 = n2.split(" ")
b2 = int(a2[0])
c2 = int(a2[1])
x2 = b2*c2
print(f"La note est {b2} et le coefficient {c2} ")


n3 = input("Veuillez entrer la note du module 1 et le coefficient correspondant :")
a3 = n3.split(" ")
b3 = int(a3[0])
c3 = int(a3[1])
x3 = b3*c3
print(f"La note est {b3} et le coefficient {c3} ")


n4 = input("Veuillez entrer la note du module 1 et le coefficient correspondant :")
a4 = n4.split(" ")
b4 = int(a4[0])
c4 =int(a4[1])
x4 = b4*c4
print(f"La note est {b4} et le coefficient {c4} ")

m = x+x1+x2+x3+x4
s = c+c1+c2+c3+c4
mc = m / s
print(f"La moyenne est donc :{mc}")

if b<8 or b1<8 or b2 <8 or b3<8 or b4 <8:
    print("Non admis")
    exit()

if mc>10:
    print("Admis")

else :
    print("Non admis")