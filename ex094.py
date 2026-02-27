"""
Crie um programa que leia o nome, sexo e idade de várias pessoas, guardando tudo em um dicionário e todos os dicionários em uma lista. No final mostre:
a) Quantas pessoas foram cadatradas
b) A média de idade do grupo
c) Uma lista com todas as mulheres
d) Uma lista com todas as pessoas acima da média
"""
ficha = {}
lista = []
lista_mulheres = []
acima_média = []
soma_idade = 0
while True:
    ficha['nome'] = str(input('Nome: ')).strip()
    ficha['sexo'] = ' '
    while ficha['sexo'] not in 'MmFf':
        ficha['sexo'] = str(input('Sexo [M/F]: ')).strip()[0]
    if ficha['sexo'] in 'Ff':
        lista_mulheres.append(ficha['nome'])
    ficha['idade'] = int(input('Idade: '))
    soma_idade+=ficha['idade']
    lista.append(ficha.copy())
    r = ' '
    while r not in 'SsNn':
        r = str(input('Quer continuar [S/N]: ')).strip()[0]
    if r in 'Nn':
        break
print('-='*30)
print(f'Pessoas cadastradas: {len(lista)}')
média_idade = soma_idade/len(lista)
if ficha['idade'] > média_idade:
    acima_média.append(ficha['nome'])
print(f'Média de idade: {média_idade:.0f} anos')
print(f'Lista de mulheres:')
for m in lista_mulheres:
    print(f'\t{m}')
print(f'Lista de pessoas acima da média:')
for p in acima_média:
    print(f'\t{p}')
