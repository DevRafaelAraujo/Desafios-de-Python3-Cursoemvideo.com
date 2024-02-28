def metade(valor, forma=True):
    res = valor / 2
    return res if forma is False else moeda(res)

def dobro(valor, forma=True):
    res = valor * 2
    return res if forma is False else moeda(res)

def aumentar(valor, taxa=10, forma=True):
    res = valor + (valor * taxa/100)
    return res if forma is False else moeda(res)

def diminuir(valor, taxa=10, forma=True):
    res = valor - (valor * taxa/100)
    return res if forma is False else moeda(res)


def moeda(valor, moeda='R$'):
    return f'{moeda}{valor:.2f}'.replace('.', ',')


def resumo(valor, aumento, reducao):
    print('-' * 30)
    print(f'{'RESUMO DO VALOR':^30}')
    print('-' * 30)
    print(f'{'Preço analisado:':<18} {moeda(valor)}')
    print(f'{'Dobro do preço:':<18} {dobro(valor)}')
    print(f'{'Metade do preço':<18} {metade(valor)}')
    print(f'{aumento}{'% de aumento:':<16} {aumentar(valor)}')
    print(f'{reducao}{'% de redução:':<16} {diminuir(valor)}')