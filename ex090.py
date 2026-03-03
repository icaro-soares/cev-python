"""
Faça um programa que leia o nome e a média de um aluno, guardando também a situação em um dicionário. No final mostre o conteúdo da estrutura na tela.
"""
ficha = {}
ficha['nome'] = str(input('Nome: ')).strip()
ficha['média'] = float(input('Média: '))
ficha['situação'] = ' '
if ficha['média'] >= 7.0:
    ficha['situação'] = 'Aprovado'
elif 5.0 <= ficha['média'] <= 6.9:
    ficha['situação'] = 'Recuperação'
else:
    ficha['sitação'] = 'Reprovado'
print('-='*30)
for k, v in ficha.items():
    print(f'{k} tem valor {v}')
