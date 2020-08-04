l = []
while True:
    l.append(int(input('Digite um valor: ')))
    while True:
        q = input('Quer continuar? [S/N] ').upper().strip()[0]
        if q in 'SN':
            break
    if q in 'N':
        break
    print(17*'--')
print(30*'-=')
print(f'Você digitou {len(l)} elementos.')
p = l[:]
p.sort(reverse=True)
print(f'Os valores em ordem decrescente são: {p}.')
c=0
if 5 in l:
    print('O valor 5 faz parte da lista, e está nas posições: ',end='')
    for n in l:
        if n == 5:
            print(c, end=', ')
        c+=1
else:
    print('O valor 5 não faz parte da lista.')