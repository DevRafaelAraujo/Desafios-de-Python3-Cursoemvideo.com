from Desafio107 import moeda

n = float(input('Digite o preço: R$'))
print(f'A metade de {moeda.moeda(n)} é {moeda.metade(n)}')
print(f'O dobro de {moeda.moeda(n)} é {moeda.dobro(n)}')
print(f'Aumentando 10% de {moeda.moeda(n)} temos {moeda.aumentar(n)}')
print(f'Reduzindo 10% de {moeda.moeda(n)} temos {moeda.diminuir(n)}')
