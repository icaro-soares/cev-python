nome_completo = str(input('Nome Completo: ')).strip().title()
nome_separado = nome_completo.split()
print(f"""Seu primeiro nome é {nome_separado[0]}
e seu último nome é {nome_separado[-1]}""")
