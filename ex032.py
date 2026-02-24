"""Faça um programa que leia um ano qualquer e diga se ele é
bissexto ou não"""
from datetime import date


ano = int(input('Ano [0 para utilizar o ano atual]: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0 :
    print(f'Ano {ano} BISSEXTO')
else:
    print(f'Ano {ano} NÃO É BISSEXTO')
