def ajuda():
    from time import sleep
    while True:
        sleep(0.3)
        print('\033[m\033[42m-' * 30)
        print(f'{'SISTEMA DE AJUDA PyHELP':^30}')
        print('-' * 30)
        sleep(0.3)
        f = input(f'\033[mFunção ou Biblioteca > \033[44m').strip()
        sleep(0.3)
        if f == 'FIM' or f == 'fim':
            print('\033[m\033[41m-' * 40)
            print(f'{'Até logo!!!':^40}')
            print('-' * 40)
            break
        print('-' * 40)
        print(f'{'Acessando o manual do comando':>32} {f}')
        print('-' * 40)
        print('\033[7:40m')
        sleep(0.3)
        help(f)


ajuda()
