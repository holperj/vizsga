from naplo import bejegyzes

CBadás:list[bejegyzes] = []
f = open('cb.txt', 'r', encoding= 'utf-8')
f.readline()
for row in f:
    CBadás.append(bejegyzes(row))
f.close()

print('3. feladat: CB-Rádió')
print(f'3.2 feladat: Bejegyzések száma: {len(CBadás)} db')

db = 0
for item in CBadás:
    if item.nev == "Sanyi":
        db += 1

print(f'3.3 feladat: Sanyihoz tartozó bejegyzések: {db} db')

most = []
max = 0
for item in CBadás:
    if item.db > max:
        max = item.db
for item in CBadás:
    if item.db == max:
        most.append(item)

print('3.4 feladat: A legtöbb adás:')
db = 0
for item in most:
    print(f'\tIdő: {most[db].ora}:{most[db].perc} Darab: {most[db].db} Név: {most[db].nev}')
    db += 1

f = open('cb2.txt', 'w', encoding= 'utf-8')
f.write('Kezdes;Nev;Adasdb\n')
for item in CBadás:
    f.write(f'{item.ido_percben};{item.nev};{item.db}\n')
f.close()