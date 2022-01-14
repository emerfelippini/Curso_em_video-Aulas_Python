'''import random
alu = ('Michael', 'Bruno', 'Fabricio', 'Marcos')
print('O escolhido para apagar o quadro é o {}'.format(random.choice(alu)))'''
from random import choice
alu1 = input('Primeiro aluno? ')
alu2 = input('Segundo aluno? ')
alu3 = input('Terceiro aluno? ')
alu4 = input('Quarto aluno? ')
lista = [alu1, alu2, alu3, alu4]
print('O aluno escolhido foi o {}'.format(choice(lista)))