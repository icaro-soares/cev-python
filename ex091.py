"""
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""
from random import randint
from time import sleep

valores = {}
valores['jogador1'] = randint(1, 6)
valores['jogador2'] = randint(1, 6)
valores['jogador3'] = randint(1, 6)
valores['jogador4'] = randint(1, 6)
for k, v in valores.items():
    print(f'O {k} tirou {v} no dado')
    sleep(1)
print('-='*30)
print(f'{"ranking":^60}'.upper())
print('-='*30)
valores_inverso = dict(sorted(valores.items(), key=lambda item: item[1], reverse=True))
c = 1
while c <= 4:
    for k, v in valores_inverso.items():
        print(f'{c}º lugar {k} com {v}')
        c+=1
