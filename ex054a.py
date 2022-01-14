import datetime
ano_atual = datetime.date.today().year
menor_idade = 0
maior_idade = 0
print('\033[1;30;42m', ' ' * 15, 'VERFICAÇÃO DE IDADE', ' ' * 15, '\033[m' )
for cont in range (1, 8, +1):
    ano_nas = int(input('Digite o {}° ano de nascimento: '.format(cont)))
    if ano_atual - ano_nas >= 21:
        maior_idade += 1
    else:
        menor_idade += 1
print('\033[1;32m{} pessoa(s) atingiram a maior idade.\033[m\n\033[1;31m{} pessoa(s) são de menor idade.\033[m'.format(maior_idade, menor_idade))


