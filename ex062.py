"""Melhore o desafio 061, perguntando para o usuário se ele quer mostrar mais
alguns termos. O programa vai encerrar quando ele disser que quer mostrar
0 termos"""
primeiro = int(input('Primeiro termo da PA: '))
razão = int(input('Razão: '))
c = 1
total = 0
mais = 10
while mais != 0:
    total += mais
    while c <= total:
        print(f'{primeiro} → ', end='')
        primeiro += razão
        c += 1
    print('PAUSA')
    mais = int(input('Quantos termos devo mostrar a mais: '))
print(f'Total de termos mostrados: {total}')
