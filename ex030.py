"""Crie um programa que leia um número inteiro qualquer e mostre na
tela se ele é par ou ímpar"""
número = int(input('Digite um número inteiro qualquer: '))
if número % 2 == 0:
    print(f'O número {número} é PAR')
else:
    print(f'O número {número} é ÍMPAR')
