"""
Aprimore o desafio 093 para que ele funcione com vários jogadores, incluindo um sistema de visualização de detalhes do aproveitamento de cada jogador
"""
time = []
jogador = {}
partidas = []

while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome: '))
    tot = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f'Gols na partida {c+1}: ')))
    jogador['gols'] = partidas[:]
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())
    while True:
        resp = str(input('Quer continuar [S/N]? ')).strip()[0]
        if resp in 'SsNn':
            break
        print('Erro! Apenas S ou N!')
    if resp in 'Nn':
        break
print('-='*30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print(f'-='*40)
for k, v in enumerate(time):
    print(f'{k:>3} ', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print(f'-='*40)
while True:
    busca = int(input('Mostrar dados de que jogador? '))
    if busca == 999:
        break
    if busca >= len(time):
        print('Erro! Não existe o jogador com esse código!')
    else:
        print(f' --- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]["gols"]):
            print(f'\tNo jogo {i+1} fez {g} gols.')
    print('-='*40)
print(f'<< Volte sempre >>')
