"""Crie um programa que leia o ano de nascimento de sete pessoas. No final
mostre quantas pessoas ainda não atingiram a maioridade e quantas já são
maiores considere 21"""
from datetime import date

maior = 0
for c in range(1, 8):
    nasc = int(input('Nascimento [0 p/ ano atual]: '))
    if nasc == 0:
        nasc = date.today().year
    idade = date.today().year - nasc
    if idade >= 21:
        maior += 1
print(f'Pessoas maiores de idade: {maior}')
