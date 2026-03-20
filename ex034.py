salário = float(input('Salário: R$'))
print(f'Salário atual: R${salário:.2f}')
if salário <= 1250:
    novo_salário = salário + (salário * 0.15)
    print(f'Salário com aumento: R${novo_salário:.2f}')
else:
    novo_salário = salário + (salário * 0.10)
    print(f'Salário com aumento: R${novo_salário:.2f}')
