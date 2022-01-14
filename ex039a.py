from datetime import date
''
ano_atual = date.today().year - 18
sexo = str(input('Digite M para masculino e F para feminino'))
nascimento = int(input('Digite o ano de seu nascimento: '))
''
if nascimento == ano_atual:
    print('Este ano você deve se alistar.')
elif nascimento < ano_atual:
    print('Você ja passou da hora de alistar, há {} anos atrás.'.format(ano_atual - nascimento))
else:
    print('Ainda não está na hora de seu alistamento, falta {} anos.'.format(nascimento - ano_atual))
