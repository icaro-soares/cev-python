"""
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""
from random import randint

dados = {
        'jogador1':randint(1, 6),
        'jogador2':randint(1, 6),
        'jogador3':randint(1, 6),
        'jogador4':randint(1, 6)
}
for k, v in dados.items():
    print(f'O jogador {k} tirou {v} no dado')
print('-='*30)
print(f'{"ranking".upper():^60}')
print('-='*30)
