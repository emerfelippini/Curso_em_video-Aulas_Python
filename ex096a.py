print('\033[1;32m INICIANDO OS ESTUDO COM FUNÇÕES\033[m')
def área():
    comprimento = float(input('Digite o comprimento (m): '))
    largura = float(input('Digite a largura (m): '))
    area = comprimento * largura
    print(f'Com o comprimento de {comprimento}m e a largura de {largura}m temos uma área de {area:.2f}m')


área()