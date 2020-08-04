l = []
p = []
i = []
while True:
    l.append(int(input('Digite um número: ')))
    while True:
        q = input('Quer continuar? [S/N] ').upper().strip()[0]
        if q in 'SN':
            break
    if q =='N':
        break
for n in l:
    if n %2==0:
        p.append(n)
    if n%2==1:
        i.append(n)
print(30*'-=')
print(f'A lista completa é: {l}')
print(f'A lista de pares é: {p}')
print(f'A lista de ímpares é: {i}')