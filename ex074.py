"""
Crie um programa que gere cinco números aleatórios e guarde-os em uma tupla.
Depois disso mostre uma listagem com os números gerados e também indique o
maior e o menor valor.
"""
from random import randint

n = (
        randint(0, 10), randint(0, 10), randint(0, 10),
        randint(0, 10), randint(0, 10)
)
print(f'Sua tupla: {n}')
print('-='*30)
print(f'O maior valor da tupla é: {max(n)}')
print(f'O menor valor da tupla é: {min(n)}')
