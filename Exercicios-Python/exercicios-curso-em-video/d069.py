m = h = mu = 0
while True:
    print(25*'-')
    print('   CADASTRE UMA PESSOA')
    print(25*'-')
    i = int(input('Idade: '))
    if i > 17:
        m+=1
    while True:
        s = input('Sexo: [M/F] ').strip().upper()[0]
        if s in 'MF':
            break
    print(25*'-')
    if s == 'M':
        h+=1
    if s == 'F' and i < 21:
        mu+=1
    while True:
        q = input('Quer continuar? [S/N] ').strip().upper()[0]
        if q in 'SN':
            break
    if q == 'N':
        break
print(f'====== FIM DO PROGRAMA ======\nTotal de pessoas com mais de 18 anos: {m}\nAo todo temos {h} homens cadastrados.\nE temos {mu} mulheres com menos de 20 anos.')