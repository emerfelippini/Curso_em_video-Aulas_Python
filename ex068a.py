import random
import timer
print('\033[1;31m JOGO DO PAR OU ÍMPAR\033[m')
vit = 0
while True:
    escolha = str(input('Escolha par ou impar: ')).upper().strip()[0]
    while escolha not in 'PpIi':
        print('Escolha Inválida')
        escolha = str(input('Escolha par ou impar: ')).upper().strip()[0]
    bot = random.randint(1, 10)
    num = int(input('\033[1;32mQue número de 1 a 10 você vai jogar: '))
    print(f'O computador escolheu {bot}\033[m')
    soma = num + bot
    if escolha == 'P' and soma % 2 == 0:
        print('Parabêns você venceu.')
        vit += 1
    elif escolha == 'I' and soma % 2 != 0:
        print('Parabêns você venceu.')
        vit += 1
    else:
        print('Sinto muito, você perdeu.')
        break
print(f'Você ganhou {vit} vezes.')
print('\033[1;31mGAME OVER\033[m')