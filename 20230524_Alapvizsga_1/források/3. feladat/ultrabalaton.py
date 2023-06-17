from fut import futo

eredmeny:list[futo] = []
f = open('ub2017egyeni.txt', 'r', encoding= 'utf-8')
f.readline()
for row in f:
    eredmeny.append(futo(row))
f.close()

print(f'3.2 feladat: Futók száma: {len(eredmeny)}')
noi = 0
for item in eredmeny:
    if item.kategoria == 'Noi'and item.tavszazalek == 100:
        noi += 1

print(f'3.3 feladat: Célba érkező női sportolók {noi} fő')

longest = 0
longest_name = ''
for item in eredmeny:
    hossz = int(len(item.name))
    if longest < hossz:
        longest = hossz
        longest_name = item

print('3.4 feladat: A elghpsszabb nevű futó')
print(f'\t Név: {longest_name.name}')
print(f'\t Rajszám: {longest_name.rajtszam}')
print(f'\t Eredmény: {longest_name.ido}')

db = 0
ossz = 0
for item in eredmeny:
    if item.kategoria == 'Ferfi' and item.tavszazalek == 100:
        ossz += item.IdőÓrában()
        db += 1
atlag = ossz / db

print(f'7. feladat: A férfi vesenyzők átlagos ideje: {atlag} óra')
