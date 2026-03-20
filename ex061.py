#fórmula: b = a + (p - 1) * r
primeiro = int(input('Primeiro termo da PA: '))
razão = int(input('Razão da PA: '))
c = 1
while c <= 10:
    print(f'{primeiro} → ', end='')
    primeiro += razão
    c +=1
print('FIM')
