"""
Docstring for ex016
Crie um programa que leia um número real
qualquer pelo teclado e mostre na tela
a sua porção inteira
"""
from math import trunc


número = float(input('Digite um valor com vírgula: '))
print(f'A parte inteira do número é: {trunc(número)}')
