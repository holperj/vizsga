from random import randint

def halmaz(szamok):
    volt = []
    for item in szamok:
        if item in volt:
            return False
        else:
            volt.append(item)
    else:
        return True

print('2. feladat: Halmaz-e?')
for i in range(8): 
    szamok = []
    for l in range(5):
        szamok.append(randint(1, 9))
    if halmaz(szamok) == True:
        print(f'{i + 1}. {szamok} -> Halmaznak tekinthető')
    else:
        print(f'{i + 1}. {szamok} -> Halmaznak nem tekinthető')