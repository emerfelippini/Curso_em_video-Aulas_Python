def ficha(nome = '<desconhecido>', gol = 0):
    print(f'O jogador {nome}, fez {gol} gols.')


nome = str(input('Nome do jogador: '))
gols = str(input('Quantos gols esse jogador marcou: '))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    ficha(gol = gols)
else:
    ficha(nome, gols)