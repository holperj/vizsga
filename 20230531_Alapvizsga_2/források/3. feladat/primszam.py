from random import randint

szamok = []

for i in range(10):
    random = randint(10, 100)
    szamok.append(random)

def prim(szam):
    osztok = []
    for oszto in range(1, szam):
        if szam % oszto == 0:
            osztok.append(oszto)
    if len(osztok) == 2:
        return True
    else:
        return False

print(szamok)
for item in szamok:
    if prim(item) == True:
        print('Van prím szám a listában!')
        break
else:
        print('Nincs prím szám a listában!')

