"""
Docstring for ex015
Escreva um programa que pergunte a quantidade de km percorridos
por um carro alugado e a quantidade de dias pelos quais ele
foi alugado. Calcule o preço a pagar, sabendo que o carro custa
R$60 por dia e R$0.15 por km rodado.
"""
km = float(input('Quantos km foram rodados com o carro? '))
dias = int(input('Quantos dias foi alugado? '))
total = (km * 0.15) + (dias * 60)
print(f'O preço total a se pagar é R${total:.2f}')
