"""
Docstring for ex013
Faça um algoritmo que leia o salário de um funcionário e mostre
seu novo salário com 15% de aumento. 
"""
salário = float(input('Salário atual: R$'))
print(f'Seu salário é de R${salário:.2f}')
novo_salário = salário + (salário * 15/100)
print(f'Seu novo salário será de R${novo_salário:.2f}')
