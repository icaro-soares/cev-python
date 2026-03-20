#fórmula: b = a + (p - 1) * r
a = int(input('Digite o primeiro termo: '))
r = int(input('Digite a razão da PA: '))
b = a + (11 - 1) * r
for c in range(a, b, r):
    print(c, end='  ')
