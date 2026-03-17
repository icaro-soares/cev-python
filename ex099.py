"""
Faça um programa que tenha uma função chamada maior(), que receba vários valores inteiros com parâmetro.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""


def maior(*num):
    print('Analisando os valores passados...')
    print('Foram passados os valores ', end='')
    for n in num:
        print(f'{n} ', end='')
    print(f'\nO maior valor é {max(num)}')
    print('-='*20)


maior(7, 5, 3)
maior(4, 10, 14, 2, 0, 10)
maior(1, 3, 0, 1, 2)
maior(7, 6, 1, 9)
