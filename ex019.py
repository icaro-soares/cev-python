"""
Docstring for ex019
Um professor quer sortear um dos seus quatro alunos
para apagar o quadro. Faça um programa que ajude ele,
lendo o nome dos alunos e escrevendo o nome do escolhido
"""
from random import choice


aluno_um = str(input('Nome do 1º aluno: '))
aluno_dois = str(input('Nome do 2º aluno: '))
aluno_três = str(input('Nome do 3º aluno: '))
aluno_quatro = str(input('Nome do 4º aluno: '))
alunos = [aluno_um, aluno_dois, aluno_três, aluno_quatro]
print(f'O aluno sorteado foi {choice(alunos)}')
