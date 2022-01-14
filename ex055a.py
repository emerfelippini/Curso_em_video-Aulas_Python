print('\033[1;32m', ' ' * 20, 'DESCOBRINDO O MAIOR E O MENOR PESO', ' ' * 20, '\033[m')
maior = 0
menor = 0
for c in range(1, 6, +1):
    peso = float(input('Digite o {}ª peso: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso foi de {}KG.'.format(maior))
print('O menor peso foi de {}KG'.format(menor))