print('ANALISANDO DADOS')
pessoas = dict()
lista = list()
media = soma = 0
print('-=' * 50)
while True:
    pessoas.clear()
    pessoas['nome'] = str(input('Nome: '))
    pessoas['sexo'] = str(input('Sexo [M/F]: ')).upper().strip()[0]
    while pessoas['sexo'] not in 'MF':
        print('Erro, digite apenas M ou F.')
        pessoas['sexo'] = str(input('Sexo: ')).upper().strip()[0]
    pessoas['idade'] = int(input('Idade: '))
    soma += pessoas['idade']
    escolha = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    lista.append(pessoas.copy())
    while escolha not in 'SN':
        print('Erro, digite apenas [S] para sim ou [N] para não.')
        escolha = str(input('Deseja continuar [S/N]: ')).upper().strip()[0]
    if escolha == 'N':
        break
    print('-=' * 50)
media = soma / len(lista)
print('-=' * 50)
print(f'A => Foram cadastradas {len(lista)} pessoas.')
print(f'B => A média de idade cadastrada foi de {media} anos.')
print('C => As mulheres cadastradas foram: ', end='')
for cont in lista:
    if cont['sexo'] == 'F':
        print(f'{cont["nome"]}', end='...')
print('\nD => As pessoas com idade acima da média foram:')
for cont in lista:
    if cont['idade'] > media:
        print(f'{cont["nome"]} com {cont["idade"]} anos, ficou acima de média.')

