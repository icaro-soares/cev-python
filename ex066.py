"""
Crie um programa que leia vários números inteiros
pelo teclado. O programa só irá parar quando o valor 999
for digitado. No final mostre quantos números foram
digitados e a soma entre eles.
"""
c = s = 0
while True:
    n = int(input('Digite um valor [999 p/ parar]: '))
    if n != 999:
        s += n
        c += 1
    else:
        print('Finalizando...')
        break
print('-='*30)
print(f'Foram digitados {c} números e a soma entre eles é {s}.')
