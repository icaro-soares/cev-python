dist = float(input('Distância (km): '))
if dist <= 200:
    valor = dist * 0.50
else:
    valor = dist * 0.40
print(f'O valor da passagem é de R${valor:.2f}')
