"""
Docstring for ex083
Crie um programa que leia uma expressão qualquer
que use parênteses seu aplicativo deverá analisar
se a expressão passada está com os parênteses abertos
e fechados na ordem correta
"""
lista = []
expr = str(input('Digite uma expressão: ')).strip()
for s in expr:
    if s == '(':
        lista.append(s)
    elif s == ')':
        lista.pop()
if len(lista) == 0:
    print('A expressão é válida!')
else:
    print('A expressão é inválida!')
