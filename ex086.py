"""
Docstring for ex086
Crie um programa que crie uma matriz 3x3
e preencha com valores lidos pelo teclado.
No final mostre a matriz com a formatação correta.
"""
lista = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
for p in range(0, 3):
    for q in range(0, 3):
        lista[p][q] = int(input(f'Digite um número para posição ({p}, {q}): '))
print('-='*30)
print(f'{"Matriz":^60}'.upper())
print('-='*30)
for p in range(0, 3):
    for q in range(0, 3):
        print(f'[{lista[p][q]:^5}]', end='')
    print()