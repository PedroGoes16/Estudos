v = [[],[]]
for c in range(1,8):
    n = int(input(f'Digite o {c}° valor: '))
    if n%2==0:
        v[0].append(n)
    if n%2==1:
        v[1].append(n)
v[0].sort()
v[1].sort()
print(f'Os valores pares digitados foram: {v[0]}')
print(f'Os valores ímpares digitados foram: {v[1]}')