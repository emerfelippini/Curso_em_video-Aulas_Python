import random, emoji, timer
print(emoji.emojize(':red_heart: JO-KEN-PO!! :red_heart:'))
print('Digite algum número para escolher sua opção:\n[0] TESOURA\n[1] PEDRA\n[2] PAPEL' )
opção = int(input('Escolha sua opção: '))
if opção != 0 or 1 or 2:
    print('Jogada inválida')
itens = ('TESOURA', 'PEDRA', 'PAPEL')
bot = random.randint(0, 2)
print('!=' * 10)
print('JO \n''KEN \n''PO!!!')
print('!=' * 10)
print('A escolha do computador foi: {}'.format(itens[bot]))
print('A sua escolha foi: {}'.format(itens[opção]))
if bot == 0 and opção == 0:
    print('Deu empate.')
elif bot == 0 and opção == 1:
    print('Parabêns você venceu.')
elif bot == 0 and opção == 2:
    print('Sinto muito, você perdeu.')
elif bot == 1 and opção == 0:
    print('Sinto muito, você perdeu.')
elif bot == 1 and opção == 1:
    print('Deu empate.')
elif bot == 1 and opção == 2:
    print('Parabêns, você venceu.')
elif bot == 2 and opção == 0:
    print('Parabêns, você venceu.')
elif bot == 2 and opção == 1:
    print('Sinto muito, você perdeu.')
elif bot == 2 and opção == 2:
    print('Deu empate.')

