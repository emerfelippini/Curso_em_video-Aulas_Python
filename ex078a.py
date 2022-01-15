lista = list()
for cont in range (0, 5, +1):
    lista.append(int(input(f'Digite o {cont + 1}ª número: ')))
print('-=' * 30)
print(f'O maior da lista é: {max(lista)}')
print(f'E está nas posições: ', end='')
for posição, c in enumerate(lista):
    if c == max(lista):
        print(f'{posição + 1}ª...', end='')
print(f'\nO menor da lista é: {min(lista)}\nE está na posição: ', end='')
for posição, cont in enumerate(lista):
    if cont == min(lista):
        print(f'{posição + 1}ª...', end='')