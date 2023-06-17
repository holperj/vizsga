import math
print('1. feladat: Háromszög kerülete és területe')
print('Kérem a háromszög oldalait')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
k = a + b + c
s = k / 2
t = math.sqrt(s*(s-a)*(s-b)*(s-c))
print(f'K = {k}')
print(f'T = {t}')