frase = str(input('Frase: ')).strip().lower()
junto = ''.join(frase.split())
if junto == junto[::-1]:
    print('A frase é um palíndromo')
else:
    print('A frase não é um palíndromo')
