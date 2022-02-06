print('\033[1;32mANALISANDO DADOS\033[m')
jogador = dict()
gols = list()
jogadores = list()
print('-=' * 50)
while True:
    gols.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    partidas = int(input('Quantas partidas esse jogador jogou: '))
    for cont in range(1, partidas + 1, +1):
        partida = int(input(f'* Quantos gols ele marcou na {cont}ª partida: '))
        gols.append(partida)
    jogador['gols'] = gols[:]
    jogador['total de gols'] = sum(gols)
    jogadores.append(jogador.copy())
    escolha = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
    while escolha not in 'SN':
        print('Opção inválida.')
        escolha = str(input('Deseja continuar [S/N]? ')).upper().strip()[0]
    if escolha == 'N':
        break
    print('-=' * 30)
print('-=' * 50)
print(f'\033[1;32m{"COD":<20}{"NOME":<10}{"GOLS":>10}{"TOTAL":>15}\033[m')
for k, v in enumerate(jogadores):
    print(f'{k:<20}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-='* 40)
while True:
    resp = int(input('Mostrar dados de qual jogador [999] para parar: '))
    if resp == 999:
        break
    while resp > len(jogadores):
        print('Escolha inválida')
        resp = int(input('Mostrar dados de qual jogador [999] para parar: ')) 
    print(f'Levantamento do jogador {jogadores[resp]["nome"]}:')
    for pos, cont in enumerate(jogadores[resp]['gols']):
        print(f'=> Na partida {pos + 1} fez {cont} gols.')