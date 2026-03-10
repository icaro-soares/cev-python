"""
Crie um programa que leia o nome, sexo e idade de várias pessoas, guardando tudo em um dicionário e todos os dicionários em uma lista. No final mostre:
a) Quantas pessoas foram cadatradas
b) A média de idade do grupo
c) Uma lista com todas as mulheres
d) Uma lista com todas as pessoas acima da média de idade
"""
pessoa = {}
galera = []
soma = média = 0
while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Apenas M ou F!')
    pessoa['idade'] = int(input('Idade: '))
    soma+=pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar [S/N]: ')).upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Apenas S ou N.')
    if resp == 'N':
        break
print('-='*30)
print(f'a) Foram cadastradas {len(galera)} pessoas.')
média = soma/len(galera)
print(f'b) A média de idade é {média:5.2f}')
print(f'c) Lista com todas as mulheres ', end='')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]}', end=' ')
print(f'\nd) Lista de pessoas acima da média ', end='')
for p in galera:
    if p['idade'] >= média:
        for k, v in p.items():
            print(f'{k} = {v}', end='')
