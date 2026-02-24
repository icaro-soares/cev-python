"""
Docstring for ex008
Escreva um programa que leia um valor em metros
e o exiba convertido em centímetros e
milímetros
"""
metros = float(input('Digite um valor em metros (m): '))
km = metros / 1000
hm = metros / 100
dam = metros / 10
dm = metros * 10
cm = metros * 100
mm = metros * 1000
print('-='*20)
print(f'{km}km')
print(f'{hm}hm')
print(f'{dam}dam')
print(f'{metros}m')
print(f'{dm}dm')
print(f'{cm}cm')
print(f'{mm}mm')
