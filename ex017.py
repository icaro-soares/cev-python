"""
Docstring for ex017
Faça um programa que leia o comprimento do cateto
oposto e do cateto adjacente de um triângulo retângulo.
Calcule e mostre o comprimento da hipotenusa
"""
from math import hypot


cateto_oposto = float(input('Cateto oposto: '))
cateto_adjacente = float(input('Cateto adjacente: '))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)
print(f'A hipotenusa vale: {hipotenusa:.2f}cm')
