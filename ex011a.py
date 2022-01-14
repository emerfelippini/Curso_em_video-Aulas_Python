n1 = float(input('Qual altura da sua parede?'))
n2 = float(input('Qual largura da sua parede?'))
area = n1*n2
print('Sua parede tem a dimensão {}x{} e sua área é de {}m²'.format(n1, n2, area))
print('Logo você precisará de {}L de tinta'.format(area/2))