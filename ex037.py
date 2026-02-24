"""Escreva um programa que leia um número inteiro qualquer e peça para o
usuário escolher qual será a base de conversão:
1 para binário
2 para octal
3 para hexadecimal"""
n = int(input('Número: '))
escolha = int(input('''Escolha a base de conversão
[1] Binário
[2] Octal
[3] Hexadecimal: '''))
if escolha == 1:
    print(f'Binário: {bin(n)[2:]}')
elif escolha == 2:
    print(f'Octal: {oct(n)[2:]}')
elif escolha == 3:
    print(f'Hexadecimal: {hex(n)[2:]}')
else:
    print('Escolha inválida!')
