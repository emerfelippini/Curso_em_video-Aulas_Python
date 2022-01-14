from emoji import emojize
print(emojize(':red_heart: DESCOBRINDO NOMENCLATURA DO TRIÂNGULO :red_heart:'))
x1 = float(input('Digite o primeiro lado do triângulo: '))
x2 = float(input('Digite o segundo lado do triângulo: '))
x3 = float(input('Digite o terceiro lado do triângulo: '))
if x1 < x2 + x3 and x2 < x1 + x3 and x3 < x1 + x2:
    print('Podemos formar um triângulo, que chamamos de ', end='')
    if x1 == x2 == x3:
        print('EQUILÁTERO.')
    elif x1 != x2 != x3 != x1:
        print('ESCALENO.')
    else:
        print('ISOSCÉLES.')
else:
    print('Não podemos formar um triângulo.')


