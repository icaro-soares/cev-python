preço = float(input('Valor: R$'))
print(f'O produto tem valor de R${preço:.2f}')
novo_preço = preço - (preço * 5/100)
print(f'Com desconto o novo preço será de R${novo_preço:.2f}')
