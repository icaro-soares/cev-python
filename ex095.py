"""
Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador
"""
jogador = {}
gol = []
jogador['nome'] = str(input('Nome: '))
part = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, part):
    gol.append(int(input(f'Gols na partida {c+1}: ')))
jogador['gols'] = gol[:]
jogador['total'] = sum(gol)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} jogou {part} partidas.')
for k, v in enumerate(gol):
    print(f'\tNa partida {k+1} fez {v} gols.')
print('-='*30)
