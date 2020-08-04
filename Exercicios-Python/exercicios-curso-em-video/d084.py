g = []
d = []
while True:
    d.append(input('Nome: '))
    d.append(float(input('Peso (Kg): ')))
    g.append(d[:])
    d.clear()
    while True:
        q = input('Quer continuar? [S/N] ').strip().upper()[0]
        if q in 'SN':
            break
    if q == 'N':
        break
    print(25*'-')
print(30*'-=')
print(f'Ao todo, você cadastrou {len(g)} pessoas.')
me = ma = 0
for p in range(0, len(g)):
    if g[p][1] < me or p == 0:
        me = g[p][1]
    if g[p][1] > ma:
        ma = g[p][1]
print(f'O maior peso foi de {ma}Kg. Peso de: ',end='')
for p in range(0, len(g)):
    if g[p][1] == ma:
        print(g[p][0], end=', ')
print(f'\nO menor peso foi de {me}Kg. Peso de: ', end='')
for p in range(0,len(g)):
    if g[p][1]==me:
        print(g[p][0], end=', ')