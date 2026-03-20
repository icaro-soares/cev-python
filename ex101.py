"""
Crie um programa que tenha uma função chamada voto() que vai receber como parâmetro o ano de nascimento de uma pessoa, retornando um valor literal indicando se uma pessoa tem voto NEGADO, OPCIONAL ou OBRIGATÓRIO nas eleições.
"""
from datetime import datetime
    

def voto(nascimento):
    """
    -> Função para saber situação de voto
    :param nascimento: usa ano de nascimento do usuário
    :var idade: calcula a idade do usuario
    :var permitido: guarda a situação do usuário
    """
    global idade
    idade = datetime.now().year - nascimento
    if idade <= 15:
        permitido = 'Negado'
        return permitido
    elif idade == 16 or idade == 17 or idade >= 65:
        permitido = 'Opcional'
        return permitido
    else:
        permitido = 'Obrigatório'
        return permitido


ano_nascimento = int(input('Ano de nascimento: '))
situação = voto(ano_nascimento)
idade = datetime.now().year - ano_nascimento
print(f'Sua idade é {idade} anos.')
print(f'Situação de voto: {situação}')
help(voto)
