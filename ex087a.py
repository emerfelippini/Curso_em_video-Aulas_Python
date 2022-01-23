print('\033[1;32mTRABALHANDO COM MATRIZES\033[m')
soma_pares = soma_valores = maior = 0
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range (0, 3, +1):
    for coluna in range(0, 3, +1):
        matriz[linha][coluna] = int(input(f'Digite o valor na posição {linha}x{coluna}: '))
print('-=' * 30)
print('As posições ficaram:')
for linha in range(0, 3, +1):
    for coluna in range(0, 3, +1):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()
print('-=' * 30)
for cont in matriz[0]:
    if cont % 2 == 0:
        soma_pares += cont
for pos, cont in enumerate(matriz[1]):
    if pos == 0:
        maior = cont
    if cont > maior:
        maior = cont
    if cont % 2 == 0:
        soma_pares += cont
for cont in matriz[2]:
    if cont % 2 == 0:
        soma_pares += cont
for l in range(0, 3, +1):
    soma_valores += matriz[l][2]
print(f'A soma dos números pares: {soma_pares}')
print(f'A soma dos valores da 3ª coluna: {soma_valores}')
print(f'O maior número da segunda linha: {maior}')