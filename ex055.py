maior = menor = 0
for c in range(1, 6):
    peso = float(input(f'Peso {c}ª pessoa: '))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print(f'Maior peso de: {maior}kg')
print(f'Menor peso de: {menor}kg')
