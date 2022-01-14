from math import radians, cos, sin, tan
x1 = float(input('Digite o ângulo desejado:'))
tan = tan(radians(x1))
sen = sin(radians(x1))
cos = cos(radians(x1))
print('Com o ângulo de {:.2f}°, temos a tangente {:.2f}°, seno em {:.2f}° e o cosseno de {:.2f}°'.format(x1, tan, sen, cos))