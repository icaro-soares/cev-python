"""Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão
a = primeiro termo
b = n ésimo termo
p = posição do termo que quer calcular
r = razão
fórmula: b = a + (p - 1) * r"""
a = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))
b = a + (11 - 1) * r
for c in range(a, b, r):
    print(c, end='  ')
