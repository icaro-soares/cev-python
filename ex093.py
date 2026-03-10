"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai perguntar o nome do jogador de futebol e quantas partidas ele jogou. Depois vai ler a quantidade de gols em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""
jogador = {}
gols = []
jogador['nome'] = str(input('Nome do jogador: ')).strip()
jogador['partidas'] = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, jogador['partidas']):
    gols.append(int(input(f'Gols na partida {c+1}: ')))
jogador['gols'] = gols
jogador['total'] = sum(gols)
print('-='*30)
print(jogador)
print('-='*30)
for k, v in jogador.items():
    print(f'O campo {k} tem valor {v}')
print('-='*30)
print(f'O jogador {jogador["nome"]} fez {jogador["partidas"]} partidas.')
for gol in enumerate(gols):
    print(f'\tNa partida {gol[0]} fez {gol[1]} gols')
print(f'Foi um total de {jogador["total"]} gols.')
