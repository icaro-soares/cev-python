from math import hypot


cateto_oposto = float(input('Cateto oposto: '))
cateto_adjacente = float(input('Cateto adjacente: '))
hipotenusa = hypot(cateto_oposto, cateto_adjacente)
print(f'A hipotenusa vale: {hipotenusa:.2f}cm')
