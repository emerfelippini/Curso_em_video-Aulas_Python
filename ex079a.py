from time import sleep
valores = list()
while True:
    print('-=' * 30)
    val = int(input('Digite o valor: '))
    if val not in valores:
            valores.append(val)
    else:
        print('O valor digitado já está na lista.')
    escolha = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
    while escolha not in 'SsNn':
        print('Escolha errada.')
        escolha = str(input('Quer continuar [S/N]: '))
    if escolha in 'Nn':
        print('Analisando dados....')
        sleep(3)
        break
    print('-=' * 30)
print(f'Os número escolhidos foram: {sorted(valores)}')