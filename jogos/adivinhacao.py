import os
from random import randint
from time import sleep

while True:
    número_secreto = randint(0, 100)
    tentativas = 0
    pontos = 1000 #pontuação será subtração da diferença entre o chute e o número secreto
    acertou = False
    print('-='*30)
    print(f'{"Jogo da adivinhação":^60}')
    print('-='*30)
    dificuldade = int(input('Escolha a dificuldade [1 - Fácil][2 - Médio][3 - Difícil]: '))
    match dificuldade:
        case 1:
            chances = 20
            print('Dificuldade fácil: 20 chances')
        case 2:
            chances = 10
            print('Dificuldade média: 10 chances')
        case 3:
            chances = 5
            print('Dificuldade difícil: 5 chances')
        case _:
            print('Comando desconhecido, reinicie o programa e tente novamente!')
            exit()
    while not acertou:
        chute = int(input('Diga seu chute: '))
        tentativas+=1
        chances-=1
        if chute == número_secreto:
            print('Você acertou!')
            print(f'Número de tentativas: {tentativas}')
            acertou = True
        else:
            if chute < número_secreto:
                pontos-=(número_secreto - chute) 
                print('Mais...')
            elif chute > número_secreto:
                pontos-=(chute - número_secreto)
                print('Menos...')
            if pontos <= 0 or chances == 0:
                print(f'Você perdeu! Sua pontuação foi zerada! O número é: {número_secreto}')
                pontos = 0
                break
    print(f'Pontuação final: {pontos}')
    print('-='*60)
    resp = ' '
    while resp not in 'SsNn':
        resp = str(input('Quer jogar de novo [S/N]? ')).strip()[0]
    if resp in 'Nn':
        print('Saindo...')
        sleep(3)
        break
    elif resp in 'Ss':
        os.system('cls' if os.name == 'nt' else 'clear')
        