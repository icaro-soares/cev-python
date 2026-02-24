"""Faça um programa que leia 3 números e diga qual é o maior e qual é o menor"""
a = int(input('1º valor: '))
b = int(input('2º valor: '))
c = int(input('3º valor: '))
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b:
    maior = c
print(f'O maior valor é {maior}')
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b:
    menor = c
print(f'O menor valor é {menor}')
