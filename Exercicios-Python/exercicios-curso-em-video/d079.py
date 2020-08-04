v = []
while True:
    n = int(input('Digite um valor: '))
    if n in v:
        print('Valor duplicado! Não vou adicionar...')
    if n not in v:
        print('Valor adicionado com sucesso...')
        v.append(n)
    while True:
        q = input('Quer continuar? [S/N] ').upper().strip()[0]
        if q in 'SN':
            break
    if q in 'N':
        break
    print(30*'-')
print(40*'-=')
v.sort()
print(f'Você digitou os valores: {v}')