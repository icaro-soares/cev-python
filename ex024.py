"""Crie um programa que leia o nome de uma cidade e diga se
ela começa ou não com 'SANTO' """
cidade = str(input('Cidade: ')).strip().title()
print(f'Começa com "Santo"? {cidade.startswith('Santo')}')
