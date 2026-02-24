"""
Crie um programa que simule um caixa eletrônico.
No início pergunte quanto o usuário quer sacar.
O programa vai informar quantas cédulas serão entregues.
Considere cédulas de R$50, R$20, R$10, R$1
"""
valor = int(input('Qual valor a sacar: R$'))
total = valor
cédulas = 100
totalcéd = 0
while True:
    if total >= cédulas:
        total -= cédulas
        totalcéd += 1
    else:
        if totalcéd > 0:
            print(f'{totalcéd} cédulas de R${cédulas}')
        if cédulas == 100:
            cédulas = 50
        elif cédulas == 50:
            cédulas = 20
        elif cédulas == 20:
            cédulas = 10
        elif cédulas == 10:
            cédulas = 5
        elif cédulas == 5:
            cédulas = 1
        totalcéd = 0
        if total == 0:
            break
