print('-' * 5, '10 termos de uma PA', '-' * 5)
termo = int(input('Digite o primeiro termo: '))
razão = int(input('Digite a razão: '))
for c in range(termo, razão * 10 + termo, razão):
    print(c, end=' -> ')