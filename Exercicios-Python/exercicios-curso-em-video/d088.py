from random import randint
from time import sleep
print(40*'-')
print(f'{"JOGA NA MEGA SENA":^40}')
print(40*'-')
q = int(input('Quantos jogos você quer que eu sorteie? '))
print(f'-=-=-=-=-= SORTEANDO {q} JOGOS =-=-=-=-=-')
for i in range(0,q):
    p = []
    while len(p)!=6:
        n = randint(1,60)
        if n not in p:
            p.append(n)
    p.sort()
    print(f'Jogo {i+1}: {p[:]}')
    p.clear()
    sleep(1)
print(f'{"BOA SORTE!":=^40}')