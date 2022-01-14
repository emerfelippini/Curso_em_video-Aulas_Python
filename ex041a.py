from datetime import date
print('*' * 5, 'CONFEDERAÇÃO NACIONAL DE NATAÇÃO', '*' * 5)
ano_nascimento = int(input('Digite o ano de nascimento do atleta:'))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
print('O atleta tem {} anos, ele se encaixa na categoria:'.format(idade))
if idade <= 9:
    print('MIRIM')
elif 9 < idade <= 14:
    print('INFANTIL')
elif 14 < idade <= 19:
    print('JUNIOR')
elif 19 < idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')

