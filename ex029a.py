print('-=-' * 20)
vel = int(input('A qual velocidade você esta dirigindo? '))
print('-=-' * 20)
print('-=-' * 20)
if vel > 80:
    print('Você está andando há {}Km/h!!!!!, está acima do limite de 80Km/h'.format(vel))
    mul = (vel - 80) * 7
    print('Sinto em lhe dizer, mas você foi multado em {}R$'.format(mul))
else:
    print('Você esta andando há {}Km/h, parabêns está no limite de 80Km/h, continue assim'.format(vel))
print('-=-' * 20)