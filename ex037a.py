print(5 * '*', 'CONVERSOR DE BASES', 5 * '*')
numero = int(input('Digite um número inteiro para converter sua base:'))
print('''Selecione a opção de conversão:
[ 1 ] para converter para BINÁRIO
[ 2 ] para converter para OCTAL
[ 3 ] para converter para HEXADECIMAL''')
opção = int(input('Digite a opção:'))
if opção == 1:
    print('A conversão de {} para binário é: {}'.format(numero, bin(numero)[2:]))
elif opção == 2:
    print('A conversão de {} para octal é: {}'.format(numero, oct(numero)[2:]))
elif opção == 3:
    print('A conversão de {} para hexadecimal é: {}'.format(numero, hex(numero) [2:]))
else:
    print('Alternativa inválida.')
