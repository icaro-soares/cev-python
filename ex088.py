"""
Docstring for ex088
Crie um programa que gere palpites da mega sena.
O programa vai perguntar quantos jogos devem ser gerados,
e vai sortear números entre 0 e 60 para cada jogos
cadastrando-os em uma lista composta.
"""
from random import randint
from time import sleep

lista = []
lista_jogos = []
qntd = int(input('Quantos jogos devo fazer? '))
tot = 1
while tot <= qntd:
    c = 0
    while True:
        núm = randint(1, 60)
        if núm not in lista:
            lista.append(núm)
            c+=1
        if c >= 6:
            break
    lista.sort()
    lista_jogos.append(lista[:])
    lista.clear()
    tot+=1
print('-='*30)
print(f'{"SORTEANDO JOGOS":^60}')
print('-='*30)
for i, j in enumerate(lista_jogos):
    print(f'Jogo {i+1}: {j}')
    sleep(1)
