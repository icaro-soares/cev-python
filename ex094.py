galera = []
pessoa = {}
soma = media = 0
while True:
    pessoa['nome'] = str(input('Nome: '))
    while True:
        pessoa['sexo'] = str(input('Sexo: '))[0]
        if pessoa['sexo'] in 'MmFf':
            break
        print('ERRO! Apenas M ou F!')
    pessoa['idade'] = int(input('Idade: '))
    soma+=pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar [S/N]: '))[0]
        if resp in 'SsNn':
            break
        print('ERRO! Apenas S ou N!')
    if resp in 'Nn':
        break
print('-='*30)
media = soma/len(galera)
print(f'A) No total foram cadastradas {len(galera)} pessoas.')
print(f'B) A média de idade do grup é {media:5.2f} anos.')
print(f'C) Nome das mulheres cadastradas ', end='')
for p in galera:
    if p['sexo'] in 'Ff':
        print(f'{p["nome"]}', end=' ')
print(f'\nD) Nome das pessoas acima da média: ', end='')
for p in galera:
    if p['idade'] >= media:
        print('     ')
        for k, v in p.items():
            print(f'{k} = {v}', end=' ')
print(f'\n<<< ENCERRADO >>>')
