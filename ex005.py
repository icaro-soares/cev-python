"""
Docstring for ex005
Faça um programa que leia um número Inteiro e mostre
na tela seu sucessor e seu antecessor.
"""
número = int(input('Digite um número: '))
ant = número - 1
suc = número + 1
print(f'O número digitado foi {número}.', end=' ')
print(f'Seu antecessor é {ant} e seu sucessor é {suc}')