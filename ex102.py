"""
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show, que terá um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
"""
def fatorial(num):
    fat = 1
    for c in range(num, 0, -1):
        print(c, end=' ')
        fat*=c
    return fat
n = int(input('Digite um número: '))
f = fatorial(n)
print(f'Mostrando {n}!: {f}')
