"""
Faça um programa que tenha uma função contador(), que receba três parâmetros: inicio, fim e passo e realize a contagem. Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10 de 1 em 1
b) de 10 até 0 de 2 em 2
c) Uma contagem personalizada
"""


def contador(i=1, f=10, p=1):
    if i < f:
        while i <= f:
            print(f'{i} ', end='')
            i+=p
        print('Fim!')
    elif i > f:
        while i >= f:
            print(f'{i} ', end='')
            i-=p
        print('Fim!')


contador(1, 10, 1)
contador(10, 0, 2)
