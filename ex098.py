def contador(i=1, f=10, p=1):
    if p < 0:
        p *= -1
    if p == 0:
        p = 1
    if i < f:
        while i <= f:
            print(f'{i} ', end='')
            i+=p
        print('Fim!')
    elif i > f:
        while i >= f:
            print(f'{i} ', end='')
            i-=p
        print('Fim!')


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é sua vez!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo) 
