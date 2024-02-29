def leiadinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(f'\033[m{msg}')).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[0;31mERRO: \"{entrada}\" é um preço inválido!')
        else:
            valido = True
            return float(entrada)
