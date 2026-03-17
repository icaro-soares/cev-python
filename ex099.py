"""
Faça um programa que tenha uma função chamada maior(), que receba vários valores inteiros com parâmetro.
Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""


def maior(*num):
    cont = maior = 0
    print('Analisando os valores... ')
    for n in num:
        print(f'{n} ', end='')
        if cont == 0:
            maior = n
        else:
            if n > maior:
                maior = n
        cont+=1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valor é {maior}')
    print('-='*40)


maior(7, 5, 3)
maior(4, 10, 14, 2, 0, 10)
maior(1, 3, 0, 1, 2)
maior(7, 6, 1, 9)
maior()
