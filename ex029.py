"""Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar a velocidade de 80lh/h exiba a mensagem que ele foi
multado. A multa vai custar R$7.00 por km ultrapassado."""
velocidade = float(input('Velocidade (km/h): '))
if velocidade > 80:
    print('Você foi multado!')
    valor = (velocidade - 80) * 7
    print(f'Valor da multa: R${valor:.2f}')
