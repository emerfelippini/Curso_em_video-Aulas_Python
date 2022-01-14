'''from math import sqrt
cato = float(input('Digite o comprimento do cateto oposto:'))
cata = float(input('Digite o comprimento do cateto adjacente: '))
hipo = (cato ** 2 + cata ** 2) ** (1/2)
print('Sendo o cateto oposto {} e o cateto adjacente {}, logo a hipotenusa é {:.2f}.'.format(cato, cata, hipo))'''
from math import hypot
cato = float(input('Qual o comprimento do cateto oposto? '))
cata = float(input('Qual o comprimento do cateto adjacente? '))
print('Segundo os dados digitados, a hipotenusa mede {:.2f}'.format(hypot(cato, cata)))

