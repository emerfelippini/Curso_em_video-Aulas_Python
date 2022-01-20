print('\033[1;32mSEPARANDO VALORES PARES E ÍMPARES\033[m')
lista = [[], []]
for cont in range(0, 7, +1):
    valor = int(input(f'Digite o {cont + 1}ª valor: '))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
lista[0].sort()
lista[1].sort()
print(f'Os número pares foram: {(lista[0])}')
print(f'Os número ímpares foram: {lista[1]}')