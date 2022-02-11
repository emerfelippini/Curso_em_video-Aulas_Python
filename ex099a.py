def maior(* num):
    maior = 0
    for cont in num:
        if cont == 0:
            maior = cont
        if cont > maior:
            maior = cont
    print('-=' * 30)
    print('Os número analisados foram: ')
    for cont in num:
        print(f'\033[1;32m{cont}\033[m', end=' ')
    print(f'\nForam analisados {len(num)} números, e o maior foi o número {maior}.')
    print('-=' * 30)


maior(1, 2, 5, 23, 51, 7)
maior(1, 8, 9, 10, 6, 33, 5, 7)


