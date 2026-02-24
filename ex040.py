"""Crie um programa que leia duas notas de um aluno e calcule sua média.
De acordo com a média atingida mostre uma mensagem:
Média abaixo de 5.0 REPROVADO
Média entre 5.0 e 6.9 RECUPERAÇÃO
Média 7.0 ou superior APROVADO"""
n1 = float(input('1ª nota: '))
n2 = float(input('2ª nota: '))
m = (n1 + n2) / 2
print(f'Sua média é {m:.1f}')
if m < 5:
    print('REPROVADO')
elif 5 <= m < 7:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')
