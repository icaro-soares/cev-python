from rich import print
from time import sleep


print('Bem vindo ao [blue]Interactive Help[/blue]!')
comando = ' '
while True:
    if comando != 'fim':
        comando = str(input('Digite um comando: ')).strip()
        help(comando)
    else:
        print('[red]Encerrando aplicação...[/red]')
        sleep(2)
        break
