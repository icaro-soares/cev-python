total = mais_1000 = barato = c = 0
nome_barato = ' '
while True:
    produto = str(input('Produto: ')).strip()
    preço = float(input('Preço: R$'))
    total += preço
    c += 1
    if preço > 1000:
        mais_1000 += 1
    if c == 1 or preço < barato:
        barato = preço
        nome_barato = produto
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Quer continuar [S/N]: ')).strip()[0]
    if resp in 'Nn':
        print('Obrigado por comprar!')
        break
print('-='*30)
print(f'Total da compra: R${total:.2f}')
print(f'Produtos que custam mais de 1000: {mais_1000}')
print(f'O produto mais barato é {nome_barato} e custa R${barato:.2f}')
