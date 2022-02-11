print('\033[1;32m APRENDENDO FUNÇÕES EM PYTHON\033[m')
def escreva(msg):
    print('-' * (len(msg) + 2))
    print(f'{  msg}')
    print('-' * (len(msg) + 2))


x = str(input('Digite uma frase: '))
escreva(x)