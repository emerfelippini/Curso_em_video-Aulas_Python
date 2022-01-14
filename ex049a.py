import emoji
print(emoji.emojize(':red_heart: TABUADA !! :red_heart:'))
num = int(input('Digite o número para gerar sua tabuada: '))
for c in range(1, 11, +1):
    soma = num * c
    print('{} X {} = {}'.format(num, c, soma))
