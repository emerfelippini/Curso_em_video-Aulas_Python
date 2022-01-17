print('\033[1;32mSEPARANDO NÚMERO PARES E ÍMPARES\033[m')
valores = list()
par = list()
ímpar = list()
print('-=' * 30)
while True:
    print('-=' * 30)
    val = int(input('Digite o valor: '))
    valores.append(val)
    if val % 2 == 0:
        par.append(val)
    else:
        ímpar.append(val)
    escolha = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    if escolha not in 'SN':
        print('Escolha inválida.')
        escolha = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    elif escolha == 'N':
        break
    print('-=' * 30)
print('-=' * 30)
print(f'Os número digitados foram: {valores}')
print(f'Os número pares foram: {par}')
print(f'Os número ímpares foram: {ímpar}')
