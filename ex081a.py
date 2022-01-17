print('\033[1;32mANALISANDO UMA LISTA\033[m')
lista = list()
while True:
    print('-=' * 30)
    lista.append(int(input('Digite o valor: ')))
    escolha = str(input('Deseja adicionar outro número [S/N]: ')).upper().strip()[0]
    while escolha not in 'NnSs':
        print('Escolha inválida.')
        escolha = str(input('Deseja adicionar outro número [S/N]: '))
    if escolha in 'Nn':
        break
    print('-=' * 30)
print('-=' * 30)
print(f'Foram digitados: {len(lista)} números.')
lista.sort(reverse=True)
print(f'A lista em ordem decrescente ficou: {lista}')
if 5 in lista:
    print('O valor 5 foi adicionado a lista.')
elif 5 not in lista:
    print('O valor 5 não está na lista.')
    