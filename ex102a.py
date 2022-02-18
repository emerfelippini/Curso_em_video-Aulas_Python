def fatorial(num, show=False):
    """
    -> Função para calcular fatorial.
    -> Paramêtros:
    * num: Número a ser calculado o fatorial.
    * show: True para mostrar calculo, False para mostrar apenas resultado.
    * return: Resultado da somatória.
    """
    soma = 1
    for cont in range (num, 0, -1):
        if show:
            print(cont, end='')
            if cont > 1:
                print(' x ', end='')
            else :
                print(' = ', end='')
        soma *= cont
    return soma


help(fatorial)
print(f'{fatorial(5, show = True)}')