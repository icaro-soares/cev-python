"""
Melhore o jogo do desafio 028, onde o computador vai 'pensar' em um número
entre 0 e 10. Só que agora o jogador vai tentar adivinhar até acertar,
mostrando no final quantos palpites foram necessários para vencer
"""
from random import randint

cpu = randint(0, 10)
print('Pensei em um número, tente adivinhá-lo.')
palpites = 0
acertou = False
while not acertou:
    chute = int(input('Seu palpite: '))
    palpites += 1
    if chute == cpu:
        print('Você acertou!')
        acertou = True
    else:
        print('Você errou!', end=' ')
        if chute < cpu:
            print('Mais...')
        else:
            print('Menos...')
print(f'Acertou em {palpites} tentativas.')
