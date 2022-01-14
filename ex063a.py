print('-=' * 20, 'SEQUENCIA FIBONACCI', '-=' * 20)
termos = int(input('Digite quantos termos mostrar: '))
print('-=' * 20)
t1 = 0
t2 = 1
cont = 3
t3 = 1
print('{} -> {} '.format(t1, t2), end='')
while cont <= termos:
    print('-> {} '.format(t3), end='')
    t1 = t2
    t2 = t3
    t3 = t1 + t2
    cont += 1
print('-> FIM')