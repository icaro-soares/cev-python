"""
Crie um programa que leia o nome, sexo e idade de várias pessoas, guardando tudo em um dicionário e todos os dicionários em uma lista. No final mostre:
a) Quantas pessoas foram cadatradas
b) A média de idade do grupo
c) Uma lista com todas as mulheres
d) Uma lista com todas as pessoas acima da média de idade
"""
ficha = {}
pessoas = []
mulheres = []
soma_idade = 0
while True:
    ficha['nome'] = str(input('Nome: ')).strip()
    ficha['sexo'] = ' '
    while ficha['sexo'] not in 'MF':
        ficha['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if ficha['sexo'] == 'F':
        mulheres.append(ficha['nome'])
    ficha['idade'] = int(input('Idade: '))
    soma_idade+=ficha['idade']
    pessoas.append(ficha.copy())
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('-='*30)
print(f'Foram cadastradas {len(pessoas)} pessoas')
media_idade = soma_idade/len(pessoas)
print(f'A média de idade do grupo é {media_idade:.0f}')
print('Lista de mulheres')
for m in mulheres:
    print(f'\t{m}')
