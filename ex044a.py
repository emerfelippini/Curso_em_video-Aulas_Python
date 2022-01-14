print('*' * 5, 'ESCOLHER FORMA DE PAGAMENTO', '*' * 5)
preço = float(input('Digite o preço do produto: R$'))
print('CONDIÇÕES DE PAGAMENTO:')
print('( 1 ) á vista em dinheiro/cheque, 10% de desconto.')
print('( 2 ) á vista no cartão, 5% de desconto.')
print('( 3 ) em até 2x no cartão, preço normal.')
print('( 4 ) 3x ou mais no cartão, 20% de juros.')
pagamento = int(input('Digite o número relacionado a forma de pagamento a ser realizado: '))
if pagamento == 1:
    print('O preço a ser pago pelo produto será R${:.2f}'.format(preço * 0.9))
elif pagamento == 2:
    print('O preço a ser pago pelo produto será R${:.2f}'.format(preço * 0.95))
elif pagamento == 3:
    print('O preço a ser pago pelo produto será R${:.2f}'.format(preço))
elif pagamento == 4:
    print('O preço a ser pago pelo produta será R${:.2f}'.format(preço * 1.20))