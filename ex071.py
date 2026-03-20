valor = int(input('Qual valor a sacar: R$'))
total = valor
cédulas = 100
totalcéd = 0
while True:
    if total >= cédulas:
        total -= cédulas
        totalcéd += 1
    else:
        if totalcéd > 0:
            print(f'{totalcéd} cédulas de R${cédulas}')
        if cédulas == 100:
            cédulas = 50
        elif cédulas == 50:
            cédulas = 20
        elif cédulas == 20:
            cédulas = 10
        elif cédulas == 10:
            cédulas = 5
        elif cédulas == 5:
            cédulas = 1
        totalcéd = 0
        if total == 0:
            break
