"""
Docstring for ex014
Escreva um programa que converta uma temperatura digitada em °C
e converta para °F
"""
#formula: (c * 1,8) + 32 ou (c * 9 / 5) + 32
c = float(input('Qual a temperatura de hoje? '))
f = (c * 1.8) + 32
print(f'Sua temperatura em graus Farenheit é °{f}')
