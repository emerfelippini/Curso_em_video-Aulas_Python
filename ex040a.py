print('CALCULANDO A MÉDIA')
nota1 = float(input('Digite a sua primeira nota:'))
nota2 = float(input('Digite a sua segunda nota:'))
media = ( nota1 + nota2 ) / 2
if media < 5.0:
    print('Sinto muito, sua media foi de {} e você está reprovado.'.format(media))
elif media > 7.0:
    print('Meus parabêns, a sua média foi de {}, e você está aprovado.'.format(media))
else:
    print('Sua média foi de {}, você ficou de recuperação.'.format(media))