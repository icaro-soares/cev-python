"""Faça um programa que leia uma frase pelo teclado e mostre:
1. Quantas vezes aparece a letra 'A'
2. Em que posição ela aparece a primeira vez
3. Em que posição ela aparece a última vez"""
frase = str(input('Digite uma frase: ')).strip().upper()
print(f'A letra "A" aparece {frase.count("A")} vezes')
print(f'A letra "A" aparece pela primeira vez na posição {frase.find("A")}')
print(f'A letra "A" aparece pela última vez na posição {frase.rfind("A")}')
