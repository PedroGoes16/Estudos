l = []
d = []
while True:
    d.append(input('Nome: '))
    d.append(float(input('Nota 1: ')))
    d.append(float(input('Nota 2: ')))
    l.append(d[:])
    d.clear()
    while True:
        q = input('Quer continuar? [S/N] ').upper().strip()[0]
        print(25*'-')
        if q in 'SN':
            break
    if q == 'N':
        break
print(f'N°  NOME          MÉDIA')
print(25*'-')
for c in range(0,len(l)):
    m = (l[c][1]+l[c][2])/2
    print(f'{c:<3}{l[c][0]:<15}{m:^5.1f}')
while True:
    print(60*'-')
    p = int(input('Mostrar notas de qual aluno? (999 interrompe) '))
    if p == 999:
        break
    if p >= len(l):
        print('Esse número não se refere a nenhum aluno!')
    else:
        print(f'Notas de {l[p][0].strip()} são {l[p][1:3]}')
print(f'{"FINALIZADO":=^57}')