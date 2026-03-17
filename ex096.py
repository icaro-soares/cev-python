"""
Faça um exercício que tenha uma função chamada area, que receba duas dimensões de um terreno retângular (largura e comprimento) e mostre a área do terreno.
"""


def area(larg, comp):
    a = larg*comp
    print(f'A área do terreno é de {a:.2f}m²')


l = float(input('Qual a largura do terreno (m): '))
c = float(input('Qual o comprimento do terreno (m): '))
area(l, c)
