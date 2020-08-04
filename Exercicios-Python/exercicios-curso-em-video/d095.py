l = []
j = {}
p = []
while True:
    j['nome'] = input('Nome do Jogador: ')
    q = int(input(f'Quantas partidas {j["nome"]} jogou? '))
    p.append(q)
    j['gols'] = []
    for c in range(0,q):
        j['gols'].append(int(input(f'Quantos gols na partida {c}? ')))
    j['total'] = sum(j['gols'])
    l.append(j.copy())
    while True:
        q = input('Quer continuar? [S/N] ').upper().strip()[0]
        if q in 'SN':
            break
    if q == "N":
        print(30*'-=')
        break
    print(30 * '-')
print(f'{"Cod":<4}{"Nome":<20}{"Gols":<20}{"Total":<5}')
print(50*'-')
for c,v in enumerate(l):
    print(f'{c:^4}{v["nome"]:<20}{str(v["gols"]):<20}{v["total"]:<5}')
print(30*'-=')
while True:
    d = int(input('Mostrar dados de qual jogador? (999 p/ sair) '))
    if d == 999:
        break
    if d >= len(l) or d<0:
        print(f'ERRO! Não existe jogador com o código {d}! Tente novamente.')
        print(60*'-')
    else:
        print(f'-- LEVANTAMENTO DO JOGADOR {l[d]["nome"]}:')
        print(f'O jogador {l[d]["nome"]} jogou {p[d]} partidas.')
        for c, v in enumerate(l[d]["gols"]):
            print(f'   => Na partida {c}, fez {v} gols.')
        print(f'Foi um total de {l[d]["total"]} gols.')
        print(60*'-')
print('<< VOLTE SEMPRE >>')