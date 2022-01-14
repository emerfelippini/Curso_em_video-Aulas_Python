import random
computador = random.randint(0, 5)
x1 = int(input('Pensei em número, tente adivinhálo: '))
if x1 == computador:
    print('Parabêns você adivinhou')
else:
    print('È uma pena, não foi dessa vez, eu pensei no número {} e não no {}.'.format(computador, x1))