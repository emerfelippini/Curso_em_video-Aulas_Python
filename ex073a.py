print('-=' * 20, '\033[1;32mBrasileirão 2021\033[m', '-=' * 20)
lista = ('Atlético-MG', 'Flamengo', 'Palmeiras', 'Fortaleza', 'Corinthians', 'Bragantino',
         'Fluminense', 'América-MG', 'Atlético-GO', 'Santos', 'Ceará', 'Internacional',
         'São Paulo', 'Atlético-PR', 'Cuiabá', 'Juventude', 'Grêmio', 'Bahia', 'Sport', 'Chapecoense')
print('-=' * 30)
print(f'Lista de times do Brasileirão 2021:')
for t in lista:
    print(t, end=', ')
print('-=' * 30)
print(f'Os 5 primeiros times são: \033[1;32m{lista[:5]}\033[m')
print('-=' * 30)
print(f'Os 4 últimos times são: \033[1;31m{lista[16:]}\033[m')
print('-=' * 30)
print(f'Os times em ordem alfabética são: {sorted(lista)}')
print('-=' * 30)
print(f'A chapecoense está {lista.index("Chapecoense") + 1}° posição.')
