"""
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios. Guarde esses resultados em um dicionário. No final, coloque esse dicionário em ordem, sabendo que o vencedor tirou o maior número no dado.
"""
from random import randint
from time import sleep

c = 1
dados = {
        'jogador1':randint(1, 6),
        'jogador2':randint(1, 6),
        'jogador3':randint(1, 6),
        'jogador4':randint(1, 6)
}
for k, v in dados.items():
    print(f'O jogador {k} tirou {v} no dado')
    sleep(1)
dict_decrescente = dict(sorted(dados.items(), reverse=True))
print('-='*30)
print(f'{"ranking".upper():^60}')
print('-='*30)

for k, v in dict_decrescente.items():
    print(f'{c}º Lugar {k} com {v}')
    c+=1
    