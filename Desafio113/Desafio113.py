def leiaint(msg):
    while True:
        try:
            n = int(input(f'\033[m{msg}'))
        except KeyboardInterrupt:
            print()
            print('O usuário não digitou o valor.')
            n = 0
            return n
            break
        except:
            print('\033[31mERRO!!! Número digitado inválido.')
        else:
            return n


def leiafloat(msg):
    while True:
        try:
            r = float(input(f'\033[m{msg}'))
        except KeyboardInterrupt:
            print()
            print('O usuário não digitou um valor.')
            r = 0
            return r
            break
        except:
            print('\033[31mERRO!!! Número digitado inválido.')
        else:
            return r


n = leiaint('Digite um número inteiro: ')
r = leiafloat('Digite um número real: ')
print(f'O número inteiro é {n} e o número real é {r}')
