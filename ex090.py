"""
Faça um programa que leia o nome e a média de um aluno, guardando também a situação em um dicionário. No final mostre o conteúdo da estrutura na tela.
"""
boletim = {}
boletim['aluno'] = str(input('Nome: ')).strip()
boletim['média'] = float(input('Média: '))
if boletim['média'] >= 7.0:
    boletim['situação'] = 'Aprovado(a)'
elif 5.0 <= boletim['média'] <= 6.9:
    boletim['situação'] = 'Recuperação'
else:
    boletim['situação'] = 'Reprovado(a)'
print(boletim)
