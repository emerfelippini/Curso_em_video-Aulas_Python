print('\033[1;32mBANCO DE DADOS\033[m')
lista = list()
dados = list()
quantidade = maior_peso = menor_peso = 0
while True:
    print('-=' * 30)
    dados.append(str(input('Digite o nome: ')))
    dados.append(float(input('Digite o peso: ')))
    if len(lista) == 0:
        maior_peso = menor_peso = dados[1]
    else:
        if dados[1] > maior_peso:
            maior_peso = dados[1]
        if dados[1] < menor_peso:
            menor_peso = dados[1]
    quantidade += 1
    lista.append(dados[:])
    dados.clear()
    escolha = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    if escolha == 'N':
        break
    while escolha not in 'SN':
        print('Escolha inválida.')
        escolha = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    print('-=' * 30)
print(f'Foram cadastradas: {quantidade} pessoas.')
print(f'As pessoas mais pesadas tiveram {maior_peso}KG e elas foram:')
for cont in lista:
    if cont[1] == maior_peso: 
        print(f'{cont[0]}', end='...')
print(f'\nAs pessoas mais leves tiveram {menor_peso}KG e elas foram:')
for cont in lista:
    if cont[1] == menor_peso:
        print(f'{cont[0]}', end='...')