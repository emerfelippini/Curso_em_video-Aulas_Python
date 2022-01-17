print('\033[1mANALISANDO UMA EXPRESSÃO MATEMÁTICA\033[m')
lista = list()
abertura = fechamento = 0
expressão = str(input('Digite uma expressão: '))
for simb in expressão:
    if simb == '(':
        lista.append('(')
    elif simb == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break
if len(lista) == 0:
    print(f'\033[1;32mA expressão {expressão} é válida.\033[m')
elif len(lista) != 0:
    print(f'\033[1;31mA expressão {expressão} é inválida.\033[m')