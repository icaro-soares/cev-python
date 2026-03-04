"""
Crie um programa que leia o nome, sexo e idade de várias pessoas, guardando tudo em um dicionário e todos os dicionários em uma lista. No final mostre:
a) Quantas pessoas foram cadatradas
b) A média de idade do grupo
c) Uma lista com todas as mulheres
d) Uma lista com todas as pessoas acima da média de idade
"""
ficha = {}
pessoas = []
soma_idade = media_idade = 0
lista_mulheres = []
acima_media = []

while True:
    ficha['nome'] = str(input('Nome: ')).strip()
    ficha['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
    ficha['idade'] = int(input('Idade: '))
    pessoas.append(ficha.copy())

    if ficha['sexo'] == 'F':
        lista_mulheres.append(ficha['nome'])
    soma_idade+=ficha['idade']
    media_idade = soma_idade/len(pessoas)
    if ficha['idade'] > media_idade:
        acima_media.append(ficha['nome'])

    res = ' '
    while res not in 'SN':
        res = str(input('Quer continuar [S/N]: ')).strip().upper()[0]
    if res == 'N':
        break
print('-='*30)
print(f'Foram cadastradas {len(pessoas)} pessoas')
print(f'A média de idade do grupo é {media_idade:.0f}')
print('Lista de mulheres')
for m in lista_mulheres:
    print(f'\t{m}')
print('Pessoas acima da média de idade')
for p in acima_media:
    print(f'\t{p}')
