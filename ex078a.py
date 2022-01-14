lista = list()
for cont in range (0, 5, +1):
    lista.append(int(input(f'Digite o {cont + 1}ª número: ')))
print('-=' * 30)
print(f'O maior da lista é: {max(lista)}')
print(f'E está nas pocisões: ', end='')
for posição, c in enumerate(lista):
    if c == max(lista):
        print(f'{posição + 1}ª', end='')
'\n'
print('-=' * 30)
print(f'O menor da lista é: {min(lista)}, e está na posição {lista.index(min(lista))}')
for posição, cont in enumerate(lista):
    if cont == min(lista):
        print(f'{posição + 1}ª', end='')
'\n'
print('-=' * 30)