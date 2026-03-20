#idade aposentar = 65
from datetime import date

ficha = {}
ficha['nome'] = str(input('Nome: ')).strip()
nasc = int(input('Ano de nascimento: '))
ficha['idade'] = date.today().year - nasc
ficha['ctps'] = int(input('CTPS: '))
if ficha['ctps'] != 0:
    ficha['contratação'] = int(input('Ano de contratação: '))
    ficha['salário'] = float(input('Salário: R$ '))
    ficha['aposentadoria'] = ficha['idade'] + ((ficha['contratação'] + 65) - date.today().year)
print('-='*30)
for k, v in ficha.items():
    print(f'\t- {k} tem valor {v}')
