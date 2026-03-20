sexo = str(input('Digite seu sexo: ')).strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Sexo inválido. Digite seu sexo novamente: '))
print(f'Sexo: {sexo} cadastrado.')
