def leiaint(msg):
    print('-' * 50)
    while True:
        n = input(f'{msg}')
        if n.isnumeric():
            break
        else:
            print(f'ERRO! Digite um número válido.')
    return n


n = leiaint('Digite um número: ')
print(f'Você acabou de digitar o número {n}')