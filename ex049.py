n = int(input('Digite um valor: '))
print('-=' * 30)
print(f'Tabuada de {n}'.center(30))
for c in range(0, 11):
    print(f'{c:2} x {n} = {c*n:3}')
print('-=' * 30)
