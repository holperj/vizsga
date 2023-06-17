def perfect(szam):
    osztok = []
    osszeg = 0
    for oszto in range(1, szam):
        if szam % oszto == 0:
            osztok.append(oszto)
    for oszto in osztok:
        osszeg += oszto
    if szam == osszeg:
        return True
    else:
        return False

print('2. feladat: Tökéletes számok')
print('Kérek két természetes számot:')
tol = int(input('tól = '))
ig = int(input('ig = '))

print(f'Tökéltetes számok {tol} és {ig} között:')
tokeletes = []
for szam in range(tol, ig):
    eredmeny = perfect(szam)
    if eredmeny == True:
        tokeletes.append(szam)
    else:
        pass

if len(tokeletes) != 0:
    for szam in tokeletes:
        if szam != tokeletes[-1]:
            print(f'{szam}; ', end = '')
        else:
            print(szam)
else:
    print('A megadott tartományban nincsen tökéletes szám!')