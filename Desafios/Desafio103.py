def ficha(nome='<desconhecido>',gols=0):
    print('-' * 50)
    print(f'O jogador {nome}, marcou {gols} gols no campeonato.')

n = str(input('Nome do jogador: '))
g = str(input('Gols marcados: '))
if n.strip() == '':
    if g.isnumeric():
        ficha(gols=g)
    else:
        ficha()
else:
    if g.isnumeric():
        ficha(n, g)
    else:
        ficha(n)
