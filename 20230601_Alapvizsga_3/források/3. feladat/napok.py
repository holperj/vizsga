napok = ['hétfő', 'kedd', 'szerda', 'csütörtök', 'péntek']

def maganh_szam(szo):
    db = 0
    maganh = ['a','á','e','é','i','í','o','ó','ö','ő','u','ú','ü','ű']
    for betu in szo:
        if betu in maganh:
            db += 1
    return db
legtobb = 0
legtobb_nap = ''
for item in napok:
    db = maganh_szam(item)
    if db > legtobb:
        legtobb = db
        legtobb_nap = item

print(f'A legtöbb magánhangzó a {legtobb_nap}-ben van')

