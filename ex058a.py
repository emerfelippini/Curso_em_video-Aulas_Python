import emoji, random, timer
print('\033[1;31m', '-' * 20, 'JOGO DA ADIVINHAÇÃO', '-' * 20, '\033[m')
print('Olá sou o computador...\n' 'Acabei de pensar em número de 1 a 10, que tal você tentar adivinhar?')
palpite = int(input('Qual o seu palpite: '))
bot = random.randint(1, 10)
tentativas = 1
while palpite != bot:
    if palpite < bot:
        palpite = int(input('\033[1;31mMais... tente novamente:\033[m'))
        tentativas += 1
    elif palpite > bot:
        palpite = int(input('\033[1;31mMenos... tente novamente:\033[m '))
        tentativas += 1
if palpite == bot:
    print('\033[1;32mParabêns, o número que eu escolhi era {}, e após {} tentativas você acertou.\033[m'.format(bot, tentativas))
