"""Desenvolva um programa que leia o comprimento de três retas e diga se
elas podem formar um triângulo ou não"""
a = float(input('Comprimento da reta 1: '))
b = float(input('Comprimento da reta 2: '))
c = float(input('Comprimento da reta 3: '))
if a + b > c and a + c > b and b + c > a:
    print('Pode formar um triângulo!')
else:
    print('Não pode formar um triângulo')
