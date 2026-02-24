"""Desenvolva um programa que leia seis números inteiros e mostre a soma
daqueles que forem pares. Se o valor digitado for ímpar, desconsidere-o"""
soma = 0
cont = 0
for c in range(0, 6):
    n = int(input(f'Digite o {c+1}º valor: '))
    if n % 2 == 0:
        cont += 1
        soma += n
print(f'Foram digitados {cont} valores pares que somam {soma}')
