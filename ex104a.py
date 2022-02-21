def leiaInt(msg):
    valor = 0
    ok = False
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('\033[1;31mERRO!!, Digite um valor válido.\033[m')
        if ok == True:
            break
    return valor



num = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {num}.')