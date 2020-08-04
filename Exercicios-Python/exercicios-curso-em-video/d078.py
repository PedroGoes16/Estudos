l = []
p = []
pme = []
for i in range(0,5):
    l.append(int(input(f'Digite um valor para a posição {i}: ')))
c = 0
for v in l:
    if v == max(l):
        p.append(c)
    if v == min(l):
        pme.append(c)
    c+=1
print(40*'-=')
print(f'Você digitou os valores: {l}')
print(f'O maior valor digitado foi {max(l)} na(s) posição(ões): ', end='')
for n in p:
    print(f'{n}', end=', ')
print(f'\nO menor valor digitado foi {min(l)} na(s) posição(ões): ', end='')
for n in pme:
    print(f'{n}', end=', ')
