"""
Docstring for ex079
Crie um programa onde o usuário possa digitar vários
valores numéricos e guarde-os em uma lista. Caso o
número já exista lá dentro, ele não será adicionado.
No final serão exibidos todos os valores em ordem
crescente.
"""
lista = []
while True:
    n = int(input('Digite um valor: '))
    if n not in lista:
        lista.append(n)
        print('Número adicionado com sucesso!')
    else:
        print('O número já existe na lista.')
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Quer continuar [S/N]: ')).strip()[0]
    if resp in 'Nn':
        break
print('-='*30)
print(f'Sua lista: {sorted(lista)}')
