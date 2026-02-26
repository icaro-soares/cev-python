"""
Faça um programa que leia o nome e a média de um aluno, guardando também a situação em um dicionário. No final mostre o conteúdo da estrutura na tela.
"""
aluno = {}
aluno['nome'] = str(input('Nome: ')).strip()
aluno['média'] = float(input('Média: '))
if aluno['média'] >= 7:
    aluno['situação'] = 'Aprovado(a)'
elif 5 <= aluno['média'] <= 6.9:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado(a)'
print('-=')
for k, v in aluno.items():
    print(f'A chave: {k} tem valor: {v}')
