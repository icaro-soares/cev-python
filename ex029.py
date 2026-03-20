velocidade = float(input('Velocidade (km/h): '))
if velocidade > 80:
    print('Você foi multado!')
    valor = (velocidade - 80) * 7
    print(f'Valor da multa: R${valor:.2f}')
