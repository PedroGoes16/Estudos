j = {}
j['nome'] = input('Nome do Jogador: ')
q = int(input(f'Quantas partidas {j["nome"]} jogou? '))
j['gols'] = []
for c in range(0,q):
    j['gols'].append(int(input(f'Quantos gols na partida {c}? ')))
print(30*'-=')
j['total'] = sum(j['gols'])
print(j)
print(30*'-=')
for c,v in j.items():
    print(f'O campo {c} tem o valor {v}.')
print(30*'-=')
print(f'O jogador {j["nome"]} jogou {q} partidas.')
for c, v in enumerate(j["gols"]):
    print(f'   => Na partida {c}, fez {v} gols.')
print(f'Foi um total de {j["total"]} gols.')
