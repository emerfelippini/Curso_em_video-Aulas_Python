from time import sleep
print('Digite 999 se quiser parar')
num = soma = quantidade = 0
while num != 999:
    num = int(input('Digite um número: '))
    soma += num
    quantidade += 1
soma -= 999
quantidade -= 1
print('Foram mostrados {} números e a soma deles é {}.'.format(quantidade, soma))
print('Finalizando ....')
sleep(2)