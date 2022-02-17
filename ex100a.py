from random import randint
números = list()
def sorteia():
    for _ in range(0, 5):
        números.append(randint(1, 100))
    print(números)


def somaPar():
    soma = 0
    for cont in números:
        if cont % 2 == 0:
            soma += cont
    print(soma)

    
print('Os números sorteados foram: ', end='')
sorteia()
print('A soma dos números pares foi: ', end='')
somaPar()