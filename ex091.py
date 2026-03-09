"""
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""
from random import randint
from time import sleep

jogo = {}
c = 1
jogo['j1'] = randint(1, 6)
jogo['j2'] = randint(1, 6)
jogo['j3'] = randint(1, 6)
jogo['j4'] = randint(1, 6)
for k, v in jogo.items():
    print(f'O jogador {k} tirou {v} no dado')
    sleep(1)
print('-='*30)
print(f'{"ranking".upper():^60}')
print('-='*30)
jogo_inverso = dict(sorted(jogo.items(), key=lambda item: item[1], reverse=True))
for k, v in jogo_inverso.items():
    sleep(1)
    print(f'{k} em {c}º lugar com {v}')
    c+=1
