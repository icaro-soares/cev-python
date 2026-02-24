"""Crie um Programa que leia um nome completo de alguém.
Mostre: 1. O nome com todas as letras maiúsculas
2. O nome com todas as letras minúsculas
3. Quantas letras ao total (sem espaços)
4. Quantas letras tem o primeiro nome"""
nome = str(input('Nome completo: ')).strip()
print(f'Seu nome em maiúsculas: {nome.upper()}')
print(f'Seu nome em minúsculas: {nome.lower()}')
nome_separado = nome.split()
nome_junto = ''.join(nome_separado)
print(f'O nome {nome}, no total tem {len(nome_junto)} letras')
print(f'O primeiro nome é {nome_separado[0]} e tem {len(nome_separado[0])} letras')
