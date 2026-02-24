"""
Docstring for ex078
Crie uma lista que leia 5 valores numéricos.
No final mostre o maior e o menor valor e suas
posições.
"""
from rich import print

#criação automática
lista1 = list(range(0, 5)) 
print(f'Sua lista: {lista1}')
print(f'Maior valor: {max(lista1)}')
print(f'Menor valor: {min(lista1)}')
print('-='*30)
#criação com interação do usuário
lista2 = []
maior = menor = 0
for c in range(0, 5):
    lista2.append(int(input(f'{c+1}º valor: ')))
    if c == 0:
        maior = menor = lista2[c]
    else:
        if lista2[c] > maior:
            maior = lista2[c]
        if lista2[c] < menor:
            menor = lista2[c]
print(f'Sua lista: {lista2}')
print(f'Maior valor: {maior}, nas posições: ', end='')
for i, v in enumerate(lista2):
    if v == maior:
        print(f'{i}... ', end='')
print(f'\nMenor valor: {menor}, nas posições: ', end='')
for i, v in enumerate(lista2):
    if v == menor:
        print(f'{i}... ', end='')
