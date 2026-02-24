"""Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final mostre:
A média de idade do grupo.
Qual é o nome do homem mais velho
Quantas mulheres têm menos de 21 anos."""
soma = media_idade = mais_velho = menos_21 = 0
homem_mais_velho = ''
for c in range(0, 4):
    nome = str(input('Nome: ')).strip().title()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    print('-=' * 30)
    soma += idade
    media_idade = soma/4
    if c == 1:
        mais_velho = idade
    else:
        if idade > mais_velho and sexo == 'M':
            mais_velho = idade
            homem_mais_velho = nome
    if sexo == 'F' and idade < 21:
        menos_21 += 1
print(f'A média de idade do grupo é: {media_idade:.0f}')
print(f'O homem mais velho se chama {homem_mais_velho} e têm {mais_velho} anos')
print(f'{menos_21} mulher(s) têm menos de 21 anos')
