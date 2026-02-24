"""
Crie um programa que leia dois valores e mostre um menu na tela:
[1] somar
[2] multiplicar
[3] maior
[4] novos números
[5] sair
Seu programa deverá realizar a operação solicitada em cada caso
"""
from time import sleep

n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
opção = 0
while opção != 5:
    opção = int(input('''Escolha a opção: [1] Somar [2] Multiplicar [3] Maior [4] Novos números [5] Sair: '''))
    sleep(.5)
    if opção == 1:
        soma = n1 + n2
        print(f'A soma dos valores é: {soma}')
    elif opção == 2:
        multiplicação = n1 * n2
        print(f'O produto dos valores é: {multiplicação}')
    elif opção == 3:
        if n1 > n2:
            print('O primeiro valor é maior')
        elif n1 < n2:
            print('O segundo valor é maior')
        elif n1 == n2:
            print('Não existe valor maior, eles são iguais')
    elif opção == 4:
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif opção == 5:
        print('Saindo do programa...')
    else:
        print('Opção inválida tente novamente!')
    print('-=' * 30)