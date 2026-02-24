"""
Docstring for ex085
Crie um programa que leia 7 valores numéricos
e cadastre-os em uma lista única que mantenha
separado os valores pares e ímpares.
No final mostre os valores pares e ímpares
em ordem crescente.
"""
núm = [[], []]
for c in range(0, 7):
    valor = int(input('Digite um valor: '))
    if valor % 2 == 0:
        núm[0].append(valor)
    else:
        núm[1].append(valor)
print('-='*30)
print(f'Sua lista: {núm}')
