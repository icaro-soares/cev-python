def area(larg, comp):
    a = larg*comp
    print(f'A área do terreno é de {a:.2f}m²')


l = float(input('Qual a largura do terreno (m): '))
c = float(input('Qual o comprimento do terreno (m): '))
area(l, c)
