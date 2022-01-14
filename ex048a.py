soma_imp = 0
cont = 0
for c in range (1, 501, +2):
    if c % 3 == 0:
        soma_imp = soma_imp + c
        cont += 1
print('O somátorio dos número é: {}'.format(soma_imp))
print('A quantidade de número somados foram: {}'.format(cont))