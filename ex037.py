n = int(input('Número: '))
escolha = int(input('''Escolha a base de conversão
[1] Binário
[2] Octal
[3] Hexadecimal: '''))
if escolha == 1:
    print(f'Binário: {bin(n)[2:]}')
elif escolha == 2:
    print(f'Octal: {oct(n)[2:]}')
elif escolha == 3:
    print(f'Hexadecimal: {hex(n)[2:]}')
else:
    print('Escolha inválida!')
