km = float(input('Quantos km foram rodados com o carro? '))
dias = int(input('Quantos dias foi alugado? '))
total = (km * 0.15) + (dias * 60)
print(f'O preço total a se pagar é R${total:.2f}')
