"""
Crie uma tupla com os 20 primeiros colocados da tabela do campeonato brasileiro
de futebol na ordem de colocação. Depois mostre:
a) Apenas os cinco primeiro colocados
b) Os últimos quatro colocados
c) Uma lista com os times em ordem alfabética
d) Em que posição está o time 'corinthians'
"""
times = (
        'Flamengo', 'Palmeiras', 'Cruzeiro', 'Mirassol', 'Fluminense', 'Botafogo',
        'Bahia', 'São Paulo', 'Grêmio', 'Bragantino', 'Atlético-MG', 'Santos',
        'Corinthians', 'Vasco da Gama', 'EC Vitória', 'Internacional', 'Ceará SC',
        'Fortaleza', 'Juventude', 'Sport Recife'
)
print('Lista de times:')
for t in range(len(times)):
    print(times[t])
print('-='*30)
print('Os cinco primeiros colocados são:')
for t in range(0, 5):
    print(f'{times[t]}')
print('-='*30)
print('Os últimos quatro colocados:')
for t in range(-4, 0):
    print(f'{times[t]}')
print('-='*30)
print('Lista em ordem alfabética:')
print(sorted(times))
print('-='*30)
print(f'O Corinthians está em {times.index('Corinthians')+1}º lugar')
