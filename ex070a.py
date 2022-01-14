print('CADASTRO DE PRODUTOS')
print('-=' * 20)
soma = preço_maior = menor_preço = contagem = 0
menor_nome = ''
while True:
    nome = str(input('Nome do produto: '))
    preço = float(input('Preço: R$ '))
    soma += preço
    if preço >= 1000:
        preço_maior += 1
    contagem += 1
    if contagem == 1 or menor_preço > preço:
        menor_preço = preço
        menor_nome = nome
    escolha = str(input('Continuar [S/N]: ')).upper().strip()[0]
    while escolha not in 'SsNn':
        escolha = str(input('Continuar [S/N]: ')).upper().strip()[0]
    if escolha in 'Nn':
        break
    print('-=' * 20)
print(f'Total gasto: R${soma:.2f}')
print(f'Produtos mais caros que R$1.000: {preço_maior:}')
print(f'Produto mais barato: {menor_nome}')