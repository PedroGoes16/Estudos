d = {}
l = []
while True:
    d['nome'] = input('Nome: ')
    while True:
        d['sexo'] = input('Sexo: [M/F] ').strip().upper()[0]
        if d['sexo'] not in 'MF':
            print('ERRO! Por favor, digite apenas M ou F.')
        if d['sexo'] in 'MF':
            break
    d['idade'] = int(input('Idade: '))
    while True:
        q = input('Quer continuar? [S/N] ').strip().upper()[0]
        if q in 'SN':
            break
        else:
            print('ERRO! Responda apenas S ou N.')
    l.append(d.copy())
    print(20*'-')
    if q == 'N':
        break
print(30*'-=')
print(f'- O grupo tem {len(l)} pessoas.')
i = 0
for c in l:
    i+=c['idade']
print(f'- A média de idade é de {i/len(l):.2f} anos.')
print(f'- As mulheres cadastradas foram: ',end='')
for c in l:
    if c['sexo'] == 'F':
        print(c['nome'], end=', ')
print()
print('- Listas de pessoas que estão acima da média: ')
for c in l:
    if c['idade'] > i/len(l):
        print()
        for b,v in c.items():
            print(f'{b} = {v}; ', end='')
        print()
print('<<ENCERRADO>>')