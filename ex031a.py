'''viagem = float(input('Quantos Kms serão percorridos nessa viagem? '))
if viagem <= 200:
    print('Como sua viagem é menor que 200km, você pagará R${:.2f}'.format(viagem * 0.50))
else:
    print('Como sua viagem passou de 200km, com a promoção, você pagará R${:.2f}'.format(viagem * 0.45))'''
viagem = float(input('Quantos Kms serão percorridos nessa viagem? '))
preço = viagem * 0.50 if viagem <= 200 else viagem * 0.45
print('Como você irá percorrer {:.0f}KM, sua passagem sairá de R${:.2f}'.format(viagem, preço))