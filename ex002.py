"""
Docstring for ex002
Pergunte o nome de uma pessoa e escreva uma mensagem de boas vindas
"""
nome = str(input('Qual seu nome? '))
print(f'É um prazer te conhecer, \033[4;34m{nome.title()}!\033[m')
