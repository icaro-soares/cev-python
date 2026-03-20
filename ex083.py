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
