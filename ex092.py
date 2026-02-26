"""
Crie um programa que leia o nome, ano de nascimento e carteira de trabalho e cadastre-os com idade em um dicionário. Se a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""
#idade aposentar = 65

from datetime import date

ficha = {}
ficha['nome'] = str(input('Nome: ')).strip().title()
nasc = int(input('Ano de nascimento: '))
ficha['idade'] = date.today().year - nasc
ficha['ctps'] = int(input('Número da CTPS: '))
if ficha['ctps'] != 0:
    ficha['contratação'] = int(input('Ano de contratação: '))
    ficha['salário'] = float(input('Salário: R$ '))
    ficha['aposentadoria'] = 65 - ficha['idade']
print('-='*30)
for k, v in ficha.items():
    print(f'{k} tem valor {v}')
