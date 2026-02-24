"""
Docstring for ex084
Faça um programa que leia o nome e o peso
de várias pessoas guardando tudo em uma lista.
No final mostre:
a) Quantas pessoas foram cadastradas
b) Uma listagem com as pessoas mais pesadas
c) Uma listagem com as pessoas mais leves
"""
temp = []
princ = []
mai = men = 0
while True:
    temp.append(str(input('Nome: ')).strip())
    temp.append(float(input('Peso(kg): ')))
    if len(princ) == 0:
        mai = men = temp[1]
    else:
        if temp[1] > mai:
            mai = temp[1]
        if temp[1] < men:
            men = temp[1]
    princ.append(temp[:])
    temp.clear()
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Quer continuar [S/N]: ')).strip()[0]
    if resp in 'Nn': 
        break
print('-='*30)
print(f'{len(princ)} pessoas cadastradas.')
print(f'Maior peso de {mai}kg. Peso de', end=' ')
for p in princ:
    if p[1] == mai:
        print(f'{p[0]}', end=' ')
print(f'\nMenor peso de {men}kg. Peso de', end=' ')
for p in princ:
    if p[1] == men:
        print(f'{p[0]}', end=' ')
