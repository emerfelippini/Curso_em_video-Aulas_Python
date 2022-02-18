def voto(ano):
    from datetime import datetime
    ano_atual = datetime.today().year
    if (ano_atual - ano) < 16:
        return 'negado'
    elif 16 <= (ano_atual - ano ) < 18 or (ano_atual - ano) > 65:
        return 'opcional'
    elif 18 <= (ano_atual - ano ) <= 65:
        return 'obrigatório'


ano = int(input('Digite o ano de nascimento: '))
print(f'A pessoa nascendo no ano {ano}, o voto é {voto(ano)}.')