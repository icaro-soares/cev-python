"""
Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma
tupla. No final mostre:
a) Quantas vezes apareceu o número 9
b) Em que posição foi digitado o valor 3
c) Quais foram os números pares
"""
n = (
        int(input('1º valor: ')), int(input('2º valor: ')),
        int(input('3º valor: ')), int(input('4º valor: '))
)
print(f'Sua tupla: {n}')
print('-='*30)
print(f'O valor 9 apareceu {n.count(9)} vezes.')
print('-='*30)
if 3 in n:
    print(f'O valor 3 apareceu na posição: {n.index(3)}')
else:
    print('O valor 3 não está na tupla')
print('-='*30)
print('Os valores pares são: ', end='')
for núm in n:
    if núm % 2 == 0:
        print(núm, end=' ')
        