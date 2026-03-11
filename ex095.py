"""
Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador
"""
jogador = {}
gols = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    for c in range(0, jogador['partidas']):
        gols.append(int(input(f'Quantos gols na partida {c+1}? ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    while True:
        resp = str(input('Quer continuar [S/N]: '))[0]
        if resp in 'SsNn':
            break
        print('ERRO! Apenas S ou N')
    if resp in 'Nn':
        break
print('-='*30)
print(jogador)
