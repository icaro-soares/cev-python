"""Desenvolva um programa que pergunte a distância de uma viagem
em km. Calcule o preço da passagem cobrando R$0.50 por km para viagens
de até 200km e R$0.40 para viagens mais longas"""
dist = float(input('Distância (km): '))
if dist <= 200:
    valor = dist * 0.50
else:
    valor = dist * 0.40
print(f'O valor da passagem é de R${valor:.2f}')
