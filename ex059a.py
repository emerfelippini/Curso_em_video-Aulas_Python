from time import sleep
print('\033[1;4;32;40m', '-' * 15, 'CALCULADORA', '-' * 15, '\033[m')
print('Digite dois número para efeturar o calculo.')
num1 = float(input('Número 1: '))
num2 = float(input('Número 2: '))
escolha = 0
while escolha != 5:
    print('-' * 30)
    print('\033[1;32m[1] SOMAR\n[2] MULTIPLICAR\n[3] DESCOBRIR NÚMERO MAIOR\n[4] NOVOS NÚMEROS\n[5] SAIR DO PROGRAMA\033[m')
    escolha = int(input('Digite um número para selecionar operação:'))
    print('-' * 30)
    if escolha == 1:
        print('{} + {} = {}'.format(num1, num2, num1 + num2))
    elif escolha == 2:
        print('{} x {} = {}'.format(num1, num2, num1 * num2))
    elif escolha == 3:
        if num1 > num2:
            print('{} é maior que {}'.format(num1, num2))
        elif num1 < num2:
            print('{} é menor que {}'.format(num1, num2))
    elif escolha == 4:
        num1 = float(input('Número 1: '))
        num2 = float(input('Número 2: '))
    elif escolha > 5 or escolha == 0:
        print('Opção inválida.')
print('Finalizando...')
sleep(2)