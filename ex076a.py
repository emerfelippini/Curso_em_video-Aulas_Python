lista = ('Caderno', 5.35, 'Lápis', 1.50, 'Borracha', 0.75, 'Lapiseira', 2.50, 'Folhas A4', 18.50, 'Apontador',
         3, 'Fichário', 22.50, 'Lápis de cor', 15.50)
print('\033[1;32m LISTA SUPER MERCADO\033[m')
print('-=' * 30)
for cont in range(0, len(lista), +1):
    if cont % 2 == 0:
        print(f'{lista[cont]:.<30}', end='')
    else:
        print(f'R${lista[cont]:.2f}')
print('-=' * 30)