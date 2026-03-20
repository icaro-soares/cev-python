s = n = c = 0
while n != 999:
    n = int(input('Digite um número [999 p/ parar]: '))
    if n != 999:
        s += n
        c += 1
print(f'Você digitou {c} números, e a soma é {s}')
