from emoji import emojize
print(emojize(':red_heart: CALCULADORA DE INDICE DE MASSA CORPÓREA :red_heart:' ))
altura = float(input('Digite sua altura [ M ]: '))
peso = float(input('Digite seu peso [ KG ]: '))
imc = peso / ( altura ** 2 )
if imc <= 18.5:
    print('Seu IMC está abaixo do ideal, seu IMC é de {:.2f}'.format(imc))
elif 18.5 < imc <= 25:
    print('Seu IMC está ideal, parabéns, seu IMC é de {:.2f}'.format(imc))
elif 25 < imc <= 30:
    print('Sobrepeso, tenha cuidado, seu IMC é de {:.2f}'.format(imc))
elif 30 < imc <= 40:
    print('Obesidade, tenha cuidado, seu IMC é de {:.2f}'.format(imc))
else:
    print('OBESIDADE MÓRBIDA, tenha muito cuidado, seu IMC é de {:.2f}'.format(imc))