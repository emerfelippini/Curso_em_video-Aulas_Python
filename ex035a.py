x1 = float(input('Comprimento do primeiro segmento:'))
x2 = float(input('Comprimento do segundo segmento: '))
x3 = float(input('Comprimento do terceiro segmento: '))
# calculando primeiro segmento:
if x1 < x2 + x3 and x2 < x1 + x3 or x3 < x1 + x2:
    print('Podemos formar um triângulo')
else:
    print('Não podemos formar um triângulo')
