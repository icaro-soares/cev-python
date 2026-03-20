lista = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Continuar [S/N]: ')).strip().upper()[0]
    if resp == 'N':
        break
print('-='*30)
print(f'Foram digitado {len(lista)} números')
print('-='*30)
print(f'Lista em ordem decrescente: {sorted(lista, reverse=True)}')
print('-='*30)
if 5 in lista:
    print(f'O valor 5 está na lista')
else:
    print('O valor 5 não está na lista')
    