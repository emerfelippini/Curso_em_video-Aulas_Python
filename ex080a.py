lista = list()
for c in range(0, 5, +1):
    num = int(input('Digite o valor: '))
    if c == 0 or num > lista[-1]:
        lista.append(num)
        print('Número adicionado ao final da lista.')
    else:
        pos = 0
        while pos < len(lista):
            if num <= lista[pos]:
                lista.insert(pos, num)
                print(f'Número adicionado na posição {pos} da lista')
                break
            pos += 1
print(lista)