print('SOMA DOS NÚMEROS PARES.')
soma_par = 0
for c in range(1, 7, +1):
    num = int(input('Digite o número: '))
    if num % 2 == 0:
        soma_par += num
        print('O número digitado é um número par e foi contabilizado.')
    else:
        print('O número digitado é um número ímpar portanto foi desconsiderado.')
print('A soma dos valores foi de: {}'.format(soma_par))