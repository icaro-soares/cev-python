"""
Faça um programa que leia o nome e a média de um aluno, guardando também a situação em um dicionário. No final mostre o conteúdo da estrutura na tela.
"""
ficha = {}
ficha['nome'] = str(input('Nome: ')).strip().capitalize()
ficha['média'] = float(input('Média: '))
if ficha['média'] <= 4.9:
    ficha['situação'] = 'REPROVADO'
elif 5 <= ficha['média'] <= 6.9:
    ficha['situação'] = 'RECUPERAÇÃO'
else:
    ficha['situação'] = 'APROVADO(A)'
print('-='*30)
for k, v in ficha.items():
    print(f'O campo {k} tem valor {v}')
