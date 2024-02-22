def metade(valor):
    res = valor / 2
    return res

def dobro(valor):
    res = valor * 2
    return res

def aumentar(valor, taxa=10):
    res = valor + (valor * taxa/100)
    return res

def diminuir(valor, taxa=10):
    res = valor - (valor * taxa/100)
    return res
