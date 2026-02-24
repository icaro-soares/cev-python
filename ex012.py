"""
Docstring for ex012
Faça um algoritmo que leia um preço de um produto e
mostre seu novo preço com 5% de desconto.
"""
preço = float(input('Valor: R$'))
print(f'O produto tem valor de R${preço:.2f}')
novo_preço = preço - (preço * 5/100)
print(f'Com desconto o novo preço será de R${novo_preço:.2f}')
