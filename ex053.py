"""Crie um programa que leia uma frase qualquer e diga se ele é ou não um
palíndromo, frase que lê-se indiferentemente de trás pra frente ou vice-versa,
desconsiderando os espaços"""
frase = str(input('Frase: ')).strip().lower()
junto = ''.join(frase.split())
if junto == junto[::-1]:
    print('A frase é um palíndromo')
else:
    print('A frase não é um palíndromo')
