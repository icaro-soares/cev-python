c = s = 0
while True:
    n = int(input('Digite um valor [999 p/ parar]: '))
    if n != 999:
        s += n
        c += 1
    else:
        print('Finalizando...')
        break
print('-='*30)
print(f'Foram digitados {c} números e a soma entre eles é {s}.')
