from time import sleep
from Desafio115 import arquivo

texto = {'azul': '\033[34m',
         'amarelo': '\033[33m',
         'verde': '\033[32m',
         'padrao': '\033[m',
         'vermelho': '\033[31m'}


def titulo(msg):
    print(f'{texto['padrao']}-' * 50)
    print(f'{msg:^50}')
    print('-' * 50)


def principal(opcoes):
    while True:
        sleep(0.5)
        titulo('MENU PRINCIPAL')
        sleep(0.5)
        for c, item in enumerate(opcoes):
            print(f'{texto['amarelo']}{c+1} - {texto['azul']}{item}')
        print(f'{texto['padrao']}-' * 50)
        sleep(0.5)
        try:
            op = int(input(f'{texto['verde']}Sua opção:{texto['padrao']} '))
            sleep(0.5)
            if op == 1:
                arquivo.lerarquivo('cursoemvideo.txt')
            elif op == 2:
                titulo('Opção 2')
            elif op == 3:
                titulo('Saindo do sistema... Até logo!')
                break
            else:
                print(f'{texto['vermelho']}ERRO! Por favor digite uma opção válida.')
        except:
            print(f'{texto['vermelho']}ERRO! Digite um número válido.')
