from calendar import firstweekday
from random import randint
from operator import itemgetter
from time import sleep
jogadores = dict()
ranking = list()
jogadores['jogador01'] = randint(1, 6)
jogadores['jogador02'] = randint(1, 6)
jogadores['jogador03'] = randint(1, 6)
jogadores['jogador04'] = randint(1, 6)
for k, v in jogadores.items():
    print(f'O {k} tirou o número {v}')
    sleep(1)
ranking = sorted(jogadores.items(), key = itemgetter(1), reverse = True)
print('-=' * 30)
sleep(1)
for pos, cont in enumerate(ranking):
    if pos == 0:
        print(f'\033[1;32mEm {pos + 1}ª lugar ficou o {cont[0]}, parabêns.\033[m')
    elif pos == 3:
        print(f'\033[1;31mEm {pos + 1}ª lugar ficou o {cont[0]}, sinto muito.\033[m')
    else:
        print(f'Em {pos + 1}ª lugar ficou o {cont[0]}.')
    sleep(2)
