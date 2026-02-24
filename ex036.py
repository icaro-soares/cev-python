"""Escreva um programa para aprovar o empréstimo bancário para a compra
de uma casa. O programa vai perguntar o valor da casa, o salário do
comprador e em quantos anos ele vai pagar. Calcule o valor da prestação mensal
sabendo que ela não pode exceder 30% do salário ou então o empréstimo será
negado"""
valor = float(input('Valor da casa: R$'))
sal = float(input('Salário: R$'))
anos = int(input('Anos pagar: '))
prestação = valor / (anos * 12)
if prestação > (sal * 0.30):
    print('Empréstimo negado!')
else:
    print('Empréstimo aprovado!')
    print(f'Valor da prestação R${prestação:.2f}')
