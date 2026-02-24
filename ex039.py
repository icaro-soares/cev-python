"""Faça um programa que leia o ano de nascimento de um jovem e informe,
de acordo com a idade:
Se ele ainda vai se alistar ao serviço militar
Se é hora de se alistar
Se já passou do tempo do alistamento
Seu programa também deverá mostrar o tempo que falta ou que se passou do prazo
"""
from datetime import date

nascimento = int(input('Ano de nascimento: '))
sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
idade = date.today().year - nascimento
print(f'Sua idade é {idade} anos.')
if sexo == 'M':
    if idade <= 17:
        print('Você ainda vai se alistar')
        falta = 18 - idade
        print(f'Ainda faltam {falta} anos para o alistamento')
    elif 18 <= idade < 30:
        print('Já é hora de se alistar!')
    elif idade >= 30:
        print('Já passou do tempo do alistamento!')
        passou = idade - 18
        print(f'Já se passaram {passou} anos desde o alistamento')
elif sexo == 'F':
    print('Alistamento não obrigatório!')
