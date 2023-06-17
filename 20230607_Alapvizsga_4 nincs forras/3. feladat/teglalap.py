print('1. feladat: Tégallap kerülete és területe')

for i in range(10):
    print(f'Adja meg a(z) {i+1}. téglalap oldalait!')
    try:    
        a = float(input('a = '))
        b = float(input('b = '))

        t = a * b
        k = 2*(a + b)

        print(f'T = {t}')
        print(f'K = {k}')
    except:
        print('Nem mefelelő adat')