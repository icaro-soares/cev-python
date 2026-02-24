"""
Docstring for ex011
Faça um programa que leia a largura e a altura de uma parede em metros,
calcule a sua área e a quantidade de tinta necessária para pintá-la,
sabendo que cada litro de tinta pinta uma área de 2m².
"""
largura = float(input('Digite a largura de uma parede (m): '))
altura = float(input('Digite a altura de uma parede (m): '))
área = largura * altura
print(f'A área de sua parede é {área:.2f}m²')
litros = área/2
print(f'Serão necessários {litros}L de tinta para pintá-la.')
