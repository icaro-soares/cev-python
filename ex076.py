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
