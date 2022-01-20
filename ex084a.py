print('\033[1;32mBANCO DE DADOS\033[m')
lista = list()
dados = list()
quantidade = maior_peso = menor_peso = 0
while True:
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
print(f'Foram cadastradas: {quantidade} pessoas.')
print(f'O maior peso foi de {maior_peso}KG, e foram cadastradas {} pessoas com esse peso.')
print(f'O menor peso foi de {menor_peso}KG, e foram cadastradas {} pessoas com esse peso.')