princ = []
par = []
impar = []
while True:
    princ.append(int(input('Digite um valor: ')))
    resp = str(input('Continuar [S/N]: ')).strip()[0]
    if resp in 'Nn':
        break
for i, v in enumerate(princ):
    if v % 2 == 0:
        par.append(v)
    else:
        impar.append(v)
print('-='*30)
print(f'Lista completa: {sorted(princ)}')
print(f'Lista de pares: {sorted(par)}')
print(f'Lista de ímpares: {sorted(impar)}')
