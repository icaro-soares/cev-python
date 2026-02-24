"""
Docstring for ex007
Desenvolva um programa que leia as
duas notas de um aluno, calcule e mostre sua média
"""
n1 = float(input('Digite a 1ª nota: '))
n2 = float(input('Digite a 2ª nota: '))
média = (n1 + n2)/2
print('-='*20)
print(f'O aluno com nota {n1:.1f} e {n2:.1f} vai ter média de {média:.1f}')
