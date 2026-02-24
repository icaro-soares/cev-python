"""Refaça o desafio 035 dos triângulos acrescentando o recurso de mostrar que
tipo de triângulo será formado:
Equilátero: todos os lados iguais
Isóceles: Dois lados iguais
Escaleno: Todos os lados diferentes"""
r1 = float(input('1º lado: '))
r2 = float(input('2º lado: '))
r3 = float(input('3º lado: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('Pode formar um triângulo ', end='')
    if r1 == r2 == r3:
        print('Equilátero!')
    elif r1 != r2 != r3 != r1:
        print('Escaleno!')
    else:
        print('Isóceles!')
else:
    print('Não pode formar um triângulo')
