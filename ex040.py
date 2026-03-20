n1 = float(input('1ª nota: '))
n2 = float(input('2ª nota: '))
m = (n1 + n2) / 2
print(f'Sua média é {m:.1f}')
if m < 5:
    print('REPROVADO')
elif 5 <= m < 7:
    print('RECUPERAÇÃO')
else:
    print('APROVADO')
