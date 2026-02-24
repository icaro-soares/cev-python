"""
Docstring for ex020
O mesmo professor do desafio anterior quer sortear
a ordem de apresentação de trabalhos dos alunos.
Faça um programa que leia o nome dos quatro alunos
e mostre a ordem sorteada.
"""
from random import shuffle


aluno_um = str(input('Nome do 1º aluno: '))
aluno_dois = str(input('Nome do 2º aluno: '))
aluno_três = str(input('Nome do 3º aluno: '))
aluno_quatro = str(input('Nome do 4º aluno: '))
alunos = [aluno_um, aluno_dois, aluno_três, aluno_quatro]
shuffle(alunos)
print(f'Ordem de apresentação: {alunos}')
