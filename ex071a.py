saque = int(input('Qual valor você quer sacar: R$'))
céd = 50
totcéd = 0
while True:
    if saque >= céd:
        saque -= céd
        totcéd += 1
    else:
        if totcéd > 0:
            print(f'Total de {totcéd} cédulas de R${céd}')
        if céd == 50:
            céd = 20
        elif céd == 20:
            céd = 10
        elif céd == 10:
            céd = 1
        totcéd = 0
        if saque == 0:
            break
