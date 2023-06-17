from nyertesek import eredmeny

Fogadasi_fordulo:list[eredmeny] = []
f = open('toto.txt', 'r', encoding='utf-8')
f.readline()
for row in f:
    Fogadasi_fordulo.append(eredmeny(row))
f.close

print('3. feladat: Toto')
print('3.1 feladat: Adatok beolvasása és tárolása')
print(f'3.2 feladat: Fogadási fordulók száma: {len(Fogadasi_fordulo)}')

db = 0
for item in Fogadasi_fordulo:
    db += item.db

print(f'3.3 feladat: Telitalálatos szelvéynek száma: {db} darab')

for item in Fogadasi_fordulo:
    if 'X' not in item.eredmeny:
        print('3.4 feladat: Volt döntetlen mentes forduló4')
        break
else:
    print('3.4 feladat: Nem volt döntetlen mentes forduló4')

stat = {}
for item in Fogadasi_fordulo:
    if item.ev in stat.keys():
        stat[item.ev] += item.db
    else:
        stat[item.ev] = item.db

print('Évenkénti nyertesek száma:')
for key, value in stat.items():
    print(f'{key} - {value} db')

stat2 = {}
for item in Fogadasi_fordulo:
    if item.ev in stat2.keys():
        stat2[item.ev] += item.nyeremeny
    else:
        stat2[item.ev] = item.nyeremeny

print('Évenkénti nyeremény száma:')
for key, value in stat2.items():
    print(f'{key} - {value} Ft')
