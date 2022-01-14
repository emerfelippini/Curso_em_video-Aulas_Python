from random import randint
print('\033[1;32m SORTEIO DE NÚMERO\033[m')
num = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
maior = menor = pos = 0
print('Os número sorteados foram:')
for cont in num:
    print(f'{cont}', end=' ')
    if pos == 0:
        maior = cont
        menor = cont
    elif cont >= maior:
        maior = cont
    elif cont <= menor:
        menor = cont
    pos =+ 1
#print(f'\nO menor valor foi {menor}')
#print(f'O maior valor foi {maior}')
print(f'\nO maior valor sorteador foi {max(num)}')
print(f'O menor valor sorteado foi {min(num)}')