from time import sleep
print('\033[1;31m PROGRESSÃO ARITMÉTICA \033[m')
print('=-' * 20)
primeiro_termo = int(input('Primeiro termo: '))
razão = int(input('Razão: '))
contador = 0
mais = 1
total = 0
while mais != 0:
    while contador < 10:
        print('{}'.format(primeiro_termo), end='')
        print(' -> ' if contador < 9 else '', end='')
        contador += 1
        primeiro_termo += razão
    mais = int(input('\nQuantos número você quer acrescentar: '))
    contador -= mais
print('Fim do programa, aguarde...')
sleep(2)