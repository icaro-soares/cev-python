"""
Faça um programa que leia o sexo de uma pessoa, mas que só aceite valores
'M' ou 'F'. Caso esteja errado, peça a digitação novamente até ser um valor
correto.
"""
sexo = str(input('Digite seu sexo: ')).strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Sexo inválido. Digite seu sexo novamente: '))
print(f'Sexo: {sexo} cadastrado.')
