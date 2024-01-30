import math
#
# prim = False
# n = 9999
# while (not prim):
#     n += n
#     i = 2
#     while(i<=math.sqrt(n) and n % i is not 0):
#         i += i
#     prim = i > math.sqrt(n)
#     return n

def osztok(szam):
    lista = []
    oszto = 2
    while oszto <= math.sqrt(szam):
        if szam % oszto == 0:
            lista.append(oszto)
        oszto += 1
    return lista

print(osztok(10001))

def osztok(szam):
    lista = []
    oszto = 2
    while oszto in range(2, round(math.sqrt(szam)+1)):
        if szam % oszto == 0:
            lista.append(oszto)
        oszto += 1
    return lista

def masodik(szam):
    prim = False
    n = 9999
    while not prim:
        n = n+1
        i = 2
        while i < math.sqrt(n) && n % i != 0):
            i = i+1
        prim = i > math.sqrt(n)
    return i

def linearis():
    int also = 42
    int felso = 67
    while i <= felso && ! (i%10==0)
        i += i
    bool van = i <= felso
    if van = true:
        print("van 0-e végződő szám: " + i)
    else:
        print("nincs 0-ra végződő")
