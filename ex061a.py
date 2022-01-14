print('\033[1;32mProgressão Airtmética\033[m')
print('-' * 20)
primeiro_termo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
contador = 0
while contador < 10:
    print('{}'.format(primeiro_termo), end='')
    print(' -> ' if contador < 9 else '', end='')
    primeiro_termo += razão
    contador += 1
