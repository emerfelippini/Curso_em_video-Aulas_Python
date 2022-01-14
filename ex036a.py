print(' FINANCIE SUA CASA AQUI, FAÇA UMA SIMULAÇÃO !!', end='')
print(' Primeito de tudo, digite os seus dados.')
valor_casa = float(input('Digite o valor da casa, há ser feito a simulação: R$'))
salario = float(input('Digite seu salário mensal: R$'))
anos = int(input('Em quantos anos pretende pagar?'))
prestaçao = valor_casa / (anos * 12)
if prestaçao <= salario * 0.30:
    print('Parabêns, seu empréstimo foi aprovado, sua prestação fica no valor de R$ {:.2f} mensais.'.format (prestaçao))
else:
    print('Nos lamentamos, mas seu empréstimo não foi aprovado, pois excedeu o limite de R${:.2f}'.format(prestaçao))






