from datetime import datetime
lista = dict()
while True:
    lista['nome'] = str(input('Nome: '))
    lista['ano'] = int(input('Ano de nascimento: '))
    lista['idade'] = datetime.today().year - lista['ano']
    lista['carteira'] = int(input('Carteira de trabalho (0 não tem): '))
    if lista['carteira'] == 0:
        break
    else:
        lista['ano'] = int(input('Ano de contratação: '))
        lista['salário'] = int(input('Salário: '))
        lista['aposentadoria'] = lista['idade'] + (lista['ano'] + 35 - datetime.today().year) 
    break
for k, v in lista.items():
    print(f'O(a) {k} tem valor {v}')