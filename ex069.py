total_18 = tot_h = menos_20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = ' '
    while sexo not in 'MmFf':
        sexo = str(input('Sexo [M/F]: ')).strip()[0]
    if idade > 18:
        total_18 += 1
    if sexo in 'Mm':
        tot_h += 1
    if sexo in 'Ff' and idade < 20:
        menos_20 += 1
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Quer continuar [S/N]: ')).strip()[0]
    if resp in 'Nn':
        break
print('-='*30)
print(f'{total_18} pessoas têm mais de dezoito anos')
print(f'{tot_h} homens foram cadastrados.')
print(f'E {menos_20} mulheres têm menos de 20 anos.')
