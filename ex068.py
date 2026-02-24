"""
Faça um programa que jogue par ou ímpar
com o computador. O jogo será interrompido
quando o jogador perder. No final mostre
quantas vitórias consecutivas o jogador
teve.
"""
from random import randint

v = 0
print('-='*30)
print('Par ou Ímpar'.center(30))
print('-='*30)
while True:
    cpu = randint(0, 10)
    j1 = int(input('Digite um valor: '))
    escolha = str(input('Par ou Ímpar [P/I]: ')).strip()[0]
    print(f'Você jogou {j1} e o computador {cpu}')
    par = (j1 + cpu) % 2 == 0
    print(f'A soma dos valores foi: {j1+cpu}.', end=' ')
    print('Deu par' if par else 'Deu ímpar')
    if escolha in 'Pp':
        if par:
            print('Você ganhou!')
            v+=1
        else:
            print('Você perdeu!')
            break
    else:
        if not par:
            print('Você ganhou!')
            v+=1
        else:
            print('Você perdeu!')
            break
print(f'Vitórias consecutivas: {v}')
