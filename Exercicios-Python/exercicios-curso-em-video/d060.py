n = int(input('Digite um número para descobrir seu fatorial: '))
c = n
f = 1
while c >= 1:
    f = f*c
    print(f'{c}', end='')
    print(f' x ' if c > 1 else ' = ',end='')
    c -= 1
print(f'{f}')
print(f'\033[1;34mO fatoria de {n} é igual a {f}.\033[m')