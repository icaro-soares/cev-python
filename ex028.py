"""Escreva um programa que faça o computador 'pensar' em um número entre
0 e 5 e tente adivinha-lo. O programa deverá escrever se você acertous ou
derrou"""
from random import randint


número_aleatório = randint(0, 5)
chute = int(input('Qual seu chute (entre 0 e 5): '))
if chute == número_aleatório:
    print('Você acertou!')
else:
    print(f'Você errou. Eu pensei no número {número_aleatório}')
