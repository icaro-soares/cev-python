valor = float(input('Valor da casa: R$'))
sal = float(input('Salário: R$'))
anos = int(input('Anos pagar: '))
prestação = valor / (anos * 12)
if prestação > (sal * 0.30):
    print('Empréstimo negado!')
else:
    print('Empréstimo aprovado!')
    print(f'Valor da prestação R${prestação:.2f}')
