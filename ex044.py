preço = float(input('Preço: R$'))
forma_pgt = int(input('''Escolha a forma de pagamento 
[1 - À vista dinheiro/cheque][2 - À vista cartão][3 - Até 2x no cartão]
[4 - 3x ou mais no cartão]: '''))
if forma_pgt == 1:
    print('10% de desconto')
    novo_preço = preço - (preço * 0.10)
    print(f'R${novo_preço:.2f}')
elif forma_pgt == 2:
    print('5% de desconto')
    novo_preço = preço - (preço * 0.05)
    print(f'R${novo_preço:.2f}')
elif forma_pgt == 3:
    print('Até 2x no cartão. Preço normal')
    parcela = int(input('Em quantas vezes: '))
    total = preço / parcela
    print(f'{parcela}x parcelas de {total:.2f}')
elif forma_pgt == 4:
    print('3x ou mais no cartão. 20% de juros')
    parcela = int(input('Em quantas vezes: '))
    novo_preço = preço + (preço * 0.20)
    total = novo_preço / parcela
    print(f'Novo preço: R${novo_preço:.2f}')
    print(f'{parcela}x parcelas de {total:.2f}')
else:
    print('Operação inválida!')
