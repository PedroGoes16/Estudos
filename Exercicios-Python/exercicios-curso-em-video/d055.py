g = []
for c in range(1,6):
    p = float(input(f'Digite o peso da pessoa {c} em Kg: '))
    g.append(p)
g.sort()
print(f'O menor peso foi {g[0]} Kg enquanto o maior peso foi {g[4]} Kg.')