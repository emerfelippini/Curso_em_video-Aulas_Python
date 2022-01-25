print('\033[1;32mANALISADOR DE NOTAS\033[m')
print('-=' * 30)
lista = list()
copia = list()
media = opçao = 0
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('1ª nota: '))
    nota2 = float(input('2ª nota: '))
    media = (nota1 + nota2) / 2
    lista.append(nome)
    lista.append(nota1)
    lista.append(nota2)
    lista.append(media)
    copia.append(lista[:])
    lista.clear()
    escolha = str(input('Deseja adicionar outro aluno [S/N]: ')).upper().strip()[0]
    while escolha not in 'SN':
        print('Escolha inválida, tente novamente.')
        escolha = str(input('Deseja adicionar outro aluno [S/N]: ')).upper().strip()[0]
    if escolha == 'N':
        break
    print('-=' * 30)
print('-=' * 30)
print(f'{"Nº":<5}{"NOME":^8}{"MÉDIA":>13}')
for pos, cont in enumerate(copia):
    print(f'{pos:<5}{cont[0]:^8}{cont[3]:>13}')
print('-=' * 30)
while True:
    opção = int(input('Digite o número do aluno para ver sua nota ou [999] para encerrar o programa: '))
    if opção == 999:
        print('Obrigado.... até logo.')
        break
    if opção <= len(copia) - 1:
        print(f'\033[1;32mO aluno {copia[opção][0]} teve as nota {copia[opção][1]} e {copia[opção][2]}, com isso sua média foi {copia[opção][3]}\033[m')
    print('-=' * 30)
