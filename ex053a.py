print('\033[1;30;42m', ' ' * 15, 'PALÍNDROMO', ' ' * 15, '\033[m')
frase = str(input('Digite a frase a ser verificada: ')).strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = junto[::-1]
if junto == inverso:
    print('A frase normal: {}\nA frase invertida: {}\nPortanto, a frase é um palíndromo'.format(junto, inverso))
else:
    print('A frase normal: {}\nA frase invertida: {}\nPortanto, a frase não é um palíndromo'.format(junto, inverso))
