aluno = dict()
aluno['nome'] = str(input('Digite o nome do aluno: '))
aluno['média'] = float(input('Digite a média do aluno: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'aprovado'
elif aluno['média'] <= 5:
    aluno['situação'] = 'reprovado'
else:
    aluno['situação'] = 'em recuperação'
print('-=' * 40)
print(f'O aluno {aluno["nome"]}, teve uma média {aluno["média"]}, portanto, está {aluno["situação"]}.')