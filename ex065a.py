escolha = 's'
num = cont = soma = maior = menor = 0
while escolha not in 'Nn':
    num = int(input('Digite um número: '))
    escolha = str(input('Quer continuar [S/N]: ')).strip()[0]
    if escolha not in 'SsNn':
        print('Escolha inválido, digite novamente')
    cont += 1
    soma += num
    if cont == 1:
        maior = menor = num
    else:
        if maior < num:
            maior = num
        elif menor > num:
            menor = num
print('Voce digitou {} número e a média foi de {:.2f}.'.format(cont, (soma/cont)))
print('O número maior foi {} e o menor foi {}.'.format(maior, menor))