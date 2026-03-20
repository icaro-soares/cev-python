from datetime import date

nascimento = int(input('Nascimento: '))
idade = date.today().year - nascimento
print(f'Sua idade: {idade}\nVocê se encaixa na catergoria: ', end='')
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JÚNIOR')
elif idade <= 25:
    print('SÊNIOR')
else:
    print('MASTER')
