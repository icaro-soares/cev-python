"""Faça um programa que leia o nome completo de alguém e mostre
o primeiro e o último nome separadamente"""
nome_completo = str(input('Nome Completo: ')).strip().title()
nome_separado = nome_completo.split()
print(f"""Seu primeiro nome é {nome_separado[0]}
e seu último nome é {nome_separado[-1]}""")
