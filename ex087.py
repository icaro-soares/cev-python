"""
Docstring for ex087
Aprimore o desafio anterior, mostrando no final:
a) A soma de todos os valores pares
b) A soma dos valores da terceira coluna
c) O maior valor da segunda coluna
"""
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
somapar = scol = mai = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}][{c}]: '))
        if matriz[l][c] % 2 == 0:
            somapar += matriz[l][c]
        if matriz[l][2]:
            scol += matriz[l][c]
        if matriz[l][1]:
            if matriz[l][1] > mai:
                mai = matriz[l][1]
print('-='*30)
print(f'{"Matriz":^60}'.upper())
print('-='*30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()
print('-='*30)
print(f'A soma dos pares é {somapar}')
print(f'Soma dos valores da terceira coluna: {scol}')
print(f'O maior valor da segunda coluna é {mai}')
