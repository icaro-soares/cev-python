"""
Faça um programa que mostre a tabuada de vários números.
O programa será interrompido quando um valor negativo
for digitado
"""
while True:
    n = int(input('Digite um número para ver sua tabuada: '))
    if n < 0:
        print('Obrigado por usar o programa!')
        break
    else:
        print('-='*30)
        for c in range (0, 11):
            print(f'{n} x {c:2} = {n*c:3}')
        print('-='*30)
    