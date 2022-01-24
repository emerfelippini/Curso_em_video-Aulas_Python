from random import randint
from time import sleep
print('\033[1;32mSORTEIOS DA MEGASENA\033[m')
print('-=' * 30)
lista = list()
jogos = list()
total = 1
escolha = int(input('Quantos jogos você deseja fazer? '))
print('-=' * 30)
while total <= escolha:
    for cont in range (0, 6, +1):
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
    lista.sort()
    jogos.append(lista[:])
    lista.clear()
    total += 1
for pos, cont in enumerate(jogos):
    sleep(1)
    print(f'\033[1;32mO {pos + 1}ª jogo: {cont}\033[m')
    print('-=' * 30)
sleep(14)
print('\033[1;31mBOA SORTE!!!!\033[m')