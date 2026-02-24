"""Faça um programa que leia um número qualquer e mostre o seu fatorial"""
#Usando o while
m = 1
n = int(input('Digite um número: '))
print(f'{n}! = ', end='')
while n >= 1:
    print(f'{n}', end='')
    m *= n
    n -= 1
    print(' x ' if n >= 1 else ' = ', end='')
print(m)
print('-='*30)
#Usando o for
n = int(input('Digite um valor: '))
m = 1
print(f'{n}! = ', end='')
for c in range(n, 0, -1):
    print(c, end='')
    m *= c
    print(' x ' if c >1 else ' = ', end='')
print(m)
