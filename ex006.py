"""
Docstring for ex006
Crie um algoritmo que leia um número e mostre
o seu dobro, triplo e raiz quadrada.
"""
número = int(input('Digite um valor: '))
dobro = número * 2
triplo = número * 3
raiz = número ** (1/2)
print(f'O número digitado foi {número}.', end=' ')
print(f'O dobro vale {dobro}, o triplo vale {triplo} e a sua raiz quadrada é {raiz}')
