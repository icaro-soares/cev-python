"""
Crie um programa que leia o nome, ano de nascimento e carteira de trabalho e cadastre-os com idade em um dicionário. Se a CTPS for diferente de zero, o dicionário receberá também o ano de contratação e o salário. Calcule e acrescente, além da idade, com quantos anos a pessoa vai se aposentar.
"""
#idade aposentar = 65
from datetime import date

dados = {}
dados['nome'] = str(input('Nome: ')).strip()
dados['nascimento'] = int(input('Nascimento: '))
dados['idade'] = date.today().year - dados['nascimento']
dados['ctps'] = int(input('CTPS [0 não tem]: '))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    dados['salário'] = float(input('Salário: R$ '))
    dados['aposentadoria'] = 65 - dados['idade']
print('-='*30)
for k, v in dados.items():
    print(f'{k} tem valor {v}')
if dados['aposentadoria']:
    print(f'Ainda faltam {v} anos para se aposentar')
