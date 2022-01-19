var = 50
print(type(var))
while True:
    print('-=' * 30)
    val = int(input('Digite o valor: '))
    if type(val) is str:
        print('funcionou')
        break