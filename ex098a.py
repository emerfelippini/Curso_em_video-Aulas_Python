from time import sleep
def contagem(inicio, fim, passos):
    print('-=' * 40 )
    print(f'Contagem de {inicio} até {fim} pulando {passos}.')
    if passos == 0:
        passos = 1
    if fim > inicio:
        for cont in range (inicio, fim + 1, passos):
            print(cont, end=' ', flush = True)
            sleep(0.5)
    elif fim < inicio:
        for cont in range (inicio, fim - 1, passos):
            print(cont, end=' ', flush = True)
            sleep(0.5)
    print()
    print('-=' * 40 )


# Programa principal
contagem(1, 10, 1)
contagem(10, 0, -2)
print('-=' * 40)
ini = int(input('Digite o inicio: '))
fim = int(input('Digite o fim: '))
pas = int(input('De quanto em quanto: '))
contagem(ini, fim, pas)