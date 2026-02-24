"""Crie um programa que leia vários números inteiros pelo teclado. No final
da execução mostre a média entre todos os valores e qual foi o maior e o menor
valor lido. O programa deve perguntar ao usuário se ele quer ou não
continuar a digitar o valores"""
resp = 's'
c = s = maior = menor = 0
while resp == 's':
    n = int(input('Digite um valor: '))
    s += n
    c += 1
    if c == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    resp = str(input('Quer continuar [s/n]: ')).strip().lower()[0]
m = s/c
print(f'A média entre eles é {m:.2f}.')
print(f'A soma dos valores é {s}.')
print(f'O maior valor é {maior} e o menor é {menor}.')
