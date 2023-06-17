from building import epulet

Épület:list[epulet] = []
f = open('legmagasabb.txt', 'r', encoding='utf-8')
f.readline()
for row in f:
    Épület.append(epulet(row))
f.close

print(f'3.2 feladat: Épületek száma: {len(Épület)} db')

szum = 0
for item in Épület:
    szum += item.floor

print(f'3.3 feladat: Emeletek összege: {szum}')

max = 0
max_item = ''
for item in Épület:
    if item.height > max:
        max = item.height
        max_item = item
    
print('3.4 feladat: A legmagasabb épület adatai')
print(f'\tNév: {max_item.nev}')
print(f'\tVáros: {max_item.orszag}')
print(f'\tMagasság: {max_item.height} m')
print(f'\tEmeletek száma: {max_item.floor}')
print(f'\tÉpítés éve: {max_item.year}')

for item in Épület:
    if item.orszag == 'Olaszország':
        print('Van olasz épület az adatok között!')
        break
else:
    print('Nincs olasz épület az adatok között!')

stat = {}

for item in Épület:
    if item.orszag in stat.keys():
        stat[item.orszag] += 1
    else:
        stat[item.orszag] = 1

print('Épületek száma országonként:')
for key, value in stat.items():
    print(f'\t{key}: {value}')