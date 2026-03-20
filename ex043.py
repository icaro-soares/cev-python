#Fórmula = peso/altura**2
altura = float(input('Altura: '))
peso = float(input('Peso: '))
imc = peso / (altura ** 2)
print(f'Seu IMC é: {imc:.1f}')
if imc < 18.5:
    print('Abaixo do peso')
elif 18.5 <= imc < 25:
    print('Peso ideal')
elif 25 <= imc < 30:
    print('Sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')
