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

