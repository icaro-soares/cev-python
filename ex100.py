from random import randint


def sorteia(lista):
    cont = 0
    while cont <= 4:
        lista.append(randint(0, 30))
        cont+=1
    print(f'Seus números foram {lista}')


def somaPar(soma_pares, lista):
    for n in lista:
        if n%2==0:
            soma_pares.append(n)
    print(f'A soma dos valores pares é {sum(soma_pares)}')


números = []
sorteia(números)
npares = []
somaPar(npares, números)
