print('\033[1;32m', ' ' * 20, 'ANALISANDO DADOS', ' ' * 20, '\033[m')
contagem_idade = 0
maior_idade = 0
nome_maior = ''
mulher_menor = 0
M = 0
F = 0
for c in range (1, 5, +1):
    print('-' * 5, '{}ª PESSOA'.format(c), '-' * 5)
    nome = str(input('Digite o nome da {}ª pessoa: '.format(c))).strip()
    idade = int(input('Digite a idade da {}ª pessoa: '.format(c))).strip()
    sexo = str(input('Digite [M] para masculino e [F] para feminino: ')).strip()
    if sexo != M or F:
        print('Opção inválida, pessoa desconsiderada.')
    contagem_idade += idade
    if c == 1 and sexo in 'Mm':
        nome_maior = nome
        maior_idade = idade
    elif maior_idade < idade and sexo in 'Mm':
        maior_idade = idade
        nome_maior = nome
    elif sexo in 'Ff' and idade < 20:
            mulher_menor += 1
print('O homem mais velho se chama {} e tem {} anos'.format(nome_maior, maior_idade))
print('A média de idade do grupo é de {} anos'.format(contagem_idade / 4))
print('Ao todo tem {} mulher(es) com menos de 20 anos'.format(mulher_menor))
