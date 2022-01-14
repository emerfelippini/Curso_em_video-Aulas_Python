print('\033[1;32m ENCONTRANDO VOGAIS\033[m')
palavras = ('PROGRAMADOR', 'COMPUTADOR', 'TECNICO', 'INFORMATICA', 'LIVRO',
            'MOUSE', 'TECLADO', 'CELULAR', 'CANETA', 'CARTEIRA', 'ESCOVA')
for cont in palavras:
    print(f'\nNa palavra {cont} temos ', end='')
    for letras in cont:
        if letras.upper() in 'AEIOUaeiou':
            print(letras, end='')
