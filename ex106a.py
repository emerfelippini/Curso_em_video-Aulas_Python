c = ('\033[m', # 0 sem cor
'\033[1;41m'   # 1 fundo vermelho
)
def sisHelp(com):
    help(com)


def título(msg, cor=0): 
    print(c[cor])
    print('~' * len(msg))
    print(msg)
    print('~' * len(msg))
    print(c[0])

título('SISTEMA DE AJUDA', cor=1)
while True:
    a = str(input('Digite função ou biblioteca (FIM para finalizar): '))
    if a.upper() == 'FIM':
        print('\033[1;41m    ATÉ LOGO!!\033[m')
        break
    sisHelp(a)