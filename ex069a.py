num_pessoas = maior_idade = homens = menor_idade = 0
print('\033[1;31m CADASTRAMENTO \033[m')
while True:
    print('-=' * 20)
    idade = int(input('Digite a idade: '))
    if idade >= 18:
        maior_idade += 1
    sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()[0]
    while sexo not in 'MmFf':
        sexo = str(input('Digite o sexo [M/F]: ')).upper().strip()[0]
    if sexo in 'Mm':
        homens += 1
    elif sexo in 'Ff' and idade < 20:
        menor_idade += 1
    num_pessoas += 1
    escolha = str(input('Deseja cadastrar mais uma pessoa [S/N]: ')).upper().strip()[0]
    while escolha not in 'NnSs':
        escolha = str(input('Deseja cadastrar mais uma pessoa [S/N]: ')).upper().strip()[0]
    if escolha in 'Nn':
        print('Está ok.')
        break
    print('-=' * 20)
if maior_idade > 0:
    print(f'Tivemos {maior_idade} pessoas maiores de 18 anos cadastradas.')
if homens > 0:
    print(f'Tivemos {homens} homen(s) cadastrados.')
if menor_idade > 0:
    print(f'Tivemos {menor_idade} mulhere(s) com menos de 20 anos cadastrados.')
print('Finalizando programa ....')