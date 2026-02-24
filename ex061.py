"""Refaça o desafio 051, lendo o primeiro termo e a razão de uma PA,
mostrando os 10 primeiros termos da progressão usando a estrutura while
a = primeiro termo
b = n ésimo termo
p = posição do termo que quer calcular
r = razão
fórmula: b = a + (p - 1) * r"""
primeiro = int(input('Primeiro termo da PA: '))
razão = int(input('Razão da PA: '))
c = 1
while c <= 10:
    print(f'{primeiro} → ', end='')
    primeiro += razão
    c +=1
print('FIM')
