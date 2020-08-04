def ficha():
    print(30*'-')
    n = str(input('Nome do Jogador: '))
    if n == '':
        n = '<desconhecido>'
    g = str(input('Números de Gols: '))
    if g.isnumeric():
        g = int(g)
    else:
        g = 0
    print(f'O jogador {n} fez {g} gol(s) no campeonato.')


ficha()