print('\033[1;32mCRIANDO UMA MATRIZ\033[m')
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for linha in range (0, 3, +1):
    for coluna in range (0, 3, +1):
        matriz[linha][coluna] = int(input(f'Na posição {linha}x{coluna}: '))
for linha in range (0, 3, +1):
    for coluna in range (0, 3, +1):
        print(f'[{matriz[linha][coluna]:^5}]', end='')
    print()