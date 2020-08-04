l = []
p = []
i = []
while True:
    v = int(input('Digite um número: '))
    l.append(v)
    if v%2==0:
        p.append(v)
    else:
        i.append(v)
    while True:
        q = input('Quer continuar? [S/N] ').upper().strip()[0]
        if q in 'SN':
            break
    if q == 'N':
        break
print(30*'-=')
print(f'A lista completa é: {l}')
print(f'A lista de pares é: {p}')
print(f'A listsa de ímpares é: {i} ')