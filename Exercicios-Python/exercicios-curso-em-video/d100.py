from random import randint
from time import sleep
l = []
def s():
    print('Sorteando 5 valores... Temos a lista: ', end='')
    for c in range(0,5):
        sleep(1)
        p = randint(0,9)
        l.append(p)
        print(p, end=', ')
    print('PRONTO!')
def sp():
    print(f'Somando os valores pares de {l}, temos ', end='')
    spar=0
    for n in l:
        if n %2 == 0:
            spar+=n
    print(spar)
s()
sp()