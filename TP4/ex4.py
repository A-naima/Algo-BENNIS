L = [2,7,5,6,7,1,6,2,1,7,6]
def most_frequent(a):
    e = None
    nbr = 0
    for i in range(len(a)):
        b = a[i]
        c = a.count(b)
        if c > nbr:
            nbr = c
            e = a
    tab = [a,nbr]
    return tab
from collections import counter
count = counter(1)
d,f = count.most_common(1)[0]