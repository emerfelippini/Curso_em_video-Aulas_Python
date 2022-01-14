print('\033[1;32m ', '-' * 20, 'CALCULANDO O FATORIAL', '-' * 20, '\033[m')
num = int(input('Digite um número, para calcular seu fatorial: '))
c = num
f = 1
print('\033[1;32m{}! = '.format(num), end='')
while c > 0:
    print('{}'.format(c), end='')
    print(' x ' if c > 1 else ' = ', end='')
    f *= c
    c -= 1
print(f, '\033[m')