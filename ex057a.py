print('\033[1;32m VALIDAÇÃO DO SEXO DE UMA PESSOA \033[m')
sexo = ''
sexo = str(input('Digite o sexo da pessoa [M/F]: ')).upper().strip()[0]
while sexo != 'M' and 'F':
    print('Opção inválida.')
    sexo = str(input('Digite novamente o sexo da pessoa [M/F]: ')).upper().strip()[0]
print('Opção registrada com sucesso, opção escolhida foi: {}'.format(sexo))

