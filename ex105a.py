def notas(* notas, sit=False):
    """
    -> Função para analisar notas dos alunos.
    *param notas: uma ou mais notas de alunos (aceita infinitas notas)
    *param sit: se True mostra a situação do aluno conforme sua média
    -> Tem como saída um dicionário com informações variádas.
    """
    maior = menor = media = 0
    dic = dict()
    dic['total'] = len(notas)
    dic['maior'] = max(notas)
    dic['menor'] = min(notas)
    dic['média'] = sum(notas) / len(notas)
    if sit == True:
        if media >= 7:
            dic['situação'] = 'Boa'
        elif media <= 5:
            dic['situação'] = 'Ruim'
        else:
            dic['situação'] = 'Razoável'
    print(dic)


notas(5.5, 7, 2, 9.3, 3, 1)
help(notas)