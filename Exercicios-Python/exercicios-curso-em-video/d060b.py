n = int(input('Digite um número para descobrir seu fatorial: '))
f = 1
for c in range(1, n+1):
    if c == 1:
        print(f'{n}! = {c}', end='')
    if c > 1:
        print(f' x {c}', end='')
    f = f*c
print(f' = {f}')
print(f'\033[33mO fatorial de {n} é igual a {f}\033[m')