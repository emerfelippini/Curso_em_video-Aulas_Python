nome = input('Digite seu nome: ')
print('Seu nome em maiúsculas ficaria {}.'.format(nome.upper()))
print('Seu nome em minúsculas fica {}.'.format(nome.lower()))
print('Seu nome tem {} caracteres.'.format(len(nome) - nome.count(' ')))
div = nome.split()
print('Seu primeiro nome é {} e ele tem {} caracteres.'.format(div[0], nome.find(' ')))