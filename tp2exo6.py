from random import *

x=randint(0, 100)
print(f"{x}")
if x < 50:
    msg="Pile !"
else:
    msg ="Face !"
print(f"{msg}")