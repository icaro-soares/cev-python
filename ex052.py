"""Faça um programa que leia um número inteiro e diga se ele é ou não um
número primo, divisível po 1 e ele mesmo"""
n = int(input('Número: '))
divisores = 0
print(f'Os divisores de {n} são: ', end='')
for c in range(1, n+1):
    if n % c == 0:
        print(c, end=' ')
        divisores += 1
if divisores == 2:
    print(f'\nO número {n} é primo, pois tem apenas {divisores} divisores')
else:
    print(f'\nO número {n} tem {divisores} divisores, então não é primo')
