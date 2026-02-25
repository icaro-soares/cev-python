"""
Crie um programa que leia o nome, ano de nascimento e carteira de trabalho e cadastre-os com idade em um dicionário, se a CTPS for diferente de zero. O dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""
#idade aposentar = 65

from datetime import date

dados = {}
dados['nome'] = str(input('Nome Completo: ')).strip().title()
nasc = int(input('Ano Nascimento: '))
dados['idade'] = date.today().year - nasc
dados['ctps'] = int(input('Nº da CTPS: '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['idade_contratação'] = dados['contratação'] - nasc
    dados['salário'] = float(input('Salário: R$ '))
    
print('-='*30)
for k, v in dados.items():
    print(f'{k}: {v}')
print('-='*30)

