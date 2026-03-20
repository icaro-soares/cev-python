carteira = float(input('Quantos reais têm na carteira? R$'))
dólar = carteira/5.38
euro = carteira/6.28
iene = carteira/0.034
print(f'Com esse valor posso comprar US${dólar:.2f} Dólares')
print(f'Com esse valor posso comprar €{euro:.2f} Euros')
print(f'Com esse valor posso comprar ¥{iene:.2f} Ienes')
