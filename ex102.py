"""
Crie um programa que tenha uma função fatorial() que receba dois parâmetros: o primeiro que indique o número a calcular e o outro chamado show, que terá um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
"""
def fatorial(num, show=True):
    fat = 1
    for c in range(num, 0, -1):
        if show:
            if c >= 1: print(f'{c}! x ', end=' ') 
        fat*=c
        
        
    return fat
n = int(input('Digite um número: '))
f = fatorial(n, show=True)
print(f'{f}')
