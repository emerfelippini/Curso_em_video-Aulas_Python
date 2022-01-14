while True:
    num = int(input('Digite um número [0 para sair]: '))
    if num == 0:
        break
    for cont in range (1, 11, +1):
        print(f'\033[1;32m{num} x {cont} = {num * cont}\033[m')
print('Programa finalizado')