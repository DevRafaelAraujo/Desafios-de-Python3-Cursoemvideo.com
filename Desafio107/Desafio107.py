import moeda

n = float(input('Digite o preço: R$'))
print(f'A metade de R${n} é R${moeda.metade(n)}')
print(f'O dobro de R${n} é R${moeda.dobro(n)}')
print(f'Aumentando 10% de R${n}, temos R${moeda.aumentar(n)}')
print(f'Subtraindo 10% de R${n}, temos R${moeda.diminuir(n)}')
