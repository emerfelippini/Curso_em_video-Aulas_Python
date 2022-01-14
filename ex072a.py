print('\033[1;31m Digitando o número por extenso \033[m')
lista = ('Zero', 'Um', 'Dois', 'Três', 'Quatro', 'Cinco',
         'Seis', 'Sete', 'Oito', 'Nove', 'Dez', 'Onze',
         'Doze', 'Treze', 'Quatorze', 'Quinze',
         'Dezesseis', 'Dezessete', 'Dezoito',
         'Dezenove', 'Vinte' )
while True:
    num = int(input('Digite um número entre 0 e 20: '))
    if 0 <= num <= 20:
        print(f'O número digitado : {lista[num]}')
        escolha = str(input('Você quer continuar? [S/N]')).upper().strip()[0]
        if escolha in 'N':
            break
        while escolha not in 'NnSs':
            escolha = str(input('Você quer continuar? [S/N]: '))

