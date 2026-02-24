"""
Docstring for ex018
Faça um programa que leia um ângulo qualquer
e mostre na tela o valor do seno,
cosseno e tangente desse ângulo
"""
from math import sin, cos, tan, radians


ângulo = float(input('Ângulo: '))
print(f'O seno de {ângulo}° é {sin(radians(ângulo)):.3f}')
print(f'O cosseno de {ângulo}° é {cos(radians(ângulo)):.3f}')
print(f'A tangente de {ângulo}° é {tan(radians(ângulo)):.3f}')
