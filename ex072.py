"""
Crie um programa que tenha uma tupla totalmente preenchida com uma contagem
por extenso, de zero até vinte. Seu programa deverá ler um número pelo teclado
e mostrá-lo escrito por extenso.
"""
números = (
        'zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito',
        'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis',
        'dezessete', 'dezoito', 'dezenove', 'vinte'
)
while True:
    n = int(input('Digite um valor [0 a 20]: '))
    if n in range(len(números)):
        print(f'Número por extenso: {números[n]}')
    else:
        n = int(input('Digite um valor [0 a 20]: '))
    r = ' '
    while r not in 'SsNn':
        r = str(input('Quer continuar [S/N]: ')).strip()[0]
    if r in 'Nn':
        break
    