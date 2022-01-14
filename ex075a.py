num = (int(input('Digite o primeiro número: ')),
        int(input('Digite o primeiro número: ')),
        int(input('Digite o primeiro número: ')),
         int(input('Digite o primeiro número: ')))
print(f'Os números digitados foram: {num}')
print(f'O valor 9 apareceu {num.count(9)} vez(es).')
print(f'O valor 3 apareceu na {num.index(3)}ª posição')
print('Os valores pares foram:')
for c in num:
    if c % 2 == 0:
        print(c, end=' -> ')
print('FIM')