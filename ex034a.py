sal = float(input('Quanto você ganha? R$'))
print('Analisando seu salário...')
if sal < 1250:
    x1 = ( sal * 0.15 ) + sal
else:
    x1 = ( sal * 0.10 ) + sal
print('Com o aumento, o seu salário fica de R${:.2f}'.format(x1))