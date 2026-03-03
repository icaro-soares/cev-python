"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai perguntar o nome do jogador de futebol e quantas partidas ele jogou. Depois vai ler a quantidade de gols em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""
jogador = {}
gols = []
jogador['nome'] = str(input('Nome do jogador: ')).strip()
jogador['partidas'] = int(input('Quantas partidas: '))
for c in range(jogador['partidas']):
    gol = int(input(f'Quantidade de gols na partida {c}: '))
    gols.append(gol)
jogador['gols'] = gols
print('-='*30)
for k, v in jogador.items():
    print(f'A chave {k} tem valor {v}')
