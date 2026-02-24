"""
Docstring for ex004
Faça um programa que leia algo pelo teclado e mostre na tela seu tipo
primitivo e todas as informações sobre ela
"""
algo = input('Digite algo: ')
print(type(algo))
print(f'É um número? {algo.isnumeric()}')
print(f'É alfabético? {algo.isalpha()}')
print(f'É alfanumérico? {algo.isalnum()}')
print(f'Está em maiúsculas? {algo.isupper()}')
print(f'Está em minúsculas? {algo.islower()}')
