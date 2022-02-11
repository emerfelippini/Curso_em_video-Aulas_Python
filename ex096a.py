print('\033[1;32m INICIANDO OS ESTUDO COM FUNÇÕES\033[m')
def área(largura, comprimento):
    area = largura * comprimento
    print(f'Com as medidas de {largura} x {comprimento} temos uma área de {area}m²')
   

print('-=' * 30)
print('CONTROLE DE TERRENOS')
print('-=' * 30)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
área(l, c)