jogador = dict()
gols = list()
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input('Quantas partidas esse jogador jogou: '))
for cont in range(1, partidas + 1, +1):
    partida = int(input(f'* Quantos gols ele marcou na {cont}ª partida: '))
    gols.append(partida)
jogador['gols'] = gols[:]
jogador['total de gols'] = sum(gols)
print('-=' * 50)
print(jogador)
print('-=' * 50)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('-=' * 50)
print(f'O jogador {jogador["nome"]} jogou {partidas} partidas.')
for pos, cont in enumerate(gols):
    print(f'=> Na partida {pos + 1}ª, fez {cont} gols.')
print(f'Foi um total de {sum(gols)} gols.')