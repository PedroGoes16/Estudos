m = [[0,0,0], [0,0,0], [0,0,0]]
sp = st = 0
for l in range(0,3):
    for c in range(0,3):
        m[l][c] = int(input(f'Digite um número para [{l}, {c}]: '))
        if m[l][c]%2==0:
            sp+=m[l][c]
print(30*'==')
for l in range(0,3):
    st+=m[l][2]
    for c in range(0,3):
        print(f'[{m[l][c]:^5}]',end='')
    print()
print(30*'-=')
print(f'A soma de todos os valores pares é {sp}.')
print(f'A soma dos valores da terceira coluna é {st}.')
print(f'O maior valor da segunda linha é {max(m[1])}.')