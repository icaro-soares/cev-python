"""A Confederação Nacional de Natação precisa de um programa que leia o
ano de nascimento de um atleta e mostre a categoria de acordo com a idade
Até 9 anos MIRIM
Até 14 anos INFANTIL
Até 19 anos JÚNIOR
Até 25 anos SÊNIOR
Acima MASTER"""
from datetime import date

nascimento = int(input('Nascimento: '))
idade = date.today().year - nascimento
print(f'Sua idade: {idade}\nVocê se encaixa na catergoria: ', end='')
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JÚNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')
