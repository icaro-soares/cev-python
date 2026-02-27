"""
Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai perguntar o nome do jogador de futebol e quantas partidas ele jogou. Depois vai ler a quantidade de gols em cada partida. No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
"""
c = 0
jogador = {}
jogador['nome']= str(input('Nome: ')).strip()
jogador['partidas'] = int(input('Nº de partidas: '))
while c < jogador['partidas']:
    jogador['gols'] = int(input(f'Gols na partida {c+1}: '))
    c+=1
print('-='*30)
for k, v in jogador.items():
    print(f'A chave [{k}] tem valor [{v}]')
