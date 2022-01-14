x1 = str(input('Digite uma frase: ').strip())
print('A letra A parece {} vezes.'.format(x1.lower().count('a')))
print('Foi encontrada a primeira vez no {} caractere.'.format(x1.lower().find('a') + 1 ))
print('Foi encontrada pela última vez no {} caractere'.format(x1.lower().rfind('a') + 1 ))