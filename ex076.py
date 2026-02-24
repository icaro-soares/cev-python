"""
Crie um programa que tenha uma tupla única com nomes de produtos e seus preços
respectivamente em sequência. No final mostre uma listagem de preços organizando
os dados de forma tabular
"""
produtos = (
        'TV', 2_000,
        'Home Theater', 2_900,
        'Smartphone', 3_500,
        'Sound Bar', 1_000,
        'iPhone', 8_000
)
for item in range(len(produtos)):
    if item % 2 == 0:
        print(f'{produtos[item]:.<30}',end='')
    else:
        print(f'R${produtos[item]:>7.2f}')
