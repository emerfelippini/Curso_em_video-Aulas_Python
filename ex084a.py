print('\033[1;32mBANCO DE DADOS\033[m')
lista = list()
dados = list()
quantidade = maior_peso = menor_peso = 0
while True:
    dados.append(str(input('Digite o nome: ')))
    dados.append(float(input('Digite o peso: ')))
    quantidade += 1
    lista.append(dados[:])
    dados.clear()
    escolha = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
    if escolha == 'N':
        break
    while escolha not in 'SN':
        print('Escolha inválida.')
        escolha = str(input('Quer continuar [S/N]: ')).upper().strip()[0]
for pos, cont in enumerate(lista):
    if pos == 0:
        maior_peso = cont[pos][1]
        menor_peso = cont[pos][1]
    if cont[pos][1] > maior_peso:
        maior_peso = cont[pos][1]
    elif cont[pos][1] < menor_peso:
        menor_peso = cont[pos][1]
print(f'Foram cadastradas: {quantidade} pessoas.')
print(f'Tiveram {maior_peso} com o maior peso.')
print(f'Tiveram {menor_peso} com o menor peso.')