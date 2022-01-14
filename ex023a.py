#frase = input('Digite um número de 0 a 9999: ')
#print('A unidade é {}'.format(frase[3]))
#print('A dezena é {}'.format(frase[2]))
#print('A centena é {}'.format(frase[1]))
#print('A milhar é {}'.format(frase[0]))
num = int(input('Digite um número: '))
print('Analisando seu número ...')
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('A unidade é {} '.format(u))
print('A dezena é {}'.format(d))
print('A centena é {}'.format(c))
print('O milhar é {}'.format(m))