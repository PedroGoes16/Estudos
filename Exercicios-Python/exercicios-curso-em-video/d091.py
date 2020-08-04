from random import randint
from time import sleep
from operator import itemgetter
j = {}
print('Valores sorteados: ')
print(30*'-')
j['jogador1'] = randint(1,6)
j['jogador2'] = randint(1,6)
j['jogador3'] = randint(1,6)
j['jogador4'] = randint(1,6)
for c,v in j.items():
    sleep(1)
    print(f'O {c} tirou {v} no dado.')
print(30*'-')
print('Ranking dos jogadores:')
print(30*'-')
sleep(1)
r = sorted(j.items(), key=itemgetter(1), reverse = True)
for c,v in enumerate(r):
    print(f'O {c+1}º lugar: {v[0]} com {v[1]}.')
    sleep(1)