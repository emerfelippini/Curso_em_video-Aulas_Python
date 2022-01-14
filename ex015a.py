dia = int(input('Quantos dias alugados? '))
km = float(input('Quantos KM rodados? '))
print('Como você ficou {} dias com ele e rodou {:.2f}KM, sua conta ficou em {:.2f}R$'.format(dia, km, (60*dia)+(0.15*km)))
