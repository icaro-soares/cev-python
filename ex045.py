"""Faça um programa que faça o computador jogar Jokenpô com você"""
from random import randint

itens = ('pedra', 'papel', 'tesoura')
j1 = int(input('Faça sua jogada [0 - pedra][1 - papel][2 - tesoura]: '))
cpu = randint(0, 2)
print('-=' * 30)
print(f'J1: {itens[j1]} x {itens[cpu]} :CPU')
print('-=' * 30)
#Funcionamento:
if j1 == 0:
    if cpu == 0:
        print('Empatou')
    elif cpu == 1:
        print('Perdeu')
    elif cpu == 2:
        print('Ganhou')
elif j1 == 1:
    if cpu == 0:
        print('Ganhou')
    elif cpu == 1:
        print('Empatou')
    elif cpu == 2:
        print('Perdeu')
elif j1 == 2:
    if cpu == 0:
        print('Perdeu')
    elif cpu == 1:
        print('Ganhou')
    elif cpu == 2:
        print('Empatou')
