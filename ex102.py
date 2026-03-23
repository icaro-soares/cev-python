def fatorial(num, show=True):
    fat = 1
    for c in range(num, 0, -1):
        if show:
            if c >= 1: print(f'{c} ', end='')
            if c > 1: print('x ', end='')
            else: print('= ', end='')
        fat*=c
        
        
    return fat
n = int(input('Digite um número: '))
print(f'Mostrando {n}!')
f = fatorial(n, show=False)
print(f'{f}')
