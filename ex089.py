"""
Docstring for ex089
Crie um programa que leia o nome e duas notas de vários alunos
e guarde tudo em uma lista composta. No final mostre um boletim
contendo a média de cada um e permita que o usuário
possa mostrar as notas de cada aluno individualmente.
"""
ficha = []
while True:
    nome = str(input('Nome: ')).strip()
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))
    média = (nota1 + nota2)/2
    ficha.append([nome, [nota1, nota2], média])
    resp = str(input('Quer continuar? ')).strip()[0]
    if resp in 'Nn':
        break
print('-='*30)
print(f'{"No.":<4}{"Aluno":<10}{"Média":>8}')
print('-'*26)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    print('-'*26)
    opc = int(input('Devo mostrar os dados de que aluno? [999 p/ parar] '))
    if opc == 999:
        print('Encerrando...')
        break
    else:
        if opc <= len(ficha) - 1:
            print(f'Mostrando notas de {ficha[opc][0]}: {ficha[opc][1]}')
