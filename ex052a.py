print('\033[1;32m', ' ' * 15, 'DESCOBRINDO SE O NÚMERO É PRIMO OU NÃO', ' ' * 15, '\033[m')
num = int(input('Digite o número a ser analisado: '))
cont = 0
for c in range (1, num + 1, +1):
    if num % c == 0:
        print('\033[1;32m {} \033[m'.format(c), end=' ')
        cont += 1
    else:
        print('\033[1;31m {} \033[m'.format(c), end=' ')
if cont == 2:
    print('\n\033[1;32m O número é divisel por {} número(s) e ele é um número primo. \033[m'.format(cont))
else:
    print('\n\033[1;31m O número é divisel por {} número(s) e ele não é um número primo \033[m'.format(cont))

