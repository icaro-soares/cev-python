from math import sin, cos, tan, radians


ângulo = float(input('Ângulo: '))
print(f'O seno de {ângulo}° é {sin(radians(ângulo)):.3f}')
print(f'O cosseno de {ângulo}° é {cos(radians(ângulo)):.3f}')
print(f'A tangente de {ângulo}° é {tan(radians(ângulo)):.3f}')
